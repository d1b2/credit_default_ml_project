import os
from Credit_Default import logger
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from pathlib import Path
import pandas as pd
import numpy as np
from Credit_Default.entity import *
from Credit_Default.constants import *
from Credit_Default.utils import *

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        self.train_array = np.load(TRAIN_ARRAY_FILE_PATH)
        self.test_array = np.load(TEST_ARRAY_FILE_PATH)
        self.model_name=[]
        self.accuracy_score=[]
        self.auc_score=[]
        self.mse=[]

    def logistic_regression_model(self):
        try:
            model=LogisticRegression()
            self.model_name.append('LogisticRegression')
            score=model_score(self.train_array,self.test_array,model)
            self.accuracy_score.append(score[0])
            self.auc_score.append(score[1])
            self.mse.append(score[-1])
            
        except Exception as e:
            raise e

    def knn_classifier_model(self):
        try:
            model=KNeighborsClassifier(n_neighbors=3)
            self.model_name.append('KNN_Classifier')
            score=model_score(self.train_array,self.test_array,model)
            self.accuracy_score.append(score[0])
            self.auc_score.append(score[1])
            self.mse.append(score[-1])
        except Exception as e:
            raise e
    

    def random_forest_classifier_model(self):
        try:
            model=RandomForestClassifier()
            self.model_name.append('Random_Forest_Classifier')
            score=model_score(self.train_array,self.test_array,model)
            self.accuracy_score.append(score[0])
            self.auc_score.append(score[1])
            self.mse.append(score[-1])
        except Exception as e:
            raise e
    
    def model_dataframe(self):
        try:
            models = pd.DataFrame({
                'Model' : self.model_name,    
                'Accucracy_score' : self.accuracy_score,
                'ROC_AUC_Score' : self.auc_score,
                'MSE' : self.mse})
            models['Above_Base_Accuracy']= [True if  models['Accucracy_score'][i] >= self.config.base_accuracy  else False for i in range(len(models))]
            
            model_df_filepath = os.path.join(self.config.model_df_dir,self.config.model_df_name)

            models.to_csv(model_df_filepath,index=False)
            logger.info('Dataframe of models is created')
        
        except Exception as e:
            raise e