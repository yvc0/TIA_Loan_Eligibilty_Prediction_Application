import streamlit as st

st.set_page_config(page_title="Bank Loan Eligibility App", page_icon="🏦")

# -----------------------------
# Title
# -----------------------------
st.title("🏦 Bank Loan Eligibility Prediction")
st.write("Fill in your details to check whether you are eligible for a loan.")

# -----------------------------
# Input Fields
# -----------------------------
age = st.number_input("Applicant Age", min_value=18, max_value=70, value=30, step=1)

employment = st.selectbox("Employment Type", ["Salaried", "Self-Employed", "Unemployed"])
income = st.number_input("Monthly Income (₹)", min_value=0, step=1000, value=30000)
loan_amount = st.number_input("Requested Loan Amount (₹)", min_value=10000, step=5000, value=200000)

loan_term = st.selectbox("Loan Term", ["12 months", "24 months", "36 months", "60 months"])
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=700)
existing_loans = st.number_input("Number of Existing Loans", min_value=0, max_value=10, value=0)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0)
location = st.selectbox("Location", ["Hyderabad", "Bangalore", "Mumbai", "Chennai", "Delhi"])

# -----------------------------
# Eligibility Logic (Rule-based)
# -----------------------------
eligibility_score = 0

# Age condition
if 21 <= age <= 60:
    eligibility_score += 2

# Employment & Income
if employment == "Salaried" and income > 25000:
    eligibility_score += 3
elif employment == "Self-Employed" and income > 30000:
    eligibility_score += 2
elif employment == "Unemployed":
    eligibility_score -= 2

# Credit Score
if credit_score >= 750:
    eligibility_score += 3
elif credit_score >= 650:
    eligibility_score += 2
else:
    eligibility_score -= 1

# Loan vs Income check
if loan_amount < (income * 20):  # simple affordability check
    eligibility_score += 2
else:
    eligibility_score -= 1

# Loan Term
if loan_term in ["36 months", "60 months"]:
    eligibility_score += 1

# Existing Loans
if existing_loans == 0:
    eligibility_score += 1
elif existing_loans > 3:
    eligibility_score -= 2

# Dependents
if dependents > 3:
    eligibility_score -= 1

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔍 Check Eligibility"):
    st.subheader("Prediction Result")

    if eligibility_score >= 6:
        st.success("✅ Eligible for Loan")
        st.write("👉 Suggestion: You meet the bank’s criteria. You can proceed with the loan application.")
    elif 3 <= eligibility_score < 6:
        st.warning("⚠️ Borderline Eligible")
        st.write("👉 Suggestion: Try reducing the loan amount or improving credit score for higher approval chances.")
    else:
        st.error("🚫 Not Eligible for Loan")
        st.write("👉 Suggestion: Improve credit score, increase income, or clear existing loans before applying.")

    st.info(f"Your Eligibility Score: **{eligibility_score}**")
