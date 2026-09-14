#!/usr/bin/env python
# coding: utf-8

# ## Customers Dataset

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

