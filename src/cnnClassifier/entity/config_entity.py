from dataclasses import dataclass
from pathlib import Path


#create custom Return type
@dataclass(frozen=True)
class DataIngestionConfig:
    """
    represent the configuration required for data ingestion tasks
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path #taken from base model
    training_data: Path #taken from data ingestion
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list