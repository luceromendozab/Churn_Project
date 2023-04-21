# Project on Churn in Telecommunications
## How to Enhance Customer Retention : A Case Study Analysis

![imagen](https://github.com/luceromendozab/Churn_Project/blob/main/images/churn_rate.jpeg)

This is a Churn analysis project for a telecommunications company in California. The company provides phone and internet services to its customers, and this project analyzes customer churn data as well as other factors that may influence it.

# Introduction
Churn refers to the rate at which customers stop doing business with a company, and is a critical metric for evaluating a company's performance. Understanding the factors that influence churn is crucial to developing strategies that retain customers and reduce losses.

We have also uploaded the data to a relational database using SQLalchemy for efficient data management and created a live demo of the churn prediction using the Streamlit web interface. Our goal is to provide the company with a comprehensive solution to improve customer retention and reduce churn.

# Objetives

- Develop a churn predictive model in Python using machine learning techniques to assist the company in retaining its customers and reducing losses.

- Create a live demo of the churn prediction using the Streamlit web interface, so that the company can visualize the results and take appropriate measures.

- Upload the project's data to a relational database to facilitate its management and use in future analyses.

# Data Sources

The telecommunications company data includes information on 7,043 customers in California during the third quarter of the year. The data contains customer demographic information, satisfaction scores, churn scores, and customer lifetime value (CLTV) values.

- [Kaggle Telco customer churn](https://www.kaggle.com/datasets/ylchang/telco-customer-churn-1113)

# Project structure
Data: This folder contains the data used in the project, including the raw data and the data uses in SQL,Machine Learing and Visualization. 

Notebooks: This folder contains Jupyter notebooks used for data analysis and the Machine Learning algorithms. 

SQL: Contains the relational model of our data and the insertion of data through SQLalchemy from Python.

![imagen](https://github.com/luceromendozab/Churn_Project/blob/main/SQL/relational%20model.png)

Visualization: [My Dashboard](https://public.tableau.com/app/profile/lucero.mendoza8271/viz/Churn_16817483435120/GlobalView?publish=yes) consists in 


# Conclusions and Solutions

Our churn predictive model achieved a high accuracy rate in identifying customers who are likely to churn. We identified several key factors that significantly impact churn, such as contract type, tenure, and internet service. The model also highlighted the importance of customer satisfaction in reducing churn.

Based on these findings, we recommend the following solutions to improve customer retention and reduce churn:

- Develop targeted marketing campaigns that focus on customers with a high likelihood of churn, offering personalized promotions and incentives.

- Improve customer satisfaction by addressing service quality issues, providing better customer support, and enhancing the overall customer experience.

- Offer flexible contract options that cater to the needs of different customer segments, such as month-to-month plans or annual contracts.

- Provide additional services and perks to loyal customers to increase their value and incentivize them to stay with the company.

# Tools Used
- Programming Language: Python

- Python Libraries:

    - Pandas: Used for manipulation and data analysis in the DataFrame containing diamond characteristics and prices.

    - NumPy: Used for matrix manipulation and numerical calculations in data preprocessing.

    - Matplotlib: Used for data visualization and distribution charts of variables.

    - Seaborn: Used for visualization of variable distributions and correlations between them.

    - Scikit-learn: Used for implementation of machine learning models, feature selection, and evaluation of model performance.

    - imblearn: Machine learning library that provides tools for handling and treating class imbalance problems in data sets. Over and under-sampling combination was used.

    - Pickle: Used for saving the final trained model and its subsequent use for making predictions on new data.

    -  Sqlalchemy: Provides a set of tools for working with databases through an object-oriented programming interface (API), which means that Python objects can be created to represent database tables, columns, and relationships between them.
    - 


- Visualization Tools:

    - Tableau:

- Data Analysis Tools:
    - SQL:

- Collaboration and Project Management Tools:

    - GitHub: