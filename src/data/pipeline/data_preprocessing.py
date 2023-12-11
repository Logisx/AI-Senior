from pathlib import Path

from src.utils.logging import logger
from src.data.modules.data_preprocessor import DataPreprocessor


class DataPreprocessingPipe:
    def __init__(self):
        pass

    def run(self) -> Path:
        data_preprocessor = DataPreprocessor()
        data_filepath = data_preprocessor.run()
        return data_filepath

if __name__ == "__main__":
    try:
        logger.info("Stage 2: Data preprocessing started")
        data_preprocessing_pipeline = DataPreprocessingPipe()
        data_preprocessing_pipeline.run()
        logger.info("Stage 2: Data preprocessing completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 2: Data preprocessing failed")
        raise e