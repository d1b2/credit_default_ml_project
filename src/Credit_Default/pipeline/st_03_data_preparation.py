from Credit_Default.config import ConfigurationManager
from Credit_Default.components import DataPreparation
from Credit_Default import logger

STAGE_NAME = "Data Preparation stage"

def main():
    config = ConfigurationManager()
    data_preparation_config = config.get_data_preparation_config()
    data_preparation = DataPreparation(config=data_preparation_config)   
    data_preparation.null_checks()
    data_preparation.clean_education()
    data_preparation.clean_marriage()
    data_preparation.rename_target()
    data_preparation.smote_resampling()
    data_preparation.saving_resampled_and_clean_csv()
    data_preparation.saving_clean_np_array()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e