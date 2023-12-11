from pathlib import Path

from src.utils.logging import logger
from src.data.modules.qdrant_data_uploader import QdrantDataUploader

class DataUploadPipe:
    def __init__(self):
        pass

    def run(self) -> Path:
        qdrant_data_uploader = QdrantDataUploader()
        qdrant_data_uploader.run()

if __name__ == "__main__":
    try:
        logger.info("Stage 3: Data upload started")
        data_upload_pipeline = DataUploadPipe()
        data_upload_pipeline.run()
        logger.info("Stage 3: Data upload completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 3: Data upload failed")
        raise e