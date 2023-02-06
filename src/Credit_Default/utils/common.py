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