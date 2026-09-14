# Customer Churn Analysis – AfriConnect Telecom

## Project Overview

This project analyzes customer churn for AfriConnect Telecom, a fictional African telecommunications company.

The project uses Python to examine customer information, identify patterns associated with churn, calculate customer risk scores, classify customers into different risk levels, and develop business recommendations for customer retention.

## Business Problem

Customer churn is an important business challenge because losing customers can affect revenue and long-term customer relationships.

AfriConnect needs a simple way to identify customers showing warning signs that may be associated with churn so that appropriate retention actions can be considered.

## Project Objective

The objectives of this project are to:

- Analyze customer information.
- Measure the level of customer churn.
- Compare churned and retained customers.
- Identify churn-related warning signals.
- Calculate customer risk scores.
- Classify customers as High, Medium, or Low Risk.
- Identify the highest-risk customers.
- Provide practical customer-retention recommendations.

## Dataset

The project uses a simulated dataset containing 20 customers.

The dataset contains the following fields:

- Customer_ID
- Age
- Tenure
- Monthly_Charge
- Complaints
- Support_Calls
- Satisfaction
- Last_Activity
- Churn

## Methodology

The project was completed using basic Python concepts, including:

- Lists
- Dictionaries
- Variables
- Loops
- Conditional statements
- Logical operators
- Calculations

The analysis involved:

1. Creating the customer dataset.
2. Checking data quality.
3. Analyzing customer characteristics.
4. Comparing churned and retained customers.
5. Identifying churn-related warning signals.
6. Applying rule-based risk logic.
7. Calculating risk scores.
8. Classifying customers by risk level.
9. Developing business recommendations.

## Key Findings

The dataset contains 20 customers.

- 8 customers churned.
- 12 customers were retained.
- Overall churn rate: 40%.
- 10 customers were classified as High Risk.
- 1 customer was classified as Medium Risk.
- 9 customers were classified as Low Risk.

Churned customers generally showed lower satisfaction, more complaints, shorter tenure, and longer periods of inactivity than retained customers in this sample.

## Risk Analysis

The project uses a rule-based risk-scoring system based on customer satisfaction, complaints, and recent activity.

Customers are classified into:

- **Low Risk:** 0–2
- **Medium Risk:** 3–5
- **High Risk:** 6–9

The five highest-risk customers are:

- C006
- C009
- C011
- C016
- C001

## Business Recommendations

### 1. Prioritize High-Risk Customers

AfriConnect should prioritize customers showing the strongest combination of churn-related warning signals for appropriate retention activities.

### 2. Improve Complaint Resolution

The company should investigate recurring customer complaints and improve complaint-resolution processes.

### 3. Monitor Customer Inactivity

AfriConnect should monitor prolonged inactivity and consider appropriate re-engagement activities for inactive customers, particularly those also classified as High Risk.

## Limitations

The project uses a small simulated dataset of 20 customers.

The risk system is rule-based and is not a machine-learning prediction model.

Therefore, the findings should be interpreted as patterns within the sample rather than definitive predictions about the entire customer population.

## Future Improvements

Future versions could:

- Use a larger dataset.
- Import data from CSV files.
- Use pandas for larger-scale analysis.
- Introduce machine-learning techniques.
- Add visualizations and dashboards.
- Improve customer segmentation.

## Project Files

- `customer_churn_analysis.ipynb` – Main analysis notebook.
- `customer_churn_analysis.py` – Python source code.
- `customers.py` – Customer dataset.
- `data_dictionary.docx` – Description of dataset fields.
- `business_report.docx` – Summary of the business analysis and recommendations.

## Collaborators

- Owolabi Ayotomiwa

## Conclusion

This project demonstrates how basic Python can be used to analyze customer data, identify churn-related warning signals, classify customers according to risk, and support customer-retention decisions.
