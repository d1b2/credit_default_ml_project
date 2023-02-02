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