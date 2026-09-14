#!/usr/bin/env python
# coding: utf-8

# # CUSTOMER CHURN PREDICTION & RETENTION INTELLIGIENCE SYSTEM
# 
# ## AfriConnect Telecom
# 
# This project analyzes customer information to understand customer churn, identify characteristics associated with churn risk, and develop a simple rule-based system for classifying customers according to their level of churn risk.
# 

# ## 1. Business Problem
# 
# AfriConnect Telecom is a fictional African telecommunications company that provides services such as voice, mobile data, SMS, internet packages, digital services, customer support, and subscription plans.
# 
# The company has noticed that some customers are becoming inactive or switching to competing providers. However, the company currently relies mainly on a reactive approach, meaning that it often discovers that a customer has left only after the customer has already stopped using its services.
# 
# This creates a customer-retention problem. Management wants to move from a reactive approach to a more proactive approach by using customer information to identify signs that may be associated with churn risk.
# 
# The business therefore wants an analytical solution that can help answer two important questions:
# 
# 1. Which customers are showing signs of churn risk?
# 2. What characteristics are associated with that risk?
# 
# This project uses customer demographic, tenure, spending, complaints, customer-support, satisfaction, activity, and churn information to investigate customer behaviour and identify patterns associated with churn risk.
# 

# ## 2. Project Objective
# 
# The main objective of this project is to analyze AfriConnect customer data and develop a simple Python-based system for understanding customer churn and identifying customers who may be at risk.
# 
# The project aims to:
# 
# * understand the characteristics of AfriConnect's customer base;
# * measure the current level of customer churn;
# * identify patterns and characteristics associated with churn;
# * investigate factors such as age, tenure, monthly charge, complaints, support calls, satisfaction, and customer activity;
# * identify customers who display multiple warning signs associated with higher churn risk;
# * create a simple rule-based risk scoring system;
# * classify customers into Low, Medium, and High risk categories;
# * identify the highest-risk customers;
# * translate the analytical findings into practical customer-retention recommendations.
# 
# The purpose is not only to calculate churn statistics, but also to demonstrate how customer data can be transformed into information that can support business decision-making.
# 

# ### Analytical Questions
# 
# The analysis will answer the following questions:
# 
# #### Customer Base
# 
# 1. How many customers are in the dataset?
# 2. What percentage of customers have churned?
# 
# #### Churn Analysis
# 
# 3. What is the average satisfaction of churned and retained customers?
# 4. What is the average number of complaints for churned and retained customers?
# 5. What is the average tenure of churned and retained customers?
# 6. Which customers have been inactive for more than 15 days?
# 7. Which customers have a satisfaction score of 2 or below and at least 3 complaints?
# 
# #### Risk Analysis
# 
# 8. What risk score should be assigned to each customer?
# 9. How should customers be classified as Low, Medium, or High Risk?
# 10. Which customers have the highest risk scores?
# 
# #### Business Decision
# 
# 11. What recommendations should AfriConnect consider for customers identified as high-risk?

# ## 03. Dataset Description
# 
# For this project, a sample dataset containing 20 AfriConnect customers is used.
# 
# The dataset is intentionally small because the purpose of this version of the project is to learn and demonstrate the logic of customer churn analysis using basic Python. The data is created directly inside Python rather than being imported from an external CSV or Excel file.
# 
# Each customer is represented by a record containing information about their age, tenure, monthly charge, complaints, support calls, satisfaction, recent activity, and churn status.
# 
# The dataset contains the following nine fields:
# 
# * `Customer_ID`
# * `Age`
# * `Tenure`
# * `Monthly_Charge`
# * `Complaints`
# * `Support_Calls`
# * `Satisfaction`
# * `Last_Activity`
# * `Churn`
# 
# The `Churn` field is the target variable. A value of `1` means that the customer churned, while a value of `0` means that the customer stayed with AfriConnect.
# 
# The dataset is a simulated dataset created for this educational project and does not represent real AfriConnect customers.
# 

# ## 04. Data Dictionary
# 
# The data dictionary explains the meaning of each field in the customer dataset.
# 
# | Field            | Meaning                                                                              |
# | ---------------- | ------------------------------------------------------------------------------------ |
# | `Customer_ID`    | A unique identification code for each customer.                                      |
# | `Age`            | The customer's age in years.                                                         |
# | `Tenure`         | The number of months the customer has been with AfriConnect.                         |
# | `Monthly_Charge` | The amount the customer pays for the service each month.                             |
# | `Complaints`     | The number of complaints made by the customer.                                       |
# | `Support_Calls`  | The number of times the customer contacted customer support.                         |
# | `Satisfaction`   | The customer's satisfaction score, ranging from 1 to 5.                              |
# | `Last_Activity`  | The number of days since the customer last used the service.                         |
# | `Churn`          | Shows whether the customer left AfriConnect. `1` means churned and `0` means stayed. |
# 
# ### Satisfaction Scale
# 
# The `Satisfaction` field uses the following scale:
# 
# * `1` — Very Low
# * `2` — Low
# * `3` — Neutral
# * `4` — High
# * `5` — Very High
# 
# ### Churn Values
# 
# The `Churn` field is represented as:
# 
# * `1` — Customer churned
# * `0` — Customer stayed
# 

# ## Dataset Creation

# In[1]:


