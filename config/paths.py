import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_RAW_DIR = os.path.join(ROOT_DIR, "data", "raw")
DATA_PROCESSED_DIR = os.path.join(ROOT_DIR, "data", "processed")
DATA_EXTERNAL_DIR = os.path.join(ROOT_DIR, "data", "external")
DATA_FINETUNING_DIR = os.path.join(ROOT_DIR, "data", "processed", "finetuning")

DATA_PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "config", "data-params.yaml")
MODEL_PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "config", "model-params.yaml")
INFERENCE_PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "config", "inference-params.yaml")

LOGS_DIR = os.path.join(ROOT_DIR, "logs")
MODELS_CACHE_DIR = os.path.join(ROOT_DIR, "models", "cache")

if not Path(DATA_RAW_DIR).exists():
    os.makedirs(DATA_RAW_DIR, exist_ok=True)
    os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)
    os.makedirs(DATA_EXTERNAL_DIR, exist_ok=True)
    os.makedirs(DATA_FINETUNING_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs(MODELS_CACHE_DIR, exist_ok=True)

