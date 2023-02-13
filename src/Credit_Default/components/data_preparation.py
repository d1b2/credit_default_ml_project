import os

from pathlib import Path
import pandas as pd
import numpy as np
from Credit_Default import logger
from Credit_Default.entity import *
from Credit_Default.constants import *
from Credit_Default.utils import *
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import pickle


class DataPreparation:
    def __init__(self, config: DataPreparationConfig):
        self.config = config
        self.train = pd.read_csv(TRAIN_FILE_PATH)
        self.test = pd.read_csv(TEST_FILE_PATH)
        self.clean_schema = read_yaml(SCHEMA_CLEAN_FILE_PATH)
        
    def null_checks(self):
        try:
            null_status = True
            if self.train.isnull().sum().sum()==0 and self.train.isnull().sum().sum()==0:
                null_status=False
            logger.info(f"Null values present in train and test dataset : {null_status}")
        except Exception as e:
            raise e
    def clean_education(self):
        try:           
            self.train.loc[(self.train['EDUCATION'] == 5) | (self.train['EDUCATION'] == 6) | (self.train['EDUCATION'] == 0), 'EDUCATION'] = 4
            self.test.loc[(self.test['EDUCATION'] == 5) | (self.test['EDUCATION'] == 6) | (self.test['EDUCATION'] == 0), 'EDUCATION'] = 4
            logger.info(f"EDUCATION column cleaned in train and test dataset.")
        except Exception as e:
            raise e

    def clean_marriage(self):
        try:
            self.train.loc[(self.train['MARRIAGE'] == 0), 'MARRIAGE'] = 3
            self.test.loc[(self.test['MARRIAGE'] == 0), 'MARRIAGE'] = 3
            logger.info(f"MARRIAGE column cleaned in train and test dataset.")
        except Exception as e:
            raise e
    def clean_repayment_status(self):
        try:
            for i in range(6,12):
                self.train.iloc[(self.train.iloc[:,i] == 0) | (self.train.iloc[:,i] == -2), i] = -1
                self.test.iloc[(self.test.iloc[:,i] == 0) | (self.test.iloc[:,i] == -2), i] = -1
            logger.info(f"Repayment Status columns cleaned in train and test dataset.")

        except Exception as e:
            raise e

    def rename_target(self):
        try:
            self.train.rename(columns={'default.payment.next.month':'DEFAULTER'},inplace=True)
            self.test.rename(columns={'default.payment.next.month':'DEFAULTER'},inplace=True)
            logger.info(f"Target column renamed to DEFAULTER in train and test dataset.")
        except Exception as e:
            raise e
    
    def delete_columns(self):
        try:
            self.train.drop(['ID','AGE'], axis=1,inplace=True)
            self.test.drop(['ID','AGE'], axis=1,inplace=True)
            logger.info(f'ID and AGE column deleted from train and test dataset.')
        except Exception as e:
            raise e

    def smote_resampling(self):
        try:
            smote = SMOTE()
            train_df,test_df=self.train,self.test            
            x_train_smote, y_train_smote = smote.fit_resample(train_df.iloc[:,0:-1], train_df['DEFAULTER'])
            x_test_smote, y_test_smote = smote.fit_resample(test_df.iloc[:,0:-1], test_df['DEFAULTER'])

            logger.info(f'Original Train dataset shape: {len(train_df)}|Resampled Train dataset shape :{len(y_train_smote)}')
           
            logger.info(f'Original Test dataset shape: {len(test_df)}|Resampled Test dataset shape :{len(y_test_smote)}')
            columns = list(train_df.columns)
            columns.pop()

            self.train = pd.DataFrame(x_train_smote, columns=columns)
            self.train['DEFAULTER'] = y_train_smote
            self.test = pd.DataFrame(x_test_smote, columns=columns)
            self.test['DEFAULTER'] = y_test_smote
         
        except Exception as e:
            raise e
    
    def drop_duplicates(self):
        try: 
            train_duplicate = self.train[self.train.duplicated()]
            test_duplicate = self.test[self.test.duplicated()]
            if len(train_duplicate)> 0 :
                logger.info(f'{len(train_duplicate)} duplicate deleted from train dataset.')
                self.train.drop_duplicates(inplace=True)
            if len(test_duplicate)>0:
                logger.info(f'{len(test_duplicate)} duplicate deleted from test dataset.')
                self.test.drop_duplicates(inplace=True)
        except Exception as e:
            raise e
        

    def saving_resampled_and_clean_csv(self):
        try:
            train_file_path = os.path.join(self.config.clean_csv_dir,"train.csv")
            test_file_path = os.path.join(self.config.clean_csv_dir,"test.csv")
            self.train.to_csv(train_file_path,index=False)
            self.test.to_csv(test_file_path,index=False)
            logger.info(f'Saving clean train: {len(self.train)} rows and test: {len(self.test)} rows in csv files')
            pass
        except Exception as e:
            raise e
    
    def saving_column_transformer(self):
        try:
            num_features = list(self.clean_schema["numerical_features"].split(" "))
            cat_features = list(self.clean_schema["categorical_features"].split(" "))
            target_column = self.clean_schema["target_column"] 
            preprocessing= column_transformer(cat_features,num_features)           
            x_train= self.train.drop(target_column,axis=1)
            preprocessing.fit(x_train)
            transformer=os.path.join(self.config.root_dir,"transformer.pkl")
            pickle.dump(preprocessing, open(transformer, 'wb'))
            logger.info(f'Saving column transformer')
        except Exception as e:
                raise e


    def saving_clean_np_array(self):
        try:
            num_features = list(self.clean_schema["numerical_features"].split(" "))
            cat_features = list(self.clean_schema["categorical_features"].split(" "))
            target_column = self.clean_schema["target_column"] 
            preprocessing= column_transformer(cat_features,num_features)
            x_train,x_test = self.train.drop(target_column,axis=1),self.test.drop(target_column,axis=1)
            y_train,y_test = self.train[target_column],self.test[target_column]
            x_train_arr=preprocessing.fit_transform(x_train)
            logger.info(f'Fit_transform x_train')
            x_test_arr = preprocessing.transform(x_test)
            logger.info(f'Transform x_test')
            y_train_arr= np.array(y_train)
            y_test_arr= np.array(y_test)
            train_arr= np.column_stack([x_train_arr, y_train_arr])
            test_arr= np.column_stack([x_test_arr, y_test_arr])
            train_arr_filepath=os.path.join(self.config.clean_np_dir, "train_array.npy")
            test_arr_filepath=os.path.join(self.config.clean_np_dir, "test_array.npy")
            np.save(train_arr_filepath,train_arr)
            np.save(test_arr_filepath,test_arr)
            logger.info(f'Saving clean train and test numpy arrays')
        except Exception as e:
                raise e