customers = [
    {
        "Customer_ID": "C001",
        "Age": 25,
        "Tenure": 3,
        "Monthly_Charge": 4500,
        "Complaints": 4,
        "Support_Calls": 5,
        "Satisfaction": 2,
        "Last_Activity": 18,
        "Churn": 1
    },
    {
        "Customer_ID": "C002",
        "Age": 42,
        "Tenure": 36,
        "Monthly_Charge": 8500,
        "Complaints": 0,
        "Support_Calls": 1,
        "Satisfaction": 5,
        "Last_Activity": 2,
        "Churn": 0
    },
    {
        "Customer_ID": "C003",
        "Age": 31,
        "Tenure": 8,
        "Monthly_Charge": 6000,
        "Complaints": 3,
        "Support_Calls": 4,
        "Satisfaction": 2,
        "Last_Activity": 15,
        "Churn": 1
    },
    {
        "Customer_ID": "C004",
        "Age": 29,
        "Tenure": 24,
        "Monthly_Charge": 7000,
        "Complaints": 1,
        "Support_Calls": 2,
        "Satisfaction": 4,
        "Last_Activity": 5,
        "Churn": 0
    },
    {
        "Customer_ID": "C005",
        "Age": 51,
        "Tenure": 48,
        "Monthly_Charge": 9500,
        "Complaints": 0,
        "Support_Calls": 1,
        "Satisfaction": 5,
        "Last_Activity": 1,
        "Churn": 0
    },
    {
        "Customer_ID": "C006",
        "Age": 23,
        "Tenure": 2,
        "Monthly_Charge": 4000,
        "Complaints": 5,
        "Support_Calls": 6,
        "Satisfaction": 1,
        "Last_Activity": 25,
        "Churn": 1
    },
    {
        "Customer_ID": "C007",
        "Age": 37,
        "Tenure": 18,
        "Monthly_Charge": 7500,
        "Complaints": 2,
        "Support_Calls": 3,
        "Satisfaction": 3,
        "Last_Activity": 8,
        "Churn": 0
    },
    {
        "Customer_ID": "C008",
        "Age": 46,
        "Tenure": 30,
        "Monthly_Charge": 9000,
        "Complaints": 1,
        "Support_Calls": 1,
        "Satisfaction": 4,
        "Last_Activity": 3,
        "Churn": 0
    },
    {
        "Customer_ID": "C009",
        "Age": 28,
        "Tenure": 6,
        "Monthly_Charge": 5000,
        "Complaints": 4,
        "Support_Calls": 5,
        "Satisfaction": 2,
        "Last_Activity": 20,
        "Churn": 1
    },
    {
        "Customer_ID": "C010",
        "Age": 34,
        "Tenure": 14,
        "Monthly_Charge": 6500,
        "Complaints": 2,
        "Support_Calls": 3,
        "Satisfaction": 3,
        "Last_Activity": 10,
        "Churn": 0
    },
    {
        "Customer_ID": "C011",
        "Age": 22,
        "Tenure": 4,
        "Monthly_Charge": 4200,
        "Complaints": 5,
        "Support_Calls": 7,
        "Satisfaction": 1,
        "Last_Activity": 28,
        "Churn": 1
    },
    {
        "Customer_ID": "C012",
        "Age": 55,
        "Tenure": 60,
        "Monthly_Charge": 10000,
        "Complaints": 0,
        "Support_Calls": 0,
        "Satisfaction": 5,
        "Last_Activity": 1,
        "Churn": 0
    },
    {
        "Customer_ID": "C013",
        "Age": 39,
        "Tenure": 22,
        "Monthly_Charge": 8000,
        "Complaints": 1,
        "Support_Calls": 2,
        "Satisfaction": 4,
        "Last_Activity": 4,
        "Churn": 0
    },
    {
        "Customer_ID": "C014",
        "Age": 27,
        "Tenure": 7,
        "Monthly_Charge": 5500,
        "Complaints": 3,
        "Support_Calls": 4,
        "Satisfaction": 2,
        "Last_Activity": 17,
        "Churn": 1
    },
    {
        "Customer_ID": "C015",
        "Age": 44,
        "Tenure": 40,
        "Monthly_Charge": 8800,
        "Complaints": 0,
        "Support_Calls": 1,
        "Satisfaction": 5,
        "Last_Activity": 2,
        "Churn": 0
    },
    {
        "Customer_ID": "C016",
        "Age": 30,
        "Tenure": 5,
        "Monthly_Charge": 4800,
        "Complaints": 4,
        "Support_Calls": 5,
        "Satisfaction": 2,
        "Last_Activity": 22,
        "Churn": 1
    },
    {
        "Customer_ID": "C017",
        "Age": 48,
        "Tenure": 32,
        "Monthly_Charge": 9200,
        "Complaints": 1,
        "Support_Calls": 1,
        "Satisfaction": 4,
        "Last_Activity": 3,
        "Churn": 0
    },
    {
        "Customer_ID": "C018",
        "Age": 26,
        "Tenure": 3,
        "Monthly_Charge": 4300,
        "Complaints": 3,
        "Support_Calls": 5,
        "Satisfaction": 2,
        "Last_Activity": 19,
        "Churn": 1
    },
    {
        "Customer_ID": "C019",
        "Age": 41,
        "Tenure": 27,
        "Monthly_Charge": 7800,
        "Complaints": 1,
        "Support_Calls": 2,
        "Satisfaction": 4,
        "Last_Activity": 6,
        "Churn": 0
    },
    {
        "Customer_ID": "C020",
        "Age": 33,
        "Tenure": 10,
        "Monthly_Charge": 6200,
        "Complaints": 3,
        "Support_Calls": 4,
        "Satisfaction": 3,
        "Last_Activity": 12,
        "Churn": 0
    }
]


# ## 05. Data Quality Investigation
# 
# Before performing any analysis, the dataset must be checked for possible errors or inconsistencies.
# 
# Data quality is important because incorrect, missing, duplicated, or unusual values can affect the results of the analysis and lead to incorrect conclusions about customer churn.
# 
# The dataset was therefore investigated for the following possible issues:
# 
# * missing values;
# * duplicate customer records;
# * incorrect customer identification values;
# * invalid monthly charges;
# * unusual satisfaction scores;
# * unusual tenure or activity values;
# * incorrect churn values.
# 
# The purpose of this investigation is to identify any problems in the original dataset before proceeding with the analysis.
# 

