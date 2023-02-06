from Credit_Default.config import ConfigurationManager
from Credit_Default.components import DataValidation
from Credit_Default import logger

STAGE_NAME = "Data Validation stage"

def main():
   
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)    
    data_validation.validate_number_of_columns()
    data_validation.is_numerical_column_exist()
    data_validation.validate_min_max_value()
    data_validation.data_drift_report_json() 
    data_validation.data_drift_report_html_page()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e