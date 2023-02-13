
from flask import Flask,render_template
import pickle

from app_utils import *

app = Flask(__name__)
model = pickle.load(open('pipe_model.pkl', 'rb'))

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
        
        prediction = model.predict(inputs)
        
        output = round(prediction[0], 2)        
        value = inputs.values.tolist()
        
        value=readable_user_value(value) 
        return render_template('results.html', prediction_text=output,values=value)

    except Exception as e:
        raise e

if __name__ == "__main__":
    app.run(debug=True)