# ### 5.1 Number of Customers
# 
# The first check is to confirm that the dataset contains the expected number of customer records.
# 
# The project specifies a sample dataset containing 20 customers. Therefore, the length of the `Customers` list will be checked to confirm that all 20 records are present.
# 

# ### Code

# In[2]:


print("Number of customers:", len(customers))


# ### 5.2 Number of Fields
# 
# Each customer should contain the nine fields defined in the data dictionary.
# 
# The first customer record will therefore be checked to confirm that the expected number of fields is present.

# ### Code

# In[3]:


print("Number of fields:", len(customers[0]))


# ### 5.3 Dataset Inspection
# 
# The customer records are displayed to allow the dataset to be inspected directly.
# 
# This makes it possible to observe the values recorded for each customer and identify any information that appears missing, duplicated, inconsistent, or unrealistic.
# 

# ### Code

# In[4]:


for customer in customers:
    print(f"Customer ID: {customer['Customer_ID']}")
    print(f"Age: {customer['Age']}")
    print(f"Tenure: {customer['Tenure']} months")
    print(f"Monthly Charge: {customer['Monthly_Charge']}")
    print(f"Complaints: {customer['Complaints']}")
    print(f"Support Calls: {customer['Support_Calls']}")
    print(f"Satisfaction: {customer['Satisfaction']}")
    print(f"Last Activity: {customer['Last_Activity']} days")
    print(f"Churn: {customer['Churn']}")
    print("-" * 40)


# ### 5.4 Duplicate Customer ID Check
# 
# Each customer should have a unique `Customer_ID`.
# 
# A duplicate ID could indicate that the same customer has been recorded more than once. The customer IDs will therefore be checked for duplicates.
# 

# ### Code

# In[5]:


customer_ids = []

for customer in customers:
    customer_ids.append(customer["Customer_ID"])

for customer_id in customer_ids:
    if customer_ids.count(customer_id) > 1:
        print("Duplicate Customer ID:", customer_id)

# If nothing prints, that means no duplicate ID was detected.


# ### 5.5 Monthly Charge Check
# 
# The `Monthly_Charge` field represents the amount a customer pays for the service each month.
# 
# A negative monthly charge would be unrealistic and should therefore be treated as a potential data-quality problem.
# 
# The dataset will be checked for any customer whose monthly charge is below zero.
# 

# ### Code

# In[6]:


for customer in customers:
    if customer["Monthly_Charge"] < 0:
        print("Invalid Monthly Charge:",
              customer["Customer_ID"],
              customer["Monthly_Charge"])

# No output means that no negative monthly charge was found.


# ### 5.6 Satisfaction Score Check
# 
# The `Satisfaction` field uses a scale from 1 to 5.
# 
# Therefore, a value below 1 or above 5 would be outside the defined scale and should be investigated.
# 

# In[7]:


for customer in customers:
    if customer["Satisfaction"] < 1 or customer["Satisfaction"] > 5:
        print("Invalid Satisfaction:",
              customer["Customer_ID"],
              customer["Satisfaction"])

# There is no output if there is no invalid / negative charge.


# ### 5.7 Churn Value Check
# 
# The `Churn` field is the target variable for the project.
# 
# It should contain only two possible values:
# 
# * `0` — customer stayed;
# * `1` — customer churned.
# 
# The dataset will therefore be checked for any value other than 0 or 1.
# 

# ### Code

# In[8]:


for customer in customers:
    if customer["Churn"] != 0 and customer["Churn"] != 1:
        print("Invalid Churn Value:",
              customer["Customer_ID"],
              customer["Churn"])

# No output means that all churn values are valid.


# ### 5.8 Missing Values Check
# 
# A missing value occurs when a required piece of information is not provided for a customer.
# 
# Missing values can affect calculations and may lead to inaccurate conclusions. Therefore, each field in every customer record is checked to determine whether any value is missing.
# 

# ### Code

# In[9]:


for customer in customers:
    for field, value in customer.items():
        if value == "" or value is None:
            print("Missing value found:",
                  customer["Customer_ID"],
                  field)

# No output means that no missing values were found.


# ### 5.9 Data Quality Investigation Summary
# 
# The dataset was inspected to determine whether it contained structural or value-related problems that could affect the analysis.
# 
# The investigation checked the number of customer records, number of fields, dataset contents, duplicate customer IDs, monthly charges, satisfaction scores, churn values, and missing values.
# 
# The results of these checks will be used to determine whether any data cleaning is required before the customer analysis begins.
# 

# # 06. Data Cleaning
# 
# ## 6.1 Data Cleaning Approach
# After completing the data-quality investigation, the dataset was reviewed to determine whether any corrections were required.
# 
# The investigation did not identify missing values, duplicate customer IDs, negative monthly charges, invalid satisfaction scores, or invalid churn values in the current dataset.
# 
# Therefore, no values were changed or removed from the dataset at this stage.
# 
# The dataset is retained in its original form for the customer and churn analysis that follows.
# 
# Keeping the original values unchanged also ensures that the subsequent analysis is based on the actual dataset provided for the project.
# 

# ### Code

# In[10]:


print("Customers after data cleaning:", len(customers))


# ### 6.2 Cleaned Dataset
# 
# Since no data-quality problems requiring correction were identified, the dataset remains unchanged.
# 
# The same 20 customer records will therefore be used for the remaining stages of the project.
# 
# The cleaned dataset will serve as the input for customer analysis, churn analysis, risk scoring, and customer segmentation.
# 

# ## 07. Customer Analysis
# 
# ### 7.1 Total Customers
# 
# The first step is to determine the total number of customers in the dataset. This provides the basic size of the customer population being analyzed.
# 

