import os
from pathlib import Path
from dataclasses import dataclass
from typing import List
from datetime import datetime
from box import ConfigBox
from dotenv import find_dotenv, load_dotenv

from config.paths import DATA_PARAMS_FILE_PATH
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


class ConfigurationManagement:

    @staticmethod
    def get_newsapi_api_key():
        _ = load_dotenv(find_dotenv()) # read local .env file
        return os.environ["NEWSAPI_API_KEY"]

    @staticmethod 
    def get_newsapi_request_params():
        params = ConfigurationManagement.__read_data_params().newsapi_request

        newsapi_request_params = NewsApiRequestParams(
            language=params.language,
            sort_by=params.sort_by,
            page_size=params.page_size,
            page=params.page
        )

        return newsapi_request_params
    
    @staticmethod
    def get_news_download_params():
        params = ConfigurationManagement.__read_data_params().news_download

        news_download_params = NewsDownloadParams(
            num_requests=params.num_requests,
            from_date=params.from_date,
            to_date=params.to_date,
            queries_list=params.queries_list
        )

        return news_download_params

    @staticmethod
    def __read_data_params() -> ConfigBox:
        params = FileManagement.read_yaml(Path(DATA_PARAMS_FILE_PATH))
        return params
    
    