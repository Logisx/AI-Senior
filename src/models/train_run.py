import os
import fire
from pathlib import Path
from beam import App, Image, Runtime, Volume, VolumeType

from src.utils.logging import logger
from config.paths import MODELS_CACHE_DIR, DATA_PROCESSED_DIR
from src.models.training_pipeline.api import TrainingAPI
from src.utils.computation_management import ComputationManager
from src.utils.configuration_management import ConfigurationManagement


training_app = App(
    name="train_qa",
    runtime=Runtime(
        cpu=4,
        memory="64Gi",
        gpu="A10G",
        image=Image(
            python_version="python3.10", 
            python_packages="src/models/requirements.txt"
            ),
    ),
    volumes=[
        Volume(path="./qa_dataset", name="qa_dataset"),
        Volume(
            path="./output",
            name="train_qa_output",
            volume_type=VolumeType.Persistent,
        ),
        Volume(
            path="./model_cache", name="model_cache", volume_type=VolumeType.Persistent
        ),
    ],
)


@training_app.run()
def train():
    __comet_api_key = ConfigurationManagement.get_comet_api_key()
    __comet_workspace = ConfigurationManagement.get_comet_workspace()
    __comet_project_name = ConfigurationManagement.get_comet_project_name()

    # Enable logging of model checkpoints.
    os.environ["COMET_LOG_ASSETS"] = "True"
    # Set to OFFLINE to run an Offline Experiment or DISABLE to turn off logging
    os.environ["COMET_MODE"] = "ONLINE"
    # Find out more about Comet ML configuration here: https://www.comet.com/docs/v2/integrations/ml-frameworks/huggingface/#configure-comet-for-hugging-face

    logger.info("#" * 100)
    ComputationManager.log_available_gpu_memory()
    ComputationManager.log_available_ram()
    logger.info("#" * 100)

    training_config = ConfigurationManagement.get_training_arguments()

    training_api = TrainingAPI.from_config(
        config=training_config,
        root_dataset_dir=DATA_PROCESSED_DIR,
        model_cache_dir=MODELS_CACHE_DIR,
    )

    training_api.train()
    

if __name__ == "__main__":
    fire.Fire(train)