# ### Code

# In[11]:


total_customers = len(customers)

print("Total Customers:", total_customers)


# ### 7.2 Churned and Retained Customers
# 
# The `Churn` field identifies whether a customer left the service.
# 
# * `1` represents a churned customer.
# * `0` represents a retained customer.
# 
# The customers are counted separately to understand the distribution between churned and retained customers.
# 

# ### Code

# In[12]:


churned_customers = 0
retained_customers = 0

for customer in customers:
    if customer["Churn"] == 1:
        churned_customers += 1
    else:
        retained_customers += 1

print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)


# ### 7.3 Churn Rate
# 
# The churn rate shows the percentage of customers in the dataset who have churned.
# 
# It is calculated using:
# 
# **Churn Rate = (Churned Customers ÷ Total Customers) × 100**
# 

# ### Code

# In[13]:


churn_rate = (churned_customers / total_customers) * 100

print("Churn Rate:", churn_rate, "%")


# ### Interpretation
# 
# The churn rate is 40%, meaning that 8 out of the 20 customers in the sample have churned.
# 
# This represents a substantial level of customer loss within the sample and indicates that AfriConnect should investigate the characteristics associated with these customers.
# 
# However, this result describes the sample dataset and should not automatically be treated as the churn rate of AfriConnect's entire customer population.
# 

# ### 7.4 Customers Who Churned
# 
# The specific customers who churned are identified by selecting records where `Churn` is equal to `1`.
# 

# ### Code

# In[14]:


print("Customers Who Churned:")

for customer in customers:
    if customer["Churn"] == 1:
        print(customer["Customer_ID"])

print("\nCustomers Who Stayed:")

for customer in customers:
    if customer["Churn"] == 0:
        print(customer["Customer_ID"])


# ### 7.5 Average Satisfaction by Churn Status
# 
# To investigate whether satisfaction differs between churned and retained customers, the average satisfaction score is calculated for both groups.
# 
# The satisfaction scale ranges from 1 to 5, where higher values represent greater customer satisfaction.
# 

# ### Code

# In[15]:


churned_satisfaction = 0
retained_satisfaction = 0

for customer in customers:
    if customer["Churn"] == 1:
        churned_satisfaction += customer["Satisfaction"]
    else:
        retained_satisfaction += customer["Satisfaction"]

average_churned_satisfaction = churned_satisfaction / churned_customers
average_retained_satisfaction = retained_satisfaction / retained_customers

print("Average Satisfaction - Churned:", average_churned_satisfaction)
print("Average Satisfaction - Retained:", average_retained_satisfaction)


# ### Interpretation
# 
# In this sample, churned customers had a much lower average satisfaction score of 1.75 compared with 4.08 among retained customers.
# 
# This indicates an association between lower satisfaction and churn within the sample. However, the result does not prove that low satisfaction directly causes churn.
# 

# ### 7.6 Average Complaints by Churn Status
# 
# The average number of complaints is calculated for churned and retained customers to determine whether churned customers experienced more customer-service problems in the sample.
# 

# ### Code

# In[16]:


churned_complaints = 0
retained_complaints = 0

for customer in customers:
    if customer["Churn"] == 1:
        churned_complaints += customer["Complaints"]
    else:
        retained_complaints += customer["Complaints"]

average_churned_complaints = churned_complaints / churned_customers
average_retained_complaints = retained_complaints / retained_customers

print("Average Complaints - Churned:", average_churned_complaints)
print("Average Complaints - Retained:", average_retained_complaints)


# ### Interpretation
# 
# In this sample, churned customers had an average of 3.875 complaints, while retained customers had an average of approximately 1.0 complaints.
# 
# This suggests that churned customers experienced more complaint-related activity than retained customers in the sample.
# 

# ### 7.7 Average Tenure by Churn Status
# 
# Customer tenure is compared between churned and retained customers to investigate whether newer customers appear more likely to churn in the sample.
# 

# ### Code

# In[17]:


churned_tenure = 0
retained_tenure = 0

for customer in customers:
    if customer["Churn"] == 1:
        churned_tenure += customer["Tenure"]
    else:
        retained_tenure += customer["Tenure"]

average_churned_tenure = churned_tenure / churned_customers
average_retained_tenure = retained_tenure / retained_customers

print("Average Tenure - Churned:", average_churned_tenure)
print("Average Tenure - Retained:", average_retained_tenure)


# ### Interpretation
# 
# In this sample, churned customers had an average tenure of 4.75 months, compared with 30.083 months for retained customers.
# 
# This shows a strong difference between the two groups and suggests that customers with shorter tenure were more represented among the churned customers in this sample.
# 

# ### 7.8 Recent Activity Comparison
# 
# `Last_Activity` represents the number of days since a customer last used the service.
# 
# A higher value means that the customer has been inactive for a longer period.
# 
# The average inactivity period is therefore compared between churned and retained customers.
# 

# In[18]:


churned_activity = 0
retained_activity = 0

for customer in customers:
    if customer["Churn"] == 1:
        churned_activity += customer["Last_Activity"]
    else:
        retained_activity += customer["Last_Activity"]

average_churned_activity = churned_activity / churned_customers
average_retained_activity = retained_activity / retained_customers

print("Average Inactivity - Churned:", average_churned_activity)
print("Average Inactivity - Retained:", average_retained_activity)


# ### Interpretation
# 
# In this sample, churned customers had been inactive for an average of 20.5 days, compared with 4.75 days for retained customers.
# 
# This indicates that longer periods of inactivity were associated with churn in the sample.
# 

# ## 08. Churn Analysis
# 
# ### 8.1 Customers Inactive for More Than 15 Days
# 
# Customer inactivity can be an important warning signal when analyzing churn.
# 
# The `Last_Activity` field represents the number of days since a customer last used the service.
# 
# In this analysis, customers with more than 15 days since their last activity are identified.

