from src.utils.logging import logger
from src.data.modules.training_data_generation import TrainingDataGenerator

if __name__ == '__main__':
    logger.info('Training data generation started.')
    training_data_generator = TrainingDataGenerator()
    training_data_generator.run()
    logger.info('Training data generation completed.')
