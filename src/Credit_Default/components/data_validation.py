import os
from pathlib import Path
import pandas as pd
from Credit_Default import logger
from Credit_Default.entity import *
from Credit_Default.constants import *
from Credit_Default.utils import *
import evidently
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.train = pd.read_csv(TRAIN_FILE_PATH)
        self.test = pd.read_csv(TEST_FILE_PATH)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

 

    def validate_number_of_columns(self):
        try:
            validation_status = False
            number_of_columns = len(self.schema["columns"])
            logger.info(f"Required number of columns: {number_of_columns}")
            logger.info(f"Train Data has columns: {len(self.train.columns)}")
            logger.info(f"Test Data has columns: {len(self.test.columns)}")
            
            if len(self.train.columns)==number_of_columns and len(self.test.columns)==number_of_columns:
                validation_status = True
            logger.info(f"Validation status of number of columns : {validation_status}")  
        except Exception as e:
            raise e
    
    def is_numerical_column_exist(self):
        try:
            numerical_columns = list(self.schema["numerical_columns"].split(" "))
            train_columns = self.train.columns
            test_columns = self.test.columns
            numerical_column_present = True
            missing_numerical_train_columns = []
            missing_numerical_test_columns = []
            for num_column in numerical_columns:
                if num_column not in train_columns:
                    numerical_column_present=False
                    missing_numerical_train_columns.append(num_column)
                if num_column not in test_columns:
                    numerical_column_present=False
                    missing_numerical_test_columns.append(num_column)
            if len(missing_numerical_train_columns)>0:
                logger.info(f"Missing numerical columns in train dataset: {missing_numerical_train_columns}")
            if len(missing_numerical_test_columns)>0:
                logger.info(f"Missing numerical columns in test dataset: {missing_numerical_test_columns}")
            logger.info(f"Validation status of numberical of columns : {numerical_column_present}")
        except Exception as e:
            raise e

    def validate_min_max_value(self):
        try:
            min_columns = self.schema["min_of_column"]
            max_columns = self.schema["max_of_column"]
            min_max_status= True
            col = ['SEX','EDUCATION','MARRIAGE']
            for i in col:
                if self.train[i].min() != min_columns[i] or self.test[i].min() != min_columns[i]:
                    min_max_status= False
                    logger.info(f"Min value of {i} column is not valid")
                if self.train[i].max() != max_columns[i] and self.test[i].max() != max_columns[i]:
                    min_max_status= False
                    logger.info(f"Max value of {i} column is not validated")
            logger.info(f"Validation status of Min and Max values of {col} columns : {min_max_status}")
        except Exception as e:
            raise e

    def data_drift_report_json(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])           

            profile.calculate(self.train,self.test)

            report =json.loads(profile.json())
            report_file_path = os.path.join(self.config.report_dir,self.config.report_file_name)
           
            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=4)
            logger.info(f"Data drift report in .json format added.")
        except Exception as e:
            raise e

    def data_drift_report_html_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])            
            dashboard.calculate(self.train,self.test)
            report_page_file_path = os.path.join(self.config.report_dir,self.config.report_page_file_name)
            dashboard.save(report_page_file_path)
            logger.info(f"Data drift dashboard report in .html format added.")
        except Exception as e:
            raise e