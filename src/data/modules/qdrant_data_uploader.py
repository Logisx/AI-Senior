import os
from typing import Optional, List
from tqdm import tqdm
from pydantic import BaseModel

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.http.api_client import UnexpectedResponse

from src.utils.logging import logger
from config.paths import DATA_PROCESSED_DIR
from src.utils.file_management import FileManagement
from src.utils.configuration_management import ConfigurationManagement
from src.data.modules.data_preprocessor import Document

class QdrantDataUploader:
    def __init__(self):
        self.__params = ConfigurationManagement.get_qdrant_upload_params()
        self.__url = ConfigurationManagement.get_qdrant_api_url()
        self.__api_key = ConfigurationManagement.get_qdrant_api_key()
    
    def run(self):
        self.__init_qdrant()
        logger.info("Reading documents from json")
        documents_filepath = os.path.join(DATA_PROCESSED_DIR, f"documents_{self.__params.collection_name}.json")
        documents_data = FileManagement.read_json(documents_filepath)

        logger.info("Form documents from data")
        documents_list = [Document(**document) for document in documents_data]

        logger.info("Uploading documents to Qdrant")
        for document in tqdm(documents_list):
            self.__push_document_to_qdrant(document)

    def __init_qdrant(self) -> None:
        logger.info("Initializing Qdrant")
        self.__init_qdrant_client()
        self.__init_collection()

    def __init_qdrant_client(self) -> None:
        self.__qdrant_client = QdrantClient(
            url=self.__url,
            api_key=self.__api_key)
    
    def __init_collection(self) -> None:
        try:
            self.__qdrant_client.get_collection(collection_name=self.__params.collection_name)
        except (UnexpectedResponse, ValueError):
            self.__qdrant_client.recreate_collection(
                collection_name=self.__params.collection_name,
                vectors_config=VectorParams(
                    size=self.__params.vector_size,
                    distance=Distance.COSINE
                )
            )

    def __push_document_to_qdrant(self, document: Document) -> None:
        __payloads = self.__build_payloads(document)

        self.__qdrant_client.upsert(
            collection_name=self.__params.collection_name,
            points=[
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload=_payload
                )
                for idx, (vector, _payload) in enumerate(zip(document.embeddings, __payloads))
            ]
        )

    def __build_payloads(self, document: Document) -> List[dict]:
        payloads = []
        for chunk in document.chunks:
            payload = document.metadata
            payload.update({"text":chunk})
            payloads.append(payload)
        return payloads