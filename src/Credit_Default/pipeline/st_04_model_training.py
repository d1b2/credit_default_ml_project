from Credit_Default.config import ConfigurationManager
from Credit_Default.components import ModelTraining
from Credit_Default import logger

STAGE_NAME = "Model Training stage"

def main():
    config = ConfigurationManager()
    model_training_config= config.get_model_training_config()
    model_training = ModelTraining(config=model_training_config) 
    model_training.logistic_regression_model()
    model_training.knn_classifier_model()
    model_training.random_forest_classifier_model()
    model_training.model_dataframe()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e