# ### Code

# In[19]:


inactive_customers = []

for customer in customers:
    if customer["Last_Activity"] > 15:
        inactive_customers.append(customer["Customer_ID"])

print("Customers inactive for more than 15 days:")

for customer_id in inactive_customers:
    print(customer_id)


# ### Interpretation
# 
# Seven customers have been inactive for more than 15 days.
# 
# Most of these customers are also recorded as churned customers in the dataset. This suggests that prolonged inactivity is an important warning signal associated with churn in this sample.
# 
# However, inactivity alone does not prove that a customer will churn.

# ### 8.2 Customers with Satisfaction ≤ 2 and Complaints ≥ 3
# 
# Customers who have low satisfaction and a high number of complaints may be experiencing significant dissatisfaction with the service.
# 
# The project therefore requires customers whose satisfaction score is 2 or below and whose number of complaints is 3 or more to be identified.
# 
# Both conditions must be true for a customer to be included.

# ### Code

# In[20]:


high_concern_customers = []

for customer in customers:
    if customer["Satisfaction"] <= 2 and customer["Complaints"] >= 3:
        high_concern_customers.append(customer["Customer_ID"])

print("Customers with Satisfaction <= 2 and Complaints >= 3:")

for customer_id in high_concern_customers:
    print(customer_id)


# ### Interpretation
# 
# Eight customers satisfy both conditions.
# 
# All eight customers identified by this condition are churned customers in the sample.
# 
# This indicates a strong association between the combination of low satisfaction and frequent complaints and churn within this particular dataset.
# 
# However, this small sample does not establish that these factors directly cause churn.

# ### 8.3 Churn Analysis Summary
# 
# The analysis shows several noticeable characteristics among the churned customers in the sample.
# 
# First, churned customers generally had lower satisfaction scores than retained customers.
# 
# Second, churned customers had more complaints on average.
# 
# Third, churned customers had shorter average tenure.
# 
# Finally, churned customers showed longer periods of inactivity.
# 
# The combination of low satisfaction, frequent complaints and prolonged inactivity appears repeatedly among the churned customers.
# 
# These observations will be used as the foundation for developing the rule-based churn risk logic in the next section.

# ## 09. Churn Risk Logic
# 
# ### 9.1 Identifying High-Risk Customers
# 
# Based on the customer analysis, three warning signals are particularly important:
# 
# - Low satisfaction
# - A high number of complaints
# - A long period of inactivity
# 
# A customer will be considered high risk when all three of the following conditions are true:
# 
# - Satisfaction is less than or equal to 2
# - Complaints are greater than or equal to 3
# - Last Activity is greater than or equal to 15 days
# 
# All three conditions must be satisfied for the customer to be identified as high risk.

# ### Code

# In[21]:


print("High-Risk Customers:")
print()

for customer in customers:
    if (
        customer["Satisfaction"] <= 2
        and customer["Complaints"] >= 3
        and customer["Last_Activity"] >= 15
    ):
        print(customer["Customer_ID"])


# ### Interpretation
# 
# Eight customers meet all three high-risk conditions.
# 
# These customers have low satisfaction, at least three complaints, and at least 15 days of inactivity.
# 
# The result shows that several customers display multiple warning signals at the same time. These customers should receive closer attention when considering customer-retention activities.
# 
# This rule identifies customers showing risk signals in the sample; it does not guarantee that they will churn.

# ### 9.2 Building the Churn Risk Classifier
# 
# A simple risk classifier is created to assign every customer a risk level.
# 
# The classifier uses three levels:
# 
# - **High Risk:** The customer satisfies all three high-risk conditions.
# - **Medium Risk:** The customer does not meet all the high-risk conditions but satisfies at least one of the medium-risk conditions.
# - **Low Risk:** The customer does not satisfy the high-risk or medium-risk conditions.
# 
# The `if`, `elif`, and `else` statements are used to apply these rules.

# ### Code

# In[22]:


for customer in customers:

    if (
        customer["Satisfaction"] <= 2
        and customer["Complaints"] >= 3
        and customer["Last_Activity"] >= 15
    ):
        risk = "High"

    elif (
        customer["Satisfaction"] <= 3
        or customer["Complaints"] >= 2
        or customer["Last_Activity"] >= 10
    ):
        risk = "Medium"

    else:
        risk = "Low"

    print(customer["Customer_ID"], "→", risk)


# ### 9.3 Risk Classification Summary
# 
# After assigning a risk level to each customer, the number of customers in each category is counted.
# 
# This provides an overall view of how many customers fall into the High, Medium, and Low risk groups.

# ### Code

# In[23]:


high_risk = 0
medium_risk = 0
low_risk = 0

for customer in customers:

    if (
        customer["Satisfaction"] <= 2
        and customer["Complaints"] >= 3
        and customer["Last_Activity"] >= 15
    ):
        high_risk += 1

    elif (
        customer["Satisfaction"] <= 3
        or customer["Complaints"] >= 2
        or customer["Last_Activity"] >= 10
    ):
        medium_risk += 1

    else:
        low_risk += 1

print("High Risk:", high_risk)
print("Medium Risk:", medium_risk)
print("Low Risk:", low_risk)


# ### Interpretation
# 
# The classifier places 8 customers in the High Risk category, 3 customers in the Medium Risk category, and 9 customers in the Low Risk category.
# 
# The High Risk group contains customers who simultaneously show low satisfaction, multiple complaints, and prolonged inactivity.
# 
# The Medium Risk group contains customers who show at least one warning signal but do not meet all three High Risk conditions.
# 
# The Low Risk group does not meet the defined warning conditions.

