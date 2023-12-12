import torch
import psutil
import subprocess
import numpy as np

from src.utils.logging import logger

class ComputationManager:
    @staticmethod
    def log_available_gpu_memory():
        """
        Logs the available GPU memory for each available GPU device.

        If no GPUs are available, logs "No GPUs available".

        Returns:
            None
        """

        if torch.cuda.is_available():
            for i in range(torch.cuda.device_count()):
                memory_info = subprocess.check_output(
                    f"nvidia-smi -i {i} --query-gpu=memory.free --format=csv,nounits,noheader",
                    shell=True,
                )
                memory_info = str(memory_info).split("\\")[0][2:]

                logger.info(f"GPU {i} memory available: {memory_info} MiB")
        else:
            logger.info("No GPUs available")

    @staticmethod
    def log_available_ram():
        """
        Logs the amount of available RAM in gigabytes.

        Returns:
            None
        """

        memory_info = psutil.virtual_memory()

        logger.info(
            f"Available RAM: {memory_info.available / (1024.0 ** 3):.2f} GB"
        )  # convert bytes to GB