import os
from pathlib import Path
from dataclasses import dataclass
from typing import List
from datetime import datetime
from box import ConfigBox
from dotenv import find_dotenv, load_dotenv
from transformers import AutoTokenizer, AutoModel

from config.paths import DATA_PARAMS_FILE_PATH, MODEL_PARAMS_FILE_PATH
from src.utils.file_management import FileManagement

@dataclass 
class NewsApiRequestParams:
    language: str
    sort_by: str
    page_size: int
    page: int

@dataclass
class NewsDownloadParams:
    num_requests: int
    from_date: datetime
    to_date: datetime
    queries_list: List[str]

@dataclass
class DataTransformationParams:
    tokenizer: AutoTokenizer
    model: AutoModel
    vector_size: int
    collection_name: str
    news_data_filename: Path

@dataclass
class QdrantUploadParams:
    collection_name: str
    vector_size: int

class ConfigurationManagement:
    @staticmethod
    def get_newsapi_api_key() -> str:
        _ = load_dotenv(find_dotenv())
        return os.environ["NEWSAPI_API_KEY"]
    
    @staticmethod
    def get_qdrant_api_key() -> str:
        _ = load_dotenv(find_dotenv())
        return os.environ["QDRANT_API_KEY"]
    
    @staticmethod
    def get_qdrant_api_url() -> str:
        _ = load_dotenv(find_dotenv())
        return os.environ["QDRANT_API_URL"]

    @staticmethod 
    def get_newsapi_request_params() -> NewsApiRequestParams:
        params = ConfigurationManagement.__read_data_params().newsapi_request

        newsapi_request_params = NewsApiRequestParams(
            language=params.language,
            sort_by=params.sort_by,
            page_size=params.page_size,
            page=params.page
        )

        return newsapi_request_params
    
    @staticmethod
    def get_news_data_load_params() -> NewsDownloadParams:
        params = ConfigurationManagement.__read_data_params().news_download

        news_download_params = NewsDownloadParams(
            num_requests=params.num_requests,
            from_date=params.from_date,
            to_date=params.to_date,
            queries_list=params.queries_list
        )

        return news_download_params

    @staticmethod
    def get_data_transformation_params() -> DataTransformationParams:
        model_params = ConfigurationManagement.__read_model_params().model
        data_params = ConfigurationManagement.__read_data_params().data_transformation
        qdrant_params = ConfigurationManagement.__read_data_params().qdrant

        data_transformation_params = DataTransformationParams(
            tokenizer=AutoTokenizer.from_pretrained(model_params.base_model_name),
            model=AutoModel.from_pretrained(model_params.base_model_name),
            vector_size=qdrant_params.vector_size,
            collection_name=qdrant_params.collection_name,
            news_data_filename=data_params.news_data_filename
        )

        return data_transformation_params
    
    @staticmethod
    def get_qdrant_upload_params() -> ConfigBox:
        qdrant_params = ConfigurationManagement.__read_data_params().qdrant

        qdrant_upload_params = QdrantUploadParams(
            collection_name=qdrant_params.collection_name,
            vector_size=qdrant_params.vector_size
        )

        return qdrant_upload_params     

    @staticmethod
    def __read_data_params() -> ConfigBox:
        params = FileManagement.read_yaml(Path(DATA_PARAMS_FILE_PATH))
        return params
    
    @staticmethod
    def __read_model_params() -> ConfigBox:
        params = FileManagement.read_yaml(Path(MODEL_PARAMS_FILE_PATH))
        return params
    