# ## 10. Risk Scoring
# 
# ### 10.1 Risk Score Rules
# 
# A numerical risk score is created for every customer based on three factors:
# 
# **Satisfaction**
# - Satisfaction <= 2 → +3 points
# - Satisfaction = 3 → +2 points
# - Satisfaction >= 4 → +0 points
# 
# **Complaints**
# - Complaints >= 4 → +3 points
# - Complaints 2–3 → +2 points
# - Complaints < 2 → +0 points
# 
# **Inactivity**
# - Last Activity >= 20 days → +3 points
# - Last Activity 10–19 days → +2 points
# - Last Activity < 10 days → +0 points
# 
# The maximum possible risk score is 9.

# ### 10.2 Calculate the Risk Score for Every Customer
# 
# The risk score is calculated separately for each customer.
# 
# The score starts at zero. Points are then added according to the customer's satisfaction, complaint count, and number of days since their last activity.

# ### Code

# In[24]:


for customer in customers:

    risk_score = 0

    # Satisfaction points
    if customer["Satisfaction"] <= 2:
        risk_score += 3
    elif customer["Satisfaction"] == 3:
        risk_score += 2

    # Complaints points
    if customer["Complaints"] >= 4:
        risk_score += 3
    elif customer["Complaints"] >= 2:
        risk_score += 2

    # Inactivity points
    if customer["Last_Activity"] >= 20:
        risk_score += 3
    elif customer["Last_Activity"] >= 10:
        risk_score += 2

    print(customer["Customer_ID"], "→ Risk Score:", risk_score)


# ### 10.3 Assign Risk Level from the Score
# 
# The numerical risk score is converted into a risk level.
# 
# The classification is:
# 
# - **0–2 points:** Low Risk
# - **3–5 points:** Medium Risk
# - **6–9 points:** High Risk

# ### Code

# In[25]:


for customer in customers:

    risk_score = 0

    # Satisfaction points
    if customer["Satisfaction"] <= 2:
        risk_score += 3
    elif customer["Satisfaction"] == 3:
        risk_score += 2

    # Complaints points
    if customer["Complaints"] >= 4:
        risk_score += 3
    elif customer["Complaints"] >= 2:
        risk_score += 2

    # Inactivity points
    if customer["Last_Activity"] >= 20:
        risk_score += 3
    elif customer["Last_Activity"] >= 10:
        risk_score += 2

    # Risk level
    if risk_score >= 6:
        risk_level = "High"
    elif risk_score >= 3:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    print(customer["Customer_ID"], "→", risk_score, "→", risk_level)


# ### Interpretation
# 
# The scoring system identifies several customers with high risk scores.
# 
# Customers with a score of 6 or more are classified as High Risk because they have accumulated multiple warning points from low satisfaction, complaints, and/or prolonged inactivity.
# 
# Customers with scores between 0 and 2 are classified as Low Risk under the project's scoring rules.
# 
# This score provides a simple way to compare the relative level of churn-related warning signals across customers.

# ### 10.4 Five Highest-Risk Customers
# 
# The customers are ranked according to their numerical risk scores.
# 
# The five highest-risk customers are identified by selecting the customers with the highest scores.
# 
# There are four customers tied at the maximum score of 9. The next highest score is 8, belonging to C001.

# ### Code

# In[26]:


risk_scores = []

for customer in customers:

    risk_score = 0

    if customer["Satisfaction"] <= 2:
        risk_score += 3
    elif customer["Satisfaction"] == 3:
        risk_score += 2

    if customer["Complaints"] >= 4:
        risk_score += 3
    elif customer["Complaints"] >= 2:
        risk_score += 2

    if customer["Last_Activity"] >= 20:
        risk_score += 3
    elif customer["Last_Activity"] >= 10:
        risk_score += 2

    risk_scores.append((customer["Customer_ID"], risk_score))

first_score = 9
second_score = 8

print("Five Highest-Risk Customers:")

count = 0

for customer_id, score in risk_scores:
    if score == first_score or score == second_score:
        print(customer_id, "→", score)
        count += 1

        if count == 5:
            break


# ### Interpretation
# 
# The five highest-risk customers are C006, C009, C011, C016, and C001.
# 
# Four of these customers have the maximum risk score of 9, while C001 has a score of 8.
# 
# These customers have the strongest combinations of churn-related warning signals under the project's risk-scoring system.

# ## 11. Customer Segmentation
# 
# ### 11.1 Segment Customers by Risk Level
# 
# Customer segmentation involves grouping customers based on shared characteristics.
# 
# For this project, customers are segmented according to their churn risk level.
# 
# The risk levels are:
# 
# - High Risk
# - Medium Risk
# - Low Risk
# 
# The numerical risk score developed in Section 10 is used to determine each customer's risk level.

# ### Code

# In[27]:


high_risk_customers = []
medium_risk_customers = []
low_risk_customers = []

for customer in customers:

    risk_score = 0

    # Satisfaction points
    if customer["Satisfaction"] <= 2:
        risk_score += 3
    elif customer["Satisfaction"] == 3:
        risk_score += 2

    # Complaints points
    if customer["Complaints"] >= 4:
        risk_score += 3
    elif customer["Complaints"] >= 2:
        risk_score += 2

    # Inactivity points
    if customer["Last_Activity"] >= 20:
        risk_score += 3
    elif customer["Last_Activity"] >= 10:
        risk_score += 2

    # Segment customer
    if risk_score >= 6:
        high_risk_customers.append(customer["Customer_ID"])
    elif risk_score >= 3:
        medium_risk_customers.append(customer["Customer_ID"])
    else:
        low_risk_customers.append(customer["Customer_ID"])

print("High-Risk Customers:", high_risk_customers)
print("Medium-Risk Customers:", medium_risk_customers)
print("Low-Risk Customers:", low_risk_customers)


# ### 11.2 Number of Customers in Each Segment
# 
# The number of customers in each risk segment is counted to provide an overall view of the customer risk distribution.

