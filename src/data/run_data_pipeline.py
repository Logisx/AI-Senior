from src.utils.logging import logger
from src.data.pipelines.api_data_download import DataDownloadPipeline

if __name__ == "__main__":
    try:
        logger.info("Stage 1: Data download started")
        data_download_pipeline = DataDownloadPipeline()
        data_filepath = data_download_pipeline.run()
        logger.info("Stage 1: Data download completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 1: Data download failed")
        raise e