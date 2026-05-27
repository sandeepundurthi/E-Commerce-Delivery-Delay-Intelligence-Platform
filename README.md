# 📦 E-Commerce Delivery Delay Intelligence Platform

An end-to-end operations analytics and machine learning platform designed to analyze shipment delays, identify logistics bottlenecks, and predict delivery risks using e-commerce operational data.

---

# 🚀 Project Overview

This project simulates a real-world logistics intelligence system similar to those used by companies like Amazon, Walmart, and FedEx to monitor operational performance and predict shipment delays.

The platform integrates:

- PostgreSQL analytics database
- SQL-based KPI analysis
- Exploratory data analysis (EDA)
- Machine learning models
- Streamlit interactive dashboard
- Operational risk prediction

---

# 📊 Key Features

✅ Delivery delay analytics dashboard  
✅ Warehouse performance monitoring  
✅ Shipment mode analysis  
✅ Product importance analysis  
✅ Customer support escalation insights  
✅ Machine learning-based delay prediction  
✅ Feature importance analysis  
✅ Interactive operational intelligence dashboard  

---

# 🛠️ Tech Stack

## Languages & Libraries
- Python
- SQL

## Machine Learning
- Scikit-learn
- Random Forest
- XGBoost
- Logistic Regression

## Data Analysis
- Pandas
- NumPy

## Visualization
- Plotly
- Matplotlib
- Seaborn

## Database
- PostgreSQL

## Dashboard
- Streamlit

---

# 🗂️ Project Architecture

```text
Raw Shipment Data
       ↓
Data Cleaning & ETL
       ↓
PostgreSQL Database
       ↓
SQL KPI Analytics
       ↓
EDA & Root Cause Analysis
       ↓
Machine Learning Models
       ↓
Streamlit Dashboard
```

---

# 📈 Operational Insights

## Key Findings

- Overall shipment delay rate was approximately 40%
- Warehouse A showed the highest delay rate
- Road shipments experienced the highest delays
- High-priority products had significantly fewer delays
- Customer support calls strongly correlated with shipment delays
- Discount strategies and package weight were the strongest delay predictors

---

# 🤖 Machine Learning Results

| Model | Accuracy |
|------|------|
| Logistic Regression | 63.3% |
| Random Forest | 68.3% |
| XGBoost | 67.1% |

## Top Predictive Features

- Discount Offered
- Package Weight
- Cost of Product
- Prior Purchases

---

# 📊 Dashboard Features

The Streamlit dashboard includes:

- Operational KPI monitoring
- Interactive shipment analytics
- Delivery status visualization
- Operational risk driver analysis
- ML-powered delay prediction
- Dynamic filtering capabilities

---

# 📸 Dashboard Preview

Add screenshots here:

```text
screenshots/dashboard.png
```

---

# ⚙️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/ecommerce-delay-intelligence.git

cd ecommerce-delay-intelligence
```

---

## 2. Create Virtual Environment

### Mac/Linux

```bash
python -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup PostgreSQL Database

Create database:

```sql
CREATE DATABASE ecommerce_delay_db;
```

---

## 5. Run ETL Pipeline

```bash
python src/etl/prepare_data.py

python src/etl/load_to_postgres.py
```

---

## 6. Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```text
ecommerce-delay-intelligence/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda_kpi_analysis.ipynb
│   └── 03_ml_modeling.ipynb
│
├── models/
│   └── random_forest_delay_model.pkl
│
├── sql/
│   └── analytics_queries.sql
│
├── src/
│   └── etl/
│       ├── prepare_data.py
│       └── load_to_postgres.py
│
└── screenshots/
```

---

# 💼 Business Impact

This platform demonstrates how operational analytics and machine learning can help logistics organizations:

- Reduce shipment delays
- Improve customer satisfaction
- Optimize warehouse performance
- Identify operational bottlenecks
- Predict high-risk deliveries
- Improve logistics decision-making

---

# 👨‍💻 Author

Sandeep Undurthi

- LinkedIn: https://linkedin.com/in/sandeep-undurthi
- GitHub: https://github.com/sandeepundurthi

---# E-Commerce-Delivery-Delay-Intelligence-Platform
