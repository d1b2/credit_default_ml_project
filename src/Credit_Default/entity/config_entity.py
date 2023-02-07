from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    raw_data_dir: Path
    local_data_file: Path
    kaggle_file_path: Path
    unzip_dir: Path
    ingested_train_dir: Path
    ingested_test_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    report_dir: Path
    report_file_name: str
    report_page_file_name: str

@dataclass(frozen=True)
class DataPreparationConfig:
    root_dir: Path
    clean_csv_dir: Path
    clean_np_dir: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    base_accuracy: float
    model_df_dir: Path
    model_df_name: str

@dataclass(frozen=True)
class ModelTuningConfig:
    root_dir: Path
    model_scores: str
    model_name: str