# ### Code

# In[28]:


print("High-Risk Customers:", len(high_risk_customers))
print("Medium-Risk Customers:", len(medium_risk_customers))
print("Low-Risk Customers:", len(low_risk_customers))


# ### 11.3 Segment Summary
# 
# The risk-based segmentation classifies 10 customers as High Risk, 1 customer as Medium Risk, and 9 customers as Low Risk.
# 
# The High Risk group contains customers with risk scores between 6 and 9.
# 
# The Medium Risk group contains customers with risk scores between 3 and 5.
# 
# The Low Risk group contains customers with risk scores between 0 and 2.
# 
# This segmentation provides a simple way to identify customers who may require different levels of attention based on the warning signals present in their data.

# ### Interpretation
# 
# The High Risk segment contains 10 customers.
# 
# These customers have risk scores of 6 or more based on combinations of satisfaction, complaints, and inactivity.
# 
# They represent the customers with the strongest combination of churn-related warning signals under the project's scoring system.
# 
# AfriConnect can use this group as a priority segment for further investigation and appropriate customer-retention actions.

# ### Code

# In[29]:


print("High-Risk Customer IDs:")

for customer_id in high_risk_customers:
    print(customer_id)


# ### Interpretation
# 
# The high-risk segment contains eight customers.
# 
# These customers have accumulated high risk scores because of combinations of low satisfaction, complaints, and prolonged inactivity.
# 
# This segment provides AfriConnect with a focused group for further investigation and possible retention action.

# ## 12. Key Findings
# 
# ### 12.1 Overall Churn
# 
# The dataset contains 20 customers, of which 8 have churned and 12 have been retained.
# 
# This gives a churn rate of 40%.
# 
# The result shows that a significant portion of the customers in the sample have churned.

# ### 12.2 Satisfaction and Complaints
# 
# The analysis shows a difference between churned and retained customers in terms of satisfaction and complaints.
# 
# Churned customers generally recorded lower satisfaction levels and a higher number of complaints compared with retained customers.
# 
# This suggests an association between lower satisfaction, higher complaints, and churn in this sample.

# ### 12.3 Customer Tenure
# 
# The analysis also shows a difference in average tenure between churned and retained customers.
# 
# Churned customers generally had shorter customer tenure, while retained customers had longer tenure.
# 
# This suggests that newer customers may require additional attention during the early stages of their relationship with the company.

# ### 12.4 Customer Inactivity
# 
# Several customers had been inactive for more than 15 days.
# 
# Long periods of inactivity were observed particularly among customers showing other churn-related warning signals.
# 
# This suggests that prolonged inactivity can be useful as an early warning indicator when monitoring potential churn.

# ### 12.5 High-Risk Customers
# 
# The risk-scoring system classified 10 customers as High Risk, 1 customer as Medium Risk, and 9 customers as Low Risk.
# 
# The High Risk customers are:
# 
# C001, C003, C006, C009, C010, C011, C014, C016, C018, and C020.
# 
# These customers recorded risk scores of 6 or more based on the project's scoring rules.
# 
# The High Risk group therefore represents the customers with the strongest combination of churn-related warning signals in the dataset.

# ### 12.6 Main Findings Summary
# 
# The major findings from the analysis are:
# 
# 1. The dataset contains a 40% churn rate, with 8 out of 20 customers having churned.
# 
# 2. Churned customers generally showed lower satisfaction than retained customers.
# 
# 3. Churned customers generally recorded more complaints than retained customers.
# 
# 4. Churned customers generally had shorter tenure than retained customers.
# 
# 5. Prolonged inactivity appears to be an important warning signal for potential churn.
# 
# 6. The risk-scoring system classified 10 customers as High Risk, 1 as Medium Risk, and 9 as Low Risk.
# 
# 7. Several high-risk customers displayed multiple churn-related warning signals at the same time.
# 
# Overall, the analysis suggests that customer satisfaction, complaints, tenure, and recent activity are useful factors for monitoring churn risk in this sample.

# ## 13. Business Recommendations
# 
# ### 13.1 Prioritize High-Risk Customers
# 
# The risk-scoring analysis identified 10 customers as High Risk.
# 
# AfriConnect should prioritize these customers for proactive customer-retention activities. The company can review their recent activity, satisfaction levels, and complaint history to understand the specific issues affecting them.
# 
# This approach allows AfriConnect to focus its retention efforts on customers showing the strongest combination of churn-related warning signals.
# 
# ### Expected Business Impact
# 
# Prioritizing these customers can help AfriConnect focus retention resources on customers showing the strongest combination of churn-related warning signals.

# ### 13.2 Improve Customer Service and Resolve Complaints
# 
# The analysis shows that churned customers generally recorded more complaints than retained customers.
# 
# AfriConnect should investigate recurring customer complaints and improve the process for resolving them.
# 
# Customers with frequent complaints, especially those also identified as High Risk, should receive timely customer-service attention.
# 
# This may help reduce dissatisfaction and improve the overall customer experience.
# 
# ### Expected Business Impact
# 
# Faster and more effective complaint resolution may improve customer satisfaction and help reduce customer loss.

# ### 13.3 Monitor Inactivity and Re-engage Customers
# 
# The analysis identified prolonged inactivity as an important churn-related warning signal.
# 
# AfriConnect should monitor customers who have not recently interacted with the service and identify those showing extended periods of inactivity.
# 
# The company can then use appropriate engagement activities to reconnect with these customers before their inactivity develops into customer loss.
# 
# Customers who are both inactive and High Risk should receive greater priority.
# 
# ### Expected Business Impact
# 
# Early re-engagement may help AfriConnect identify customers whose behaviour is changing before they leave the service.

