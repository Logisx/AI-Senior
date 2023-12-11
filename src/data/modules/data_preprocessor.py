import os
import hashlib
from typing import Optional, List
from pydantic import BaseModel
from tqdm import tqdm
from pathlib import Path
from unstructured.cleaners.core import clean, replace_unicode_quotes, clean_non_ascii_chars
from unstructured.staging.huggingface import chunk_by_attention_window

from src.utils.logging import logger
from config.paths import DATA_RAW_DIR, DATA_PROCESSED_DIR
from src.utils.file_management import FileManagement
from src.utils.configuration_management import ConfigurationManagement


class Document(BaseModel):
    id: str
    metadata: Optional[dict] = {}
    text: Optional[list] = []
    chunks: Optional[list] = []
    embeddings: Optional[list] = []

class DataPreprocessor:
    def __init__(self):
        self.__params = ConfigurationManagement.get_data_transformation_params()
        self.__news_data = FileManagement.read_json(Path(os.path.join(DATA_RAW_DIR, self.__params.news_data_filename)))

    def run(self) -> Path:
        logger.info("Processing news data")
        documents_list = []
        for article_data in tqdm(self.__news_data):
            result = self.__process_article_data(article_data=article_data)
            documents_list.append(result)
        logger.info("Saving documents to json")
        documents_filepath = Path(os.path.join(DATA_PROCESSED_DIR, f"documents_{self.__params.collection_name}.json"))
        self.__save_documents_to_json(documents_list, documents_filepath)
        return documents_filepath
    
    def __process_article_data(self, article_data: dict) -> Document:
        document = self.__parse_document(article_data)
        document = self.__chunk_document(document)
        document = self.__embed_document(document)
        return document

    def __parse_document(self, article_data: dict) -> Document:
        document_id = hashlib.md5(article_data['description'].encode()).hexdigest()
        document = Document(id = document_id)

        article_data['title'] = clean_non_ascii_chars(replace_unicode_quotes(clean(article_data['title'])))
        article_data['description'] = clean_non_ascii_chars(replace_unicode_quotes(clean(article_data['description'])))
        article_data['content'] = clean_non_ascii_chars(replace_unicode_quotes(clean(article_data['content'])))

        document.text = [article_data['title'], article_data['description'], article_data['content']]
        document.metadata['author'] = article_data['author']
        document.metadata['title'] = article_data['title']
        document.metadata['url'] = article_data['url']
        document.metadata['date'] = article_data['publishedAt']

        return document
    
    def __chunk_document(self, document: Document) -> Document:
        chunks = []
        for text in document.text:
            chunks += chunk_by_attention_window(text, 
                            self.__params.tokenizer,
                            max_input_size=self.__params.vector_size)
            
        document.chunks = chunks
        return document
    
    def __embed_document(self, document: Document) -> Document:
        for chunk in document.text:
            inputs = self.__params.tokenizer(chunk,
                            padding=True,
                            truncation=True,
                            return_tensors="pt",
                            max_length=self.__params.vector_size)
        
            result = self.__params.model(**inputs)
            embeddings = result.last_hidden_state[:, 0, :].cpu().detach().numpy()
            lst = embeddings.flatten().tolist()
            document.embeddings.append(lst)
        return document
    
    def __save_documents_to_json(self, documents_list: List[Document], file_path: Path) -> None:
        documents_data = [
            {
                "id": document.id,
                "metadata": document.metadata,
                "text": document.text,
                "chunks": document.chunks,
                "embeddings": document.embeddings
            } for document in documents_list
        ]
        FileManagement.save_to_json(documents_data, file_path)