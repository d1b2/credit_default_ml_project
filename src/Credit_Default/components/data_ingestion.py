import os
from Credit_Default.entity import DataIngestionConfig
from Credit_Default.utils import *
from pathlib import Path
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def load_kaggle(self) :
        kaggle=load_json(Path(self.config.kaggle_file_path))
        os.environ['KAGGLE_USERNAME']=kaggle.username
        os.environ['KAGGLE_KEY']=kaggle.key
        url=self.config.source_URL.split('/')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_file("/".join(url[-3:-1]),url[-1],self.config.raw_data_dir)

    def unzip(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            zf.extractall(self.config.unzip_dir)
    
    def basic(self):
        file_name = os.listdir(self.config.unzip_dir)[0]
        df_file_path = os.path.join(self.config.unzip_dir,file_name)
        df=pd.read_csv(df_file_path)
        max1=df['LIMIT_BAL'].max()
        df['Limit_Bal_cat']=pd.cut(
                df["LIMIT_BAL"],
                bins=[0, 0.2*max1, 0.4*max1, 0.6*max1, max1],
                labels=[1,2,3,4]
            )

        strat_train_set = None
        strat_test_set = None

        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
        for train_index,test_index in split.split(df,df['Limit_Bal_cat']):
            strat_train_set = df.loc[train_index].drop(['Limit_Bal_cat'],axis=1)
            strat_test_set= df.loc[test_index].drop(['Limit_Bal_cat'],axis=1)

        if strat_train_set is not None:
            train_file_path = os.path.join(self.config.ingested_train_dir,"train.csv")
            strat_train_set.to_csv(train_file_path,index=False)
        if strat_test_set is not None:
            test_file_path = os.path.join(self.config.ingested_test_dir,"test.csv")
            strat_test_set.to_csv(test_file_path,index=False)
