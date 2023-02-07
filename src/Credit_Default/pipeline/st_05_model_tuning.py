from Credit_Default.config import ConfigurationManager
from Credit_Default.components import ModelTuning
from Credit_Default import logger

STAGE_NAME = "Model Tuning stage"

def main():
    config = ConfigurationManager()
    model_tuning_config = config.get_model_tuning_config()
    model_tuning = ModelTuning(config=model_tuning_config) 
    model_tuning.best_model_csv()
    model_tuning.model_tuning_and_saving_parameters()
    model_tuning.saving_model_scores()
    model_tuning.saving_model()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e