# Machine Learning Project


### Dataset : &nbsp; <a href="https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>

## Libraries / Languages
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/-Python-gold?style=for-the-badge&logo=python&logoColor=black" alt= "python"></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/-pandas-130654?style=for-the-badge&logo=pandas&logoColor=white" alt= "pandas"></a>
  <a href="https://numpy.org/"><img src="https://img.shields.io/badge/-NumPy-4DABCF?style=for-the-badge&logo=numpy&logoColor=white" alt= "numPy"></a>
  <a href="https://scikit-learn.org/stable/"><img src="https://img.shields.io/badge/-scikitlearn-FF9C34?style=for-the-badge&logo=scikitlearn&logoColor=white" alt= "sklearn"></a>
  <a href="https://flask.palletsprojects.com/en/2.2.x/"><img src="https://img.shields.io/badge/-Flask-lightgrey?style=for-the-badge&logo=flask&logoColor=black" alt= "flask"></a>
<a href="https://dvc.org/doc"><img src="https://img.shields.io/badge/-DVC-E65933?style=for-the-badge&logo=dvc&logoColor=2CB6CD" alt= "dvc"></a>
<a href="https://www.evidentlyai.com/"><img src="https://img.shields.io/badge/-evidently-green?style=for-the-badge&evidently=dvc&logoColor=white" alt= "evidently"></a>
<a href="https://mlflow.org/">  <img src="https://img.shields.io/badge/-mlflow-1767BB?style=for-the-badge&logo=mlflow&logoColor=white" alt= "mlflow"></a>

## Problem Statement
Financial threats are displaying a trend about the credit risk of commercial banks as the incredible improvement in the financial industry has arisen. In this way, one of the biggest threats faces by commercial banks is the risk prediction of credit clients. The goal is to predict the probability of credit default based on credit card owner's characteristics and payment history.
## Approach
Created a 5 step pipeline.
1. Data Ingestion : Data is gathered from kaggle url using api.It is then unzipped and splitted in test and train.
2. Data Validation : Both test and train datasets are validated with schema file.
3. Data Preparation : Data is cleaned resampled and transformed.
4. Model Training : Models are trained and their parameters and metrics are saved.
5. Model Tuning :  Selected model is tuned further to obtain final model. This model is used in flask application
## Stage Codeflow
<img src="https://github.com/d1b2/credit_default_ml_project/blob/main/app/static/satges_codeflow.png">

## Result
Build a flask based application solution which is able to predict whether customer defaults or not  based on credit card owner’s characteristics and payment history.
## Flask application demo

<img src="app/static/app_demo.gif" width="500" height="300"> 




## 💻 Setup
Create new environment &emsp;```conda create -n env python=3.8```
</br>Activating environment &emsp; &nbsp;```conda activate env```
</br>Deactivating environment  &ensp;```conda deactivate```
</br>Installing Requirements &emsp; &nbsp;```pip install requirements.txt```
</br>Running app to local server  ```python app.py```

## Software and Account Requirement


1. [Github Account](https://github.com/) 
2. [VS Code IDE](https://code.visualstudio.com/Download)
3. [Gitcli](https://git-scm.com/downloads)
4. [Kaggle Account](https://www.kaggle.com)

