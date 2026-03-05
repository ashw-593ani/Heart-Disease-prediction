# Heart Disease Prediction

### Project Overview
This project predicts heart disease risk using a Machine Learning model. It uses users' medical and health-related information such as age, sex, chest pain type, blood pressure, cholesterol level, and other clinical parameters to determine whether a person is at risk of heart disease.


This project helps in early detection and risk analysis using trained ML models.**Live Demo:** [Heart Disease Prediction App](https://heart-disease-prediction-x1sh.onrender.com)

---

### Features
- Predict heart disease risk (High / Low)

1.Input features:
2.Age – Patient's age
3.Sex – Male/Female
4.Chest Pain Type – Type of chest pain
5.Resting Blood Pressure – Blood pressure level
6.Cholesterol – Serum cholesterol level
7.Fasting Blood Sugar – Blood sugar level
8.Rest ECG – Electrocardiographic results
9.Max Heart Rate – Maximum heart rate achieved
10.Exercise Induced Angina – Yes/No
11.Oldpeak – ST depression induced by exercise
12.Slope – Slope of peak exercise ST segment
13.CA – Number of major vessels
14.Thal – Thalassemia type
Provides accurate predictions using a trained ML modeltrained ML model

---
### Technology Used


1. Python
2. Flask
3. HTML
4. CSS
5. Flask
6. Scikit-learn
7. Pandas
8. NumPy
9. Gunicorn
10.Render


### Installation
1. Clone the repository:
  git clone <repo-url>
  cd <repository-folder>

2. Create and activate a virtual environment:
  python -m venv myenv
  myenv\Scripts\activate       # Windows

3. Install required packages:
  pip install -r requirements.txt


### Usage

1. Run the application locally:
   python app.py

2. Provide input values through the interface

3. The system will predict whether the person is at risk of heart disease or not as output.

### Dataset
Dataset is available in CSV format.
Features include: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target


### Model


Model: Logistic Regression 

Evaluated using Train/Test split

Metrics: Accuracy, Precision, Recall, F1-Score

