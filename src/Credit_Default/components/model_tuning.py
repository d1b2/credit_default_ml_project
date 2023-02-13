import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer,make_column_transformer
from sklearn.pipeline import Pipeline,make_pipeline
from Credit_Default.entity import *
from Credit_Default.constants import *
from Credit_Default.utils import *
import pickle

class ModelTuning:
    def __init__(self, config: ModelTuningConfig):
        self.config = config
        self.train_array = np.load(TRAIN_ARRAY_FILE_PATH)
        self.test_array = np.load(TEST_ARRAY_FILE_PATH)
        self.model_list = pd.read_csv(MODEL_LIST_FILE_PATH)


    def best_model_csv(self):
        try:
            best_model=self.model_list[self.model_list.Accucracy_score == self.model_list.Accucracy_score.max()].Model.values[0]
            logger.info(f"Best Model among model csv : {best_model}")
        except Exception as e:
            raise e

    def model_tuning_and_saving_parameters(self):
        try:
            rfc = RandomForestClassifier()
            parameters = {
                        "n_estimators":[5,10,50,100,120],
                        "max_depth":[2,4,8,16,18],
                        "criterion":['gini','entropy']}
            x_train,y_train = self.train_array[:,:-1],self.train_array[:,-1]
            CV_rfc = GridSearchCV(estimator=rfc, param_grid=parameters, cv= 5)
            CV_rfc.fit(x_train, y_train)
            
            write_yaml(PARAMS_FILE_PATH ,CV_rfc.best_params_)
        except Exception as e:
            raise e
    

    def saving_model_scores(self):
        try:
            param=read_yaml(PARAMS_FILE_PATH)
            model=RandomForestClassifier(criterion=param['criterion'],
                                        max_depth=param['max_depth'],
                                        n_estimators=param['n_estimators'])
                                        
            score=model_score(self.train_array,self.test_array,model)
            
            dict1={'Model' : 'Random_Forest_Classifier',
            'Accucracy_score' : score[0],
            'ROC_AUC_Score' : score[1],
            'MSE': score[-1]} 

            model_score_file_path = os.path.join(self.config.root_dir,self.config.model_scores)
           
            with open(model_score_file_path,"w") as report_file:
                json.dump(dict1, report_file, indent=4)
            logger.info(f"Tuned Model score in .json format added.")
        except Exception as e:
            raise e
    
    def saving_model(self):
        try:
            x_train,y_train = self.train_array[:,:-1],self.train_array[:,-1]
            param=read_yaml(PARAMS_FILE_PATH)
            model=RandomForestClassifier(criterion=param['criterion'],
                                        max_depth=param['max_depth'],
                                        n_estimators=param['n_estimators'])
            model.fit(x_train,y_train)            
            model_filepath = os.path.join(self.config.root_dir,self.config.model_name)
            pickle.dump(model, open(model_filepath, 'wb'))
            logger.info(f"Tuned Model pickle file saved.")
        
        except Exception as e:
            raise e
    
    def saving_model_pipeline(self):
        try:
            clean_schema=read_yaml(SCHEMA_CLEAN_FILE_PATH)
            num_features = list(clean_schema["numerical_features"].split(" "))
            cat_features = list(clean_schema["categorical_features"].split(" "))
            preprocessing=column_transformer(cat_features,num_features)
            train_csv=pd.read_csv(Path('artifacts/data_preparation/clean_data/train.csv'))
            x_train,y_train=train_csv.iloc[:,:-1],train_csv['DEFAULTER']
            #param=read_yaml(PARAMS_FILE_PATH)
            model=pickle.load(open('artifacts/model_tuning/model.pkl', 'rb'))
            #model=RandomForestClassifier(criterion=param['criterion'],
                                            #max_depth=param['max_depth'],
                                            #n_estimators=param['n_estimators'])
            pipeline_rf = Pipeline(steps=[('preprocessor',preprocessing),
                                        ('Random_forest_classifier',model)])
            pipeline_rf.fit(x_train,y_train)
            pickle.dump(pipeline_rf, open('artifacts/model_tuning/pipe_model.pkl', 'wb'))
       
        except Exception as e:
            raise e