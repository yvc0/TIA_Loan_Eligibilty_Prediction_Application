# 🏦 Bank Loan Eligibility Prediction App

This is a **Streamlit web application** that predicts whether a bank loan applicant is eligible for a loan based on their profile.

---

## 📌 Features
- Input applicant details (age, income, employment type, credit score, dependents, etc.).
- Rule-based eligibility calculation (can be extended to ML model).
- Displays **prediction result**: Eligible ✅, Borderline ⚠️, or Not Eligible 🚫.
- Provides **loan improvement suggestions**.

---

## 📂 Project Structure
```
bank-loan-eligibility-app/
├── loan_app.py        # Main Streamlit app
├── requirements.txt   # Dependencies file
└── README.md          # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository** (or copy files locally)
   ```bash
   git clone https://github.com/your-username/bank-loan-eligibility-app.git
   cd bank-loan-eligibility-app
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App

Run the Streamlit app using:
```bash
streamlit run loan_app.py
```

The app will start locally at:
```
http://localhost:8501
```

---

## 🛠️ Requirements (requirements.txt)
```
streamlit
numpy
pandas
Pillow
```

---

## 📊 Example Inputs
- **Age:** 30  
- **Employment:** Salaried  
- **Monthly Income:** ₹30,000  
- **Loan Amount:** ₹200,000  
- **Credit Score:** 700  
- **Loan Term:** 36 months  
- **Dependents:** 0  

---

## ✅ Prediction Output
- **Eligible for Loan**: When applicant has stable income, good credit score, and loan affordability.  
- **Borderline Eligible**: Medium risk, may need improvements.  
- **Not Eligible**: High risk, needs better credit score or higher income.  

---

## ⚠️ Disclaimer
This app is for **educational/demo purposes only** and does not replace real financial eligibility checks.
