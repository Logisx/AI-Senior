import os
from pathlib import Path
from dataclasses import dataclass
from typing import List
from datetime import datetime
from box import ConfigBox
from dotenv import find_dotenv, load_dotenv
from transformers import AutoTokenizer, AutoModel, TrainingArguments

from config.paths import DATA_PARAMS_FILE_PATH, MODEL_PARAMS_FILE_PATH, LOGS_DIR, INFERENCE_PARAMS_FILE_PATH
from src.utils.file_management import FileManagement

@dataclass 
class NewsApiRequestParams:
    language: str
    sort_by: str
    page_size: int
    page: int

@dataclass
class NewsDownloadParams:
    num_requests: int
    from_date: datetime
    to_date: datetime
    queries_list: List[str]

@dataclass
class DataTransformationParams:
    tokenizer: AutoTokenizer
    model: AutoModel
    vector_size: int
    collection_name: str
    news_data_filename: Path

@dataclass
class QdrantUploadParams:
    collection_name: str
    vector_size: int

@dataclass
class TrainingDataGenerationParams:
    examples_filename: Path
    engine: str
    temperature: float
    max_tokens: int
    prompt_template: str


@dataclass
class InferenceParams:
    peft_model_id: str
    model_id: str
    model_template_name: str
    model_max_new_tokens: int
    model_temperature: float
    setup_device: str
    setup_debug: bool
    dataset_filename: Path


class ConfigurationManagement:
    @staticmethod
    def get_newsapi_api_key() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("NEWSAPI_API_KEY")
    
    @staticmethod
    def get_qdrant_api_key() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("QDRANT_API_KEY")
    
    @staticmethod
    def get_qdrant_api_url() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("QDRANT_API_URL")
    
    @staticmethod
    def get_openai_api_key() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("OPENAI_API_KEY")
    
    @staticmethod
    def get_comet_api_key() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("COMET_API_KEY")
    @staticmethod
    def get_comet_workspace() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("COMET_WORKSPACE")
    
    @staticmethod
    def get_comet_project_name() -> str:
        _ = load_dotenv(find_dotenv())
        return os.getenv("COMET_PROJECT_NAME")

    @staticmethod 
    def get_newsapi_request_params() -> NewsApiRequestParams:
        params = ConfigurationManagement.__read_data_params().newsapi_request

        newsapi_request_params = NewsApiRequestParams(
            language=params.language,
            sort_by=params.sort_by,
            page_size=params.page_size,
            page=params.page
        )

        return newsapi_request_params
    
    @staticmethod
    def get_news_data_load_params() -> NewsDownloadParams:
        params = ConfigurationManagement.__read_data_params().news_download

        news_download_params = NewsDownloadParams(
            num_requests=params.num_requests,
            from_date=params.from_date,
            to_date=params.to_date,
            queries_list=params.queries_list
        )

        return news_download_params

    @staticmethod
    def get_data_transformation_params() -> DataTransformationParams:
        model_params = ConfigurationManagement.__read_model_params().model
        data_params = ConfigurationManagement.__read_data_params().data_transformation
        qdrant_params = ConfigurationManagement.__read_data_params().qdrant

        data_transformation_params = DataTransformationParams(
            tokenizer=AutoTokenizer.from_pretrained(model_params.base_model_name),
            model=AutoModel.from_pretrained(model_params.base_model_name),
            vector_size=qdrant_params.vector_size,
            collection_name=qdrant_params.collection_name,
            news_data_filename=data_params.news_data_filename
        )

        return data_transformation_params
    
    @staticmethod
    def get_qdrant_upload_params() -> ConfigBox:
        qdrant_params = ConfigurationManagement.__read_data_params().qdrant

        qdrant_upload_params = QdrantUploadParams(
            collection_name=qdrant_params.collection_name,
            vector_size=qdrant_params.vector_size
        )

        return qdrant_upload_params     
    
    @staticmethod
    def get_training_data_generation_params() -> ConfigBox:
        params = ConfigurationManagement.__read_data_params().training_data_generation
        
        training_data_generation_params = TrainingDataGenerationParams(
            examples_filename=params.examples_filename,
            engine=params.engine,
            temperature=params.temperature,
            max_tokens=params.max_tokens,
            prompt_template=params.prompt_template
        )

        return training_data_generation_params

    @staticmethod
    def get_training_arguments() -> TrainingArguments:
        params = ConfigurationManagement.__read_model_params().training

        training_arguments = TrainingArguments(
            logging_dir=str(LOGS_DIR) + "/" + "training_logs",
            per_device_train_batch_size=params["per_device_train_batch_size"],
            gradient_accumulation_steps=params["gradient_accumulation_steps"],
            per_device_eval_batch_size=params["per_device_eval_batch_size"],
            eval_accumulation_steps=params["eval_accumulation_steps"],
            optim=params["optim"],
            save_steps=params["save_steps"],
            logging_steps=params["logging_steps"],
            learning_rate=params["learning_rate"],
            fp16=params["fp16"],
            max_grad_norm=params["max_grad_norm"],
            num_train_epochs=params["num_train_epochs"],
            warmup_ratio=params["warmup_ratio"],
            lr_scheduler_type=params["lr_scheduler_type"],
            evaluation_strategy=params["evaluation_strategy"],
            eval_steps=params["eval_steps"],
            report_to=params["report_to"],
            seed=params["seed"],
            load_best_model_at_end=params["load_best_model_at_end"],
            output_dir=params["output_dir"],
        )

        return training_arguments
    
    @staticmethod
    def get_model_params() -> ConfigBox:
        params = ConfigurationManagement.__read_model_params().model

        model_params = ConfigBox(
            base_model_name=params.base_model_name,
            template_name=params.template,
            max_new_tokens=params.max_new_tokens,
            temperature=params.temperature
        )

        return model_params

    @staticmethod
    def get_inference_params() -> ConfigBox:
        peft_model = ConfigurationManagement.__read_inference_params().peft_model
        model = ConfigurationManagement.__read_inference_params().model
        setup = ConfigurationManagement.__read_inference_params().setup
        dataset = ConfigurationManagement.__read_inference_params().dataset

        inference_params = InferenceParams(
            peft_model_id=peft_model.id,
            model_id=model.id,
            model_template_name=model.template_name,
            model_max_new_tokens=model.max_new_tokens,
            model_temperature=model.temperature,
            setup_device=setup.device,
            setup_debug=setup.debug,
            dataset_filename=dataset.filename
        )

        return inference_params

    @staticmethod
    def __read_data_params() -> ConfigBox:
        params = FileManagement.read_yaml(Path(DATA_PARAMS_FILE_PATH))
        return params
    
    @staticmethod
    def __read_model_params() -> ConfigBox:
        params = FileManagement.read_yaml(Path(MODEL_PARAMS_FILE_PATH))
        return params
    
    @staticmethod
    def __read_inference_params() -> ConfigBox:
        params = FileManagement.read_yaml(Path(INFERENCE_PARAMS_FILE_PATH))
        return params