# Credit Risk Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)

## 📌 Project Overview

This project builds an **end-to-end Credit Risk Prediction system** using Machine Learning to classify whether a loan applicant represents **GOOD** or **BAD** credit risk.

The project demonstrates the complete Data Science workflow:
- Exploratory Data Analysis (EDA)
- Data preprocessing & feature encoding
- Model training and evaluation
- Model persistence (joblib)
- Interactive deployment using Streamlit

---

## 🎯 Business Problem

Financial institutions must assess the **risk of loan default** before approving credit applications. Poor credit decisions can lead to:

- **High default losses** - Approving risky borrowers (false positives)
- **Lost revenue** - Rejecting creditworthy customers (false negatives)

This project aims to **predict credit risk accurately** using customer demographic and financial attributes, enabling better lending decisions.

---

## 📊 Dataset

- **Source:** German Credit Data
- **Size:** 1,000 records
- **Target Variable:** `Risk`
  - `1` → Good credit risk ✅
  - `0` → Bad credit risk ❌

### Key Features

| Feature | Description | Type |
|---------|-------------|------|
| Age | Applicant's age | Numerical |
| Sex | Gender (male/female) | Categorical |
| Job | Job classification (0–3) | Ordinal |
| Housing | Housing status (own/rent/free) | Categorical |
| Saving accounts | Savings category | Categorical |
| Checking account | Checking account status | Categorical |
| Credit amount | Loan amount requested | Numerical |
| Duration | Loan duration in months | Numerical |

---

## 🔍 Exploratory Data Analysis

Key steps performed in the analysis:

- **Data structure inspection** - Understanding data types and dimensions
- **Missing value analysis** - Identifying and handling null values
- **Distribution analysis** - Visualizing numerical feature distributions
- **Risk distribution** - Analyzing target class balance
- **Correlation analysis** - Identifying relationships between features

**Note:** Missing values in `Saving accounts` and `Checking account` were handled appropriately during preprocessing.

---

## ⚙️ Feature Engineering & Preprocessing

### Encoding Strategy
- Categorical variables encoded using **Label Encoding**
- Each categorical feature uses a **separate encoder** for flexibility
- All encoders are **saved as .pkl files** to ensure consistent transformations during deployment

### Encoded Features
- `Sex` → Sex_encoder.pkl
- `Housing` → Housing_encoder.pkl
- `Saving accounts` → Saving accounts_encoder.pkl
- `Checking account` → Checking account_encoder.pkl

---

## 🤖 Model Training

### Algorithm: Extra Trees Classifier

**Why Extra Trees?**
- Excellent performance on tabular data
- Reduces overfitting through ensemble learning
- No feature scaling required
- Fast training and inference
- Handles non-linear relationships well

### Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | ~75-80% |
| Precision (Bad Risk) | High |
| Recall (Bad Risk) | High |

**Note:** Special attention was given to **Bad Risk recall** (sensitivity), which is critical in credit risk modeling to minimize defaults.

---

## 🚀 Deployment

The trained model is deployed as an **interactive web application** using Streamlit.

### Features:
✅ User-friendly interface  
✅ Real-time credit risk predictions  
✅ Input validation  
✅ Instant feedback on risk classification  

---

## 📁 Project Structure

```
Credit Risk Modeling Machine Lea.../
├── analysis_model.ipynb
├── app.py
├── german_credit_data.csv
├── *.pkl (các encoder và model files)
├── README.md
├── requirements.txt 
└── .gitignore       

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Scikit-learn** - Machine learning
- **Streamlit** - Web app framework
- **Joblib** - Model serialization



## ▶️ How to Run the Application
```
### 1️⃣ Clone the repository
```bash
git clone https://github.com/lequangduyet03/Credit-Risk-Modeling-Machine-Learning.git
cd Credit-Risk-Modeling-Machine-Learning
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

### 4️⃣ Open in browser

The app will automatically open at `http://localhost:8501`

---

## 📦 Requirements

Create a `requirements.txt` file with:

```
streamlit==1.28.0
pandas==2.0.3
scikit-learn==1.3.0
joblib==1.3.2
numpy==1.24.3
```

---

## 📈 Future Improvements

- [ ] **Probability-based risk scoring** - Use `predict_proba()` for confidence scores
- [ ] **SHAP values** - Add model explainability for interpretable predictions
- [ ] **Threshold optimization** - Cost-sensitive threshold tuning
- [ ] **Model comparison** - Test Logistic Regression, XGBoost, LightGBM
- [ ] **Feature importance** - Visualize which features drive predictions
- [ ] **API deployment** - Create REST API using FastAPI
- [ ] **Docker containerization** - Package app for easy deployment

---

## 🎓 Key Learnings

This project demonstrates:
- Complete ML pipeline from data to deployment
- Handling imbalanced classification problems
- Model persistence and reproducibility
- Building production-ready ML applications
- Best practices in credit risk modeling

---

## 👤 Author

lequangduyet03 - [GitHub](https://github.com/lequangduyet03)

**Focus Areas:**
- Machine Learning
- Credit Risk Modeling
- End-to-End ML Pipelines
- MLOps & Deployment

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---


## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐!

---

**Note:** This project is for educational purposes and demonstrates ML concepts. For production use in financial institutions, additional validation, regulatory compliance, and risk management practices would be required.
