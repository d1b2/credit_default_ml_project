import time
from flask import Flask,render_template
import pickle

from app_utils import *

csv_path='app/database.csv'
if not os.path.exists(csv_path):
    create_records_header(csv_path)
app = Flask(__name__)
model = pickle.load(open('artifacts/model_tuning/pipe_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    try:
        inputs=get_user_input_dataframe()        
        start = time.time()
        prediction = model.predict(inputs)
        end = time.time()
        eval_time = round(end-start,4) # in seconds
        
        
        output = round(prediction[0], 2)        
        value = inputs.values.tolist()
        
        value=readable_user_value(value) 
        value1=value[0]
        #dataframe=create_record_rows(csv_path,value1,output,eval_time)       
        create_record_rows(csv_path,value1,output,eval_time) 
        create_records_html(csv_path,"app/templates/records.html")
        #value2=dataframe
        return render_template('results.html', prediction_text=output,values=value,response_time=eval_time)

    except Exception as e:
        raise e
    
@app.route('/record')
def record():
    try:      
        return render_template("records.html")      

    except Exception as e:
        raise e

if __name__ == "__main__":
    app.run(debug=True)