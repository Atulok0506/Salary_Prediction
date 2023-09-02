<font color="red">Salary Prediction Machine Learning Model</font>

![Salary Prediction](https://github.com/Atulok0506/Salary_Prediction/blob/main/Screenshot_Model.png)

![Programming Language](https://img.shields.io/badge/Python-3.10-orange)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![DATA](https://img.shields.io/badge/Ambitionbox-fcba03)
![Deploy](https://img.shields.io/badge/AWS-fcba03)

## Overview

Welcome to the Salary Prediction Machine Learning Model project! This project is a part of my journey in learning Data Science and delving into Machine Learning and AI. In this project, we have developed a salary prediction model using data scraped from Ambition Box. The model has achieved an impressive accuracy rate of 82%, and this README will guide you through the project's details and how to use it.

## Table of Contents

- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Model Performance](#model-performance)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About the Project

In today's competitive job market, knowing what salary to expect is crucial. This project aims to predict salaries based on various factors such as job title, location, company ratings, and more. The model was built using popular Python libraries and machine learning techniques.

## Dataset

We collected our data from Ambition Box, a valuable source for company information. The dataset contains various features related to job postings, companies, and salaries. We used this data to train and evaluate our salary prediction model.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11
- Jupyter Notebook (for running the code)
- Required Python libraries (NumPy, Pandas, Scikit-Learn, Matplotlib, etc.)

## Getting Started

1. Clone this repository to your local machine: git clone `https://github.com/Atulok0506/Salary_Prediction.git`
2. Install the required Python libraries by running `pip install -r requirements.txt`.
3. Open the Jupyter Notebook `salary_prediction_model.ipynb`.
4. Run the Application: `python main.py`
5.  Access the Application: `http://localhost:5000`

## Model Performance

Our salary prediction model achieved an accuracy rate of 82%. This is a remarkable result and can be a valuable tool for job seekers, HR professionals, and businesses.

## Usage

To use the model for salary predictions, follow these steps:

1. Input Data:

Provide the necessary input features such as years of experience, min salary, maximum salary, job_profile and company in the provided input fields.

2. Predict Salary:

Click the "Predict" button to generate a salary prediction based on the input data.

3. View Result:

The predicted salary will be displayed on the screen.

Here's a Python code snippet to get you started:

```python
import joblib

# Load the trained model
model = joblib.load("random_forest_model_scaled.pkl")

# Prepare input data for prediction
input_data = {
    "min_salary": "5.8",
    "max_salary": "11.5",
    "Avg Experience": 3.9,
    "company": tcs
    "job": System Engineer
}

# Make a salary prediction
predicted_salary = model.predict(input_data)

print(f"Predicted Salary: ${predicted_salary:.2f}")
```

## Contributing

We welcome contributions from the community. Feel free to open issues, submit pull requests, or provide feedback to help us improve this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please feel free to contact me:

- Name: Atul Kishore
- Email: atulstar900@gmail.com
- LinkedIn: [Atul Kishore on LinkedIn](https://www.linkedin.com/in/atul-kishore-b16991179/)

Thank you for being a part of this exciting project! Happy predicting! 🚀
