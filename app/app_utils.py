import pandas as pd
from flask import  request

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
        elif value[0][2]=='1':value[0][2]='University'
        elif value[0][2]=='1':value[0][2]='High School'
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