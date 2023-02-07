from pathlib import Path

CONFIG_FILE_PATH = Path("configs/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH=Path("configs/schema.yaml")
TRAIN_FILE_PATH=Path("artifacts/data_ingestion/train_test/train/train.csv")
TEST_FILE_PATH=Path("artifacts/data_ingestion/train_test/test/test.csv")
SCHEMA_CLEAN_FILE_PATH=Path("configs/schema_clean.yaml")
TRAIN_ARRAY_FILE_PATH=Path("artifacts/data_preparation/clean_array/train_array.npy")
TEST_ARRAY_FILE_PATH=Path("artifacts/data_preparation/clean_array/test_array.npy")