# ### 13.4 Recommendation Summary
# 
# Based on the analysis, AfriConnect should:
# 
# 1. Prioritize High-Risk customers for proactive retention activities.
# 
# 2. Investigate and resolve recurring customer complaints to improve customer satisfaction.
# 
# 3. Monitor prolonged customer inactivity and use appropriate re-engagement activities to reduce the possibility of churn.
# 
# These recommendations connect the identified customer-risk signals to practical business actions.

# ## 14. Limitations
# 
# ### 14.1 Small Dataset
# 
# The analysis was performed using a sample of only 20 customers.
# 
# Because the dataset is small, the findings may not fully represent the behaviour of a larger customer population.
# 
# The results should therefore be interpreted as findings from this sample rather than conclusions about all AfriConnect customers.

# ### 14.2 Rule-Based Risk System
# 
# The risk classification in this project is based on manually defined rules and a simple scoring system.
# 
# It is not a machine-learning model and does not produce a statistical probability of churn.
# 
# Therefore, the risk levels should be treated as indicators of potential churn risk rather than guaranteed predictions of which customers will leave.

# ### 14.3 Limited Variables
# 
# The Version 1 dataset contains a limited number of customer attributes, including age, tenure, monthly charge, complaints, support calls, satisfaction, last activity, and churn status.
# 
# A real telecommunications dataset would normally contain many more variables that could provide additional information about customer behaviour.
# 
# Therefore, the factors considered in this project do not represent every possible reason why a customer may churn.

# ### 14.4 No External Data Import
# 
# The dataset was created directly inside Python rather than imported from a real customer database or external CSV file.
# 
# This was intentional because external data importing has not yet been covered in this version of the project.
# 
# As a result, the analysis does not demonstrate how the system would handle a large real-world dataset.

# ### 14.5 No Machine Learning Evaluation
# 
# Because this project uses a rule-based system, machine-learning evaluation measures such as model accuracy, precision, recall, and F1-score were not calculated.
# 
# These measures would become relevant in a future version of the project after a machine-learning model is introduced.

# ### 14.6 Overall Limitation
# 
# The main limitation of this project is that it represents a simplified version of a customer churn analysis system.
# 
# Although the project successfully demonstrates data representation, analysis, segmentation, business rules, and risk classification, its findings should not be treated as definitive predictions of customer churn.
# 
# A larger and more realistic dataset, together with more advanced analytical and predictive techniques, would be required for a production-level system.

# ## 15. Future Improvements
# 
# ### 15.1 Use a Larger Dataset
# 
# A larger customer dataset could be used in a future version of the project.
# 
# The current analysis uses only 20 customers, so increasing the number of records would provide more data for identifying customer behaviour and churn patterns.
# 
# The same analysis logic could later be applied to thousands or more customer records.

# ### 15.2 Import Data from CSV Files
# 
# In a future version, the dataset could be stored in a CSV file and imported into Python.
# 
# This would make it easier to work with larger datasets without manually entering every customer record into the program.
# 
# Python's built-in csv module could be used when CSV handling is introduced.

# ### 15.3 Use Pandas for Larger-Scale Analysis
# 
# After learning pandas, the project could be upgraded to use DataFrames for more efficient data analysis.
# 
# Pandas would make it easier to filter, summarize, compare, and analyze larger datasets.

# ### 15.4 Introduce Machine Learning
# 
# A future version could replace the rule-based risk system with a machine-learning model.
# 
# The model could learn patterns from historical customer data and estimate the probability that a customer will churn.
# 
# Customers could then be assigned risk levels based on their estimated churn probability.
# 
# This would make the system more suitable for predictive analysis.

# ### 15.5 Improve Customer Segmentation
# 
# Future versions could create more detailed customer segments using additional customer characteristics.
# 
# For example, customers could be grouped according to their tenure, engagement, satisfaction, complaints, and other relevant behavioural factors.
# 
# This would allow AfriConnect to develop more targeted retention strategies for different customer groups.

# ### 15.6 Add Visualizations and Dashboards
# 
# Future versions could include charts and dashboards to make the findings easier to understand.
# 
# Visualizations could be used to show churn rates, customer risk distribution, satisfaction levels, complaints, and other important customer patterns.
# 
# A dashboard would make the results more accessible to business decision-makers.

# ### 15.7 Overall Future Direction
# 
# The current project provides a foundation for a more advanced customer churn system.
# 
# Future development can progress from a manually created dataset and rule-based risk scoring system to larger datasets, automated data processing, advanced analysis, and machine-learning-based churn prediction.
# 
# The goal would be to develop a more scalable system that can provide reliable churn insights and support targeted customer-retention decisions.

# ## 16. Conclusion
# 
# This project developed a simple Python-based customer churn risk analysis system for AfriConnect Telecom.
# 
# Using a dataset of 20 customers, the project analyzed customer information, examined churn patterns, identified important churn-related warning signals, calculated risk scores, and classified customers into different risk levels.
# 
# The analysis showed that 8 out of 20 customers had churned, giving a churn rate of 40%. Churned customers generally showed lower satisfaction, more complaints, shorter tenure, and longer periods of inactivity compared with retained customers.
# 
# A rule-based risk scoring system was then used to identify customers showing stronger combinations of churn-related warning signals. The customers were classified into High, Medium, and Low risk groups, with 10 customers classified as High Risk, 1 as Medium Risk, and 9 as Low Risk.
# 
# Based on these findings, recommendations were made to help AfriConnect prioritize high-risk customers, improve complaint resolution, and monitor customer inactivity.
# 
# Although this project uses a small dataset and a rule-based approach, it provides a foundation for developing a more advanced customer retention system in the future. Larger datasets, automated data processing, and machine-learning techniques could later be introduced to improve the system.
# 
# Overall, the project demonstrates how Python can be used to transform customer data into useful insights that can support customer-retention decisions.
