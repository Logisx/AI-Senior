from pathlib import Path

from src.utils.logging import logger
from src.data.modules.newsapi_data_loader import NewsapiDataLoader


class DataDownloadPipe:
    def __init__(self):
        pass

    def run(self) -> Path:
        newsapi_data_download = NewsapiDataLoader()
        data_filepath = newsapi_data_download.download_news()
        return data_filepath

if __name__ == "__main__":
    try:
        logger.info("Stage 1: Data download started")
        data_download_pipeline = DataDownloadPipe()
        data_filepath = data_download_pipeline.run()
        logger.info("Stage 1: Data download completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 1: Data download failed")
        raise e