from Credit_Default.constants import *
from Credit_Default.utils import *
from Credit_Default.entity import *

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH ) :
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir,
                            config.raw_data_dir,
                            config.unzip_dir,
                            config.ingested_train_dir,
                            config.ingested_test_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            raw_data_dir=config.raw_data_dir,
            local_data_file=config.local_data_file,
            kaggle_file_path=config.kaggle_file_path,
            unzip_dir=config.unzip_dir,
            ingested_train_dir=config.ingested_train_dir,
            ingested_test_dir=config.ingested_test_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        
        create_directories([config.root_dir,
                            config.report_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),           
            report_dir=Path(config.report_dir),
            report_file_name=config.report_file_name,
            report_page_file_name = config.report_page_file_name
        )

        return data_validation_config

    def get_data_preparation_config(self) -> DataPreparationConfig:
        config = self.config.data_preparation
        
        create_directories([config.root_dir,
                            config.clean_csv_dir,
                            config.clean_np_dir])

        data_preparation_config = DataPreparationConfig(
            root_dir = Path(config.root_dir),           
            clean_csv_dir = Path(config.clean_csv_dir),
            clean_np_dir = Path(config.clean_np_dir)
        )

        return data_preparation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        
        create_directories([config.root_dir,
                            config.model_df_dir])

        model_training_config = ModelTrainingConfig(
            root_dir = Path(config.root_dir), 
            base_accuracy = float(config.base_accuracy),
            model_df_dir = Path(config.model_df_dir),
            model_df_name = str(config.model_df_name)  
        )

        return model_training_config
    
    def get_model_tuning_config(self) -> ModelTuningConfig:
        config = self.config.model_tuning
        
        create_directories([config.root_dir])

        model_tuning_config = ModelTuningConfig(
            root_dir = Path(config.root_dir), 
            model_scores = str(config.model_scores),
            model_name = str(config.model_name)
        )

        return model_tuning_config