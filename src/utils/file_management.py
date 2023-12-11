import os
import json
import yaml
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from typing import List

from src.utils.logging import logger


class FileManagement():
    @staticmethod
    def save_to_json(data, file_path):
        """
        Save data to a JSON file.

        Args:
            data: The data to be saved.
            file_path: The path of the JSON file.

        Returns:
            None
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logger.info(f"Data saved to {file_path}")
    
    @staticmethod
    def read_json(file_path):
        """
        Read data from a JSON file.

        Args:
            file_path: The path of the JSON file.

        Returns:
            data: The data read from the JSON file.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
        logger.info(f"Data read from {file_path}")
        return data
    
    @staticmethod
    def read_yaml(path_to_yaml: Path) -> ConfigBox:
        """
        Read a YAML file and return its content as a ConfigBox object.

        Args:
            path_to_yaml (Path): The path to the YAML file.

        Returns:
            ConfigBox: The content of the YAML file as a ConfigBox object.

        Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs while reading the YAML file.
        """
        try:
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
                logger.info(f"yaml file: {path_to_yaml} loaded successfully")
                return ConfigBox(content)
        except BoxValueError:
            raise ValueError(f"yaml file: {path_to_yaml} is empty")
        except Exception as e:
            raise e
    