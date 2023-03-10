import os
from box.exceptions import BoxValueError
import yaml
from Credit_Default import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.metrics import roc_auc_score,accuracy_score,mean_squared_error

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    Args:
        path (Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def column_transformer(cat_features: list,num_features: list):
    """column transformer  
    Args:
        cat_features (list): list of categorical features of dataframe
        num_features (list): list of numerical features of dataframe
        
    Returns:
        preprocessing: column transformer
    """
    preprocessing=ColumnTransformer(transformers=[
            ('tnf1',OneHotEncoder(drop='first',sparse=False, handle_unknown='ignore'), cat_features),
            ('tnf2',StandardScaler(),num_features)],
            remainder='passthrough')
    logger.info(f"Column Tranformer with OneHotEncoding on {len(cat_features)} categorical features and StandardScaler on {len(num_features)} numerical features is called.")
    return preprocessing

@ensure_annotations
def model_score(train_array,test_array,model):
    """accuracy score and auc score of model
    Args:
        train_array (numpy array) : array of training dataset
        test_array  (numpy array) : array of testing dataset
        model (sklearn model)     : machine learning model
    Returns:
        accuracy (float) : accuracy score of model
        auc (float) : roc_auc score of model
        err (float) : mean square error of model
    """
    x_train,y_train,x_test,y_test = train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1]
    model.fit(x_train,y_train)
    accuracy=round(accuracy_score(y_test, model.predict(x_test)),2)
    auc=round(roc_auc_score(y_test, model.predict_proba(x_test)[:, 1]),2)
    err=round(mean_squared_error(y_test, model.predict(x_test)),2)
    logger.info(f"Model :{str(model)} Accuracy Score :{accuracy} ROC_AUC Score :{auc} MSE :{err}")
    return accuracy,auc,err

@ensure_annotations
def write_yaml(path_to_yaml: Path,data:dict=None):
    """Write dictionary to yaml file 
    Args:
        path_to_yaml (str): path of yaml
        data (dict) : data to written in yaml file
   
    """ 
    try:         
        with open(path_to_yaml,"w") as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
        logger.info(f"yaml file: {path_to_yaml} written successfully")  
    except Exception as e:
        raise e