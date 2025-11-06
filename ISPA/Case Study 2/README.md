# Customer Churn Prediction: Model Development, Validation, and Deployment

This repository contains the source code and documentation for the **Case Study Assignment** for **21AIC401T: Inferential Statistics and Predictive Analytics**.

The project focuses on developing, comparing, and designing a deployment strategy for predictive models to identify customers likely to churn from a telecommunications company.

---

##  Project Overview

The objective was to build models that can be used **operationally for retention campaigns**. We compared:

- A **highly interpretable Decision Tree model** (used as a proxy for CHAID)  
- A **highly predictive Logistic Regression model**

**Champion Model**: **Logistic Regression** (Selected for deployment due to superior scoring capability).

---

## 📊 Key Results

| Metric                | Logistic Regression (Champion) | Decision Tree (CHAID Proxy) | Interpretation |
|-----------------------|-------------------------------|-----------------------------|----------------|
| **ROC-AUC**           | 0.8452                        | 0.8231                      | Superior ability to discriminate high-risk customers |
| **Accuracy**          | 0.8125                        | 0.7893                      | Overall correct prediction rate |
| **Lift @ Top 10%**    | **2.85x**                     | N/A                         | **285% more effective** than random targeting |

---

## 🔍 Core Findings

- **Contractual status** is the most significant factor driving churn.
- **Highest Risk Segment**: Customers on **Month-to-month contracts** who **lack protective services** (e.g., *Online Security*, *Tech Support*) are the most volatile group.
- **Business Impact**: The Logistic Regression model allows the company to focus retention efforts on the **top 30% riskiest customers**, capturing **70% of all actual churners**, leading to **optimized resource allocation**.

---

## 📁 Repository Structure

| File/Folder                         | Description |
|-------------------------------------|-------------|
| `[model].ipynb`                     | Source Code: Contains all steps for **Data Preparation**, **EDA**, **Model Building (LogReg & DT)**, **Model Evaluation**, and **Chart Generation**. |
| `WA_Fn-UseC_-Telco-Customer-Churn.csv` | The raw input dataset used for the project. |
| `churn_prediction_report.pdf`       | Final Report Submission: The detailed **15-page academic report** (Task 5). |
| `champion_model_logreg.joblib`      | Serialized Logistic Regression model (Output of Task 4). |
| `README.md`                         | This file, summarizing the project. |

---

## Instructions to Run the Code

The project was developed in a **Python environment** using common data science libraries.

### Prerequisites

- **Python 3.8+**
- Install required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

> **Note**: The original CHAID library failed due to compatibility issues; a standard Decision Tree was used as a proxy.

### Execution

1. Clone this repository:
   ```bash
   git init ispa
   cd ispa
   git remote add origin https://github.com/ancybjohn02/course_projects.git
   git config core.sparseCheckout true
   git config core.sparseCheckoutCone true
   echo "ISPA/Case Study 2/" >> .git/info/sparse-checkout
   
   git pull origin main
   ```

2. Open the Jupyter Notebook file (`[model].ipynb`).

3. Run all cells **sequentially**. The notebook executes:
   - **Data Cleaning** and **Feature Engineering** (Discretization & One-Hot Encoding)
   - **Model Training** (Logistic Regression and Decision Tree Proxy)
   - **Metric Calculation** and **Chart Generation** (Lift/Gains curves)
   - **Model Serialization** (using `joblib`)

---

## Model Deployment Strategy

The **champion model (Logistic Regression)** is saved via `joblib` for production deployment. The strategy emphasizes **continuous maintenance**:

- **Serialization**: Model saved as `champion_model_logreg.joblib`.
- **Pipeline**: A **scoring pipeline** is required to ensure consistent **One-Hot Encoding** and **imputation** on live data.
- **Maintenance**:
  - Performance is monitored via **live ROC-AUC tracking**.
  - **Retraining** is scheduled every **3–6 months**.
  - Validated using **A/B Testing** to combat **model drift**.

---

## Developed for

**21AIC401T: Inferential Statistics and Predictive Analytics**

---

## Visualizations

![ Lift Chart (Left) and the Gains Chart (Right)](image.png)

![Monthly Charges by Churn Status](image-1.png)

![Churn Rate by Contract Type](image-2.png)

![Churn Distribution (Target Variable)](image-3.png)


--- 

**This README complies with academic and technical documentation standards for predictive modeling projects.**
