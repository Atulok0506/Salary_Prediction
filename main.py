from flask import Flask, render_template, request, jsonify
import joblib
import json
import numpy as np
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load the pre-trained model
model_filename = 'random_forest_model_scaled.pkl'
loaded_model = joblib.load(model_filename)

# Load the MinMaxScaler used during training
scaler_filename = 'min_max_scaler.pkl'
scaler = joblib.load(scaler_filename)

# function
filename = "job_company_dict.json"
with open(filename, "r") as f:
    data = json.load(f)

def get_label(company_job):
    label = data[company_job]
    return label


@app.route('/')
def home():
    return render_template('prophecy.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input values from the HTML form
        min_salary = float(request.form['min_salary'])
        max_salary = float(request.form['max_salary'])
        avg_experience = float(request.form['avg_experience'])
        company = str(request.form['company'])
        job = str(request.form['job'])

        company_job = job+"_"+company
        company_job_label = get_label(company_job)
        # Scale the input features using the same scaler used during training
        scaled_input = scaler.transform([[min_salary, max_salary, avg_experience, company_job_label]])

        # Make the prediction using the loaded model
        prediction = loaded_model.predict(scaled_input)

        # Return the prediction to the HTML template
        return render_template('prophecy.html', prediction=prediction[0])

    except Exception as e:
        return render_template('prophecy.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
