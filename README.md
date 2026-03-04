# 🚀 ProductPulse

### AI-Driven Product Analytics, Retention Intelligence & Experimentation Platform

ProductPulse is a **data-driven product analytics platform** designed to help product teams understand **user behavior, retention, churn risk, and feature adoption** while supporting **data-backed product decisions and experimentation**.

The project simulates how modern product teams use **analytics, machine learning, and experimentation frameworks** to improve product growth and user engagement.

This project demonstrates capabilities required for **Product Manager, Product Analyst, and Scrum Master roles**, including:

* Product analytics
* User behavior analysis
* Data-driven decision making
* Experimentation (A/B testing)
* Predictive modeling for churn
* Product strategy development

---

# 🎯 Project Goal

Digital products generate massive volumes of user interaction data, but product teams often struggle to answer key strategic questions:

• Why are users dropping off in the product funnel?
• Which features drive retention?
• Which users are likely to churn?
• Which product changes should be prioritized?
• How should experiments be evaluated?

ProductPulse provides a framework to **analyze product usage data and convert insights into product decisions.**

---

# 🧠 Key Product Questions Answered

This project answers several important **product management questions**:

• What is the **conversion funnel performance**?
• Where do users **drop off during the product journey**?
• What is the **user retention trend over time**?
• Which **features improve retention**?
• Which users are **likely to churn soon**?
• Do **new product features improve conversion rates**?

---

# 📊 Dataset

Dataset used:

**E-commerce Behavior Data from Multi-Category Store**

Source: Kaggle
Dataset Link
https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store

### Dataset Description

The dataset contains millions of **user interaction events in an e-commerce platform**.

Each record represents a user activity such as:

| Field        | Description                   |
| ------------ | ----------------------------- |
| event_time   | timestamp of user interaction |
| event_type   | view, cart, purchase          |
| product_id   | product identifier            |
| category_id  | product category              |
| brand        | product brand                 |
| price        | product price                 |
| user_id      | unique user                   |
| user_session | browsing session              |

These events simulate how users interact with a real digital product.

---

# ⚙️ Technology Stack

### Programming

• Python
• SQL

### Data Processing

• Pandas
• NumPy
• PyArrow

### Analytics Database

• DuckDB

### Machine Learning

• Scikit-learn

### Experimentation Statistics

• SciPy

### Data Visualization

• Plotly
• Streamlit

### Development Environment

• VS Code (MacOS)
• Conda / Miniforge environment

### Version Control

• Git
• GitHub

---

# 🏗️ Project Architecture

```
productpulse
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── exploration
│   ├── metrics analysis
│   └── retention analysis
│
├── src
│   ├── etl.py
│   ├── metrics.py
│   ├── features.py
│   ├── churn_model.py
│   ├── insights.py
│   ├── adoption.py
│   └── ab_testing.py
│
├── sql
│   ├── create tables
│   ├── funnel metrics
│   ├── retention analysis
│   └── feature adoption
│
├── dashboards
│   └── streamlit dashboard
│
├── reports
│   ├── analytics outputs
│   ├── churn model results
│   └── AI insights
│
├── strategy
│   ├── PRD.md
│   └── Roadmap.md
│
├── experiments
│   └── ab test results
│
├── models
│   └── churn prediction model
│
└── README.md
```

---

# 📈 Product Analytics Metrics Implemented

ProductPulse calculates several **core product metrics used in real product teams.**

---

## 1️⃣ Conversion Funnel Analysis

Tracks the user journey:

```
Product View → Add to Cart → Purchase
```

Metrics calculated:

• total viewers
• users adding to cart
• total purchases
• conversion rate

This identifies **drop-off points in the product journey**.

---

## 2️⃣ Retention Analysis

User retention is calculated using **cohort analysis**.

Users are grouped based on the **week of first activity**, and the system tracks whether they return in future weeks.

Retention helps measure:

• product stickiness
• long-term engagement
• user lifecycle behavior

---

## 3️⃣ Feature Adoption Analysis

ProductPulse analyzes which product actions influence retention.

Example features analyzed:

• viewing products
• adding items to cart
• completing purchases

Example insight:

Users who **add items to cart** have significantly higher retention rates compared to users who only browse products.

---

# 🤖 Churn Prediction Model

The project includes a **machine learning model that predicts whether a user will churn.**

### Churn Definition

```
User inactive for 14 days
```

### Features Used

| Feature        | Description              |
| -------------- | ------------------------ |
| sessions       | number of user sessions  |
| views          | number of product views  |
| carts          | cart additions           |
| purchases      | purchases made           |
| revenue        | total revenue generated  |
| lifecycle_days | user lifecycle duration  |
| recency_days   | days since last activity |

### Models Used

• Logistic Regression
• Random Forest

The best model is selected based on **AUC score**.

Example output:

```
User 48219 → 72% probability of churn
```

This allows product teams to identify **high-risk users and take retention actions.**

---

# 🧪 A/B Testing Simulation

ProductPulse includes a **product experimentation module**.

Example experiment:

**Testing new checkout design**

| Group | Users  | Purchases |
| ----- | ------ | --------- |
| A     | 10,000 | 1,200     |
| B     | 10,000 | 1,450     |

Metrics calculated:

• conversion rate
• conversion lift
• z-score
• p-value

Example result:

```
New checkout increases conversion by 20%
Statistically significant (p < 0.05)
Decision → Ship new design
```

This demonstrates **product experimentation methodology.**

---

# 📊 Product Decision Dashboard

The project includes a **Streamlit dashboard** to visualize insights.

Dashboard features:

• conversion funnel trends
• retention cohorts
• feature adoption metrics
• A/B experiment results
• AI product recommendations

Run the dashboard:

```
streamlit run dashboards/app.py
```

---

# 💡 AI-Generated Product Insights

The analytics engine produces product recommendations such as:

• improve checkout experience
• encourage early cart activity
• reduce friction in product discovery
• optimize high-traffic product categories

These insights simulate **how product teams interpret analytics results.**

---

# 🗺️ Product Strategy

Based on the analytics findings, a **product strategy layer** was developed.

Documents included:

```
strategy/PRD.md
strategy/Roadmap.md
```

These contain:

• problem statement
• user personas
• product goals
• feature proposals
• sprint roadmap

This demonstrates **product management thinking beyond technical analysis.**

---

# 🔄 Data Pipeline

The data pipeline follows a structured workflow.

```
Raw Dataset
     ↓
ETL Data Processing
     ↓
Analytics Database
     ↓
Product Metrics Calculation
     ↓
Churn Prediction Model
     ↓
Feature Adoption Analysis
     ↓
A/B Experiment Evaluation
     ↓
Product Decision Dashboard
```

This architecture mirrors **real-world product analytics platforms.**

---

# 🚀 How to Run the Project

### 1️⃣ Clone repository

```
git clone https://github.com/YOUR_USERNAME/productpulse.git
cd productpulse
```

---

### 2️⃣ Create Python environment

```
conda create -n productpulse python=3.11
conda activate productpulse
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run ETL pipeline

```
python -m src.etl
```

---

### 5️⃣ Generate analytics metrics

```
python -m src.metrics
```

---

### 6️⃣ Generate AI insights

```
python -m src.insights
```

---

### 7️⃣ Train churn prediction model

```
python -m src.churn_model
```

---

### 8️⃣ Run A/B testing simulation

```
python -m src.ab_testing
```

---

### 9️⃣ Launch dashboard

```
streamlit run dashboards/app.py
```

---

# 📊 Example Insights

Some example insights derived from the dataset:

• Major drop-off between **product view and cart stage**
• Cart abandonment indicates **checkout friction**
• Users adding products to cart have **higher retention rates**
• Evening hours show **peak user activity**

These insights can inform **product roadmap prioritization.**

---

# 🧪 Future Improvements

Potential enhancements include:

• real-time analytics pipeline
• advanced churn prediction models
• user segmentation using clustering
• recommendation systems
• automated experimentation platform

---

# 👤 Author

**Chakshu Jagadish**

Master’s Student – Computer Science
Stevens Institute of Technology

Focus Areas

• Product Management
• Product Analytics
• Data-Driven Decision Making
• Agile Product Development

---

# ⭐ Why This Project Matters

ProductPulse demonstrates skills required in modern product teams:

✔ product analytics
✔ machine learning
✔ experimentation frameworks
✔ data-driven product strategy
✔ dashboard-driven decision making

This project replicates how companies such as **Amazon, Uber, and Meta analyze product data to guide product decisions.**

---
