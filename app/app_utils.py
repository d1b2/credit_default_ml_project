import pandas as pd
from flask import  request
import os
import csv
import datetime

def create_records_header(csv_path): 
    """ Creates csv file with headers
    Args:
        csv_path (str): path of csv file
    """   
    try:
        columns=['Timestamp','Response_Time','Credit_Given','Gender','EDUCATION','MARRIAGE',
                                'PAY_0', 'PAY_2','PAY_3','PAY_4','PAY_5','PAY_6',
                                'BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6',
                                'PAY_AMT1','PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6','Prediction']
        
        with open(csv_path, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                
            # writing the fields 
            csvwriter.writerow(columns)
    except Exception as e:
        raise e

def create_record_rows(csv_path,value1,output,eval_time):
    """Adds rows to csv file stored at csv_path

    Args:
        csv_path (str):   path of csv file
        value1 (list):     input values of user
        output (float):   model prediction  of user input 
        eval_time (time): model prediction time
    """
    try:
        if output==1:output_text='Default'
        else:output_text='Not Default'
        value1=[datetime.datetime.now()]+[eval_time]+value1+[output_text]
        
        
        with open(csv_path, 'a') as csvfile: 
                # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                    
                # writing the fields 
            csvwriter.writerow(value1)
        return pd.read_csv(csv_path)
    except Exception as e:
        raise e
    

def create_records_html(csv_path,html_path):
    """creates html from csv file

    Args:
        csv_path (str): path of csv file
        html_path (str): path of html
    """
    try:
        record=pd.read_csv(csv_path)    
        df_html_styled = record.style.set_properties(
                **{"text-align": "left","border":"1px",
                'border-color':'blue',
                'border-width':'1px',
                'border-style':'solid',
                'padding-left': '20px',
                'padding-right': '10px',
                'padding-top': '2px',
                'padding-bottom': '2px'}
                ).hide(axis="index").set_caption('User Data Record')
        df_html_styled.to_html(html_path)
        #pd.read_csv(csv_path).to_html(html_path)
    except Exception as e:
        raise e

    


def get_user_input_dataframe():
    """Gets user inputs and convert it into dataframe

    Returns:
        user_inputs(panadas dataframe): converted dataframe
    """
    try:
        LIMIT_BAL = request.form.get('LIMIT_BAL')    
        SEX = request.form.get('SEX')
        EDUCATION=request.form.get('EDUCATION')
        MARRIAGE =request.form.get('MARRIAGE')
        PAY_0 =request.form.get('PAY_0')
        PAY_2=request.form.get('PAY_2')
        PAY_3=request.form.get('PAY_3')
        PAY_4 =request.form.get('PAY_4')
        PAY_5 =request.form.get('PAY_5')
        PAY_6 =request.form.get('PAY_6')
        BILL_AMT1 =request.form.get('BILL_AMT1')
        BILL_AMT2 =request.form.get('BILL_AMT2')
        BILL_AMT3 =request.form.get('BILL_AMT3')
        BILL_AMT4 =request.form.get('BILL_AMT4')
        BILL_AMT5 =request.form.get('BILL_AMT5')
        BILL_AMT6 =request.form.get('BILL_AMT6')
        PAY_AMT1 = request.form.get('PAY_AMT1')
        PAY_AMT2 = request.form.get('PAY_AMT2')
        PAY_AMT3 = request.form.get('PAY_AMT3')
        PAY_AMT4 = request.form.get('PAY_AMT4')
        PAY_AMT5 = request.form.get('PAY_AMT5')
        PAY_AMT6 = request.form.get('PAY_AMT6')

        user_inputs = pd.DataFrame([[LIMIT_BAL,SEX,EDUCATION,MARRIAGE,
                                PAY_0, PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,
                                BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,
                                PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6
                            ]], 
                    columns=['LIMIT_BAL','SEX','EDUCATION','MARRIAGE',
                            'PAY_0', 'PAY_2','PAY_3','PAY_4','PAY_5','PAY_6',
                            'BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6',
                            'PAY_AMT1','PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'])
        return user_inputs
        
    except Exception as e:
        raise e

def readable_user_value(value):
    """"
    Convert categorical values entered by user in readable text

    Args:
        value (list): user inputs in numbers


    Returns:
        value (list): readable user inputs
    """
    try:
        if value[0][1]=='1':value[0][1]='Male'
        else:value[0][1]='Female'
        if  value[0][2]=='1':value[0][2]='Graduate School'
        elif value[0][2]=='2':value[0][2]='University'
        elif value[0][2]=='3':value[0][2]='High School'
        else: value[0][2]='Others'
        if  value[0][3]=='1':value[0][3]='Married'
        elif value[0][3]=='2':value[0][3]='Single'
        else: value[0][3]='Others'

        for i in range(4,10):
            if value[0][i]=="-1":value[0][i]='Duly Paid'
            elif   value[0][i]=="1":value[0][i]="One month delay"
            elif  value[0][i]=="2":value[0][i]="Two months delay"
            elif  value[0][i]=="3":value[0][i]="Three months delay"
            elif  value[0][i]=="4":value[0][i]="Four months delay"
            elif  value[0][i]=="5":value[0][i]="Five month delay"
            elif  value[0][i]=="6":value[0][i]="Six months delay"
            elif  value[0][i]=="7":value[0][i]="Seven month delay"
            else :  value[0][i]="Eight months delay"

        return value

    except Exception as e:
        raise e