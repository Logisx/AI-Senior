from src.utils.logging import logger
from src.data.pipeline.data_download import DataDownloadPipe
from src.data.pipeline.data_preprocessing import DataPreprocessingPipe
from src.data.pipeline.data_upload import DataUploadPipe

if __name__ == "__main__":
    logger.info("<<<<< Data pipeline started >>>>>")
    try:
        logger.info("Stage 1: Data download started")
        data_download_pipeline = DataDownloadPipe()
        data_filepath = data_download_pipeline.run()
        logger.info("Stage 1: Data download completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 1: Data download failed")
        raise e
    
    try:
        logger.info("Stage 2: Data preprocessing started")
        data_preprocessing_pipeline = DataPreprocessingPipe()
        data_preprocessing_pipeline.run()
        logger.info("Stage 2: Data preprocessing completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 2: Data preprocessing failed")
        raise e
    
    try:
        logger.info("Stage 3: Data upload started")
        data_upload_pipeline = DataUploadPipe()
        data_upload_pipeline.run()
        logger.info("Stage 3: Data upload completed")
    except Exception as e:
        logger.exception(e)
        logger.error("Stage 3: Data upload failed")
        raise e
    
    logger.info("<<<<< Data pipeline completed >>>>>")