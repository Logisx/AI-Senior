import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_RAW_DIR = os.path.join(ROOT_DIR, "data", "raw")
DATA_PROCESSED_DIR = os.path.join(ROOT_DIR, "data", "processed")
DATA_EXTERNAL_DIR = os.path.join(ROOT_DIR, "data", "external")

DATA_PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "config", "data-params.yaml")
MODEL_PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "config", "model-params.yaml")

if not Path(DATA_RAW_DIR).exists():
    os.makedirs(DATA_RAW_DIR, exist_ok=True)
