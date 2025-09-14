# 🩺 Diabetes Prediction App

This is a Streamlit-based web application that uses a Logistic Regression model to predict whether a patient is diabetic or not based on health-related parameters. The app provides prediction results along with model accuracy and confidence level.

---

## 📊 Features

- Accepts 8 health-related inputs from the user.
- Predicts whether the patient is **Diabetic** or **Not Diabetic**.
- Displays:
  - Model **accuracy** (trained on real data)
  - **Prediction confidence** (% likelihood of diabetes)

---

## 🧾 Input Features

1. **Pregnancies**
2. **Glucose Level**
3. **Blood Pressure**
4. **Skin Thickness**
5. **Insulin**
6. **BMI** (Body Mass Index)
7. **Diabetes Pedigree Function**
8. **Age**

---

## 📁 Project Structure

diabetes-predictor/
│
├── app.py # Streamlit app code
├── data.csv # Dataset (Pima Indians Diabetes Dataset)
└── README.md # Project instructions


---

## ⚙️ Requirements

- Python 3.7+
- Streamlit
- Scikit-learn
- Pandas
- NumPy

---

## 📦 Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
## Install the required dependencies:
```bash
pip install -r requirements.txt

## 🚀 How to Run the App 

Ensure data.csv is present in the same folder as app.py.

Launch the Streamlit app:

Open your browser and go to:
http://localhost:8501