# ❤️ Heart Disease Prediction

A beginner-level **Machine Learning practice project** built to understand the fundamentals of machine learning, data preprocessing, feature engineering, model scaling, prediction, and deployment using **Streamlit**.

The project uses a **Logistic Regression** model to predict the risk of heart disease based on selected health-related parameters.

## 🚀 Live Demo

🔗 **Streamlit App:** [https://mllearning-njkbwjfgat5ts9nzgfq9qt.streamlit.app/]

> **Note:** This application is created for educational purposes and is not intended for medical diagnosis or professional medical decision-making.

---

## 📌 About the Project

This project was created as part of my journey of learning and practicing **Machine Learning concepts with Python**.

The main goal was not to build a production-level medical system, but to understand the complete basic ML workflow:

```text
Data
 ↓
Preprocessing
 ↓
Feature Encoding
 ↓
Feature Scaling
 ↓
Logistic Regression
 ↓
Prediction
 ↓
Streamlit Web App
 ↓
Deployment
```

---

## ✨ Features

* Interactive Streamlit interface
* User-friendly input fields
* Multiple health-related input parameters
* Categorical feature encoding
* Feature scaling
* Logistic Regression prediction
* Saved ML model using Joblib
* Live deployment using Streamlit Community Cloud

---

## 🧠 Machine Learning Model

The project uses **Logistic Regression** for binary classification.

The model predicts one of two outcomes:

* **0 → Low Risk of Heart Disease**
* **1 → High Risk of Heart Disease**

The trained model, scaler, and expected feature columns are stored as `.pkl` files and loaded by the Streamlit application.

---

## 📊 Input Features

The application takes the following inputs:

| Feature                 | Description                                    |
| ----------------------- | ---------------------------------------------- |
| Age                     | Age of the person                              |
| Gender                  | Gender                                         |
| Chest Pain Type         | Type of chest pain                             |
| Resting Blood Pressure  | Resting blood pressure in mm Hg                |
| Cholesterol             | Cholesterol level in mg/dl                     |
| Fasting Blood Sugar     | Whether fasting blood sugar is above 120 mg/dl |
| Resting ECG             | Resting electrocardiogram result               |
| Maximum Heart Rate      | Maximum heart rate achieved                    |
| Exercise-Induced Angina | Whether exercise causes angina                 |
| OldPeak                 | ST depression value                            |
| ST Slope                | Slope of the ST segment                        |

---

## 🛠️ Technologies Used

### Programming Language

* **Python**

### Libraries

* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **Scikit-learn** – machine learning
* **Joblib** – saving and loading trained models
* **Streamlit** – web application and deployment

---

## 📂 Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py
├── Logistic_heart.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                 | Purpose                           |
| -------------------- | --------------------------------- |
| `app.py`             | Streamlit application             |
| `Logistic_heart.pkl` | Trained Logistic Regression model |
| `scaler.pkl`         | Feature scaling object            |
| `columns.pkl`        | Expected feature columns          |
| `requirements.txt`   | Required Python dependencies      |
| `README.md`          | Project documentation             |

---

## 🔄 How the Application Works

### 1. User Input

The user provides health-related information through the Streamlit interface.

### 2. Feature Preparation

Categorical inputs such as:

* Gender
* Chest Pain Type
* Resting ECG
* Exercise-Induced Angina
* ST Slope

are converted into numerical features.

### 3. Feature Alignment

The application ensures that the input contains the same expected columns used during model training.

### 4. Feature Scaling

The input data is transformed using the saved scaler:

```python
scaled_input = scaler.transform(input_df)
```

### 5. Prediction

The trained Logistic Regression model generates the prediction:

```python
prediction = model.predict(scaled_input)[0]
```

### 6. Result

The application displays either:

```text
High Risk of Heart Disease
```

or

```text
Low Risk of Heart Disease
```

---

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Jagriti-student/ML_Learning.git
```

### 2. Navigate to the project

```bash
cd ML_Learning/Heart_Disease_Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project uses the following dependencies:

```text
streamlit
pandas
numpy
scikit-learn==1.6.1
joblib
```

---

## 🎯 Learning Outcomes

Through this project, I practiced:

* Understanding a basic classification problem
* Preparing input features for an ML model
* Handling categorical variables
* Feature scaling
* Using Logistic Regression
* Loading trained models with Joblib
* Connecting an ML model to a Streamlit interface
* Deploying a machine learning application
* Understanding the basic end-to-end ML workflow

---

## 🔮 Future Improvements

Possible improvements for this project include:

* Adding model performance metrics
* Adding confusion matrix and classification report
* Improving the UI/UX
* Adding data visualizations
* Comparing multiple classification algorithms
* Adding model accuracy information
* Improving input validation
* Adding more detailed educational explanations of the prediction process

---

## ⚠️ Disclaimer

This project is intended **only for educational and machine learning practice purposes**.

The predictions generated by this application are **not medical advice, diagnosis, or a substitute for consultation with a qualified healthcare professional**.

---

## 👩‍💻 Author

**Jagriti**

B.Tech CSE Student | GJUST

🔗 **GitHub:** https://github.com/Jagriti-student

---

⭐ If you find this project useful for learning, feel free to explore the repository and experiment with the code.
