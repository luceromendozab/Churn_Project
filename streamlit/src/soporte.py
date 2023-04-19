import pickle
import pandas as pd
import streamlit as st

# encoding Contract 
with open('data/ML/pkl/encodingContract.pkl', 'rb') as contract:
    encoding_contract = pickle.load(contract)

# encoding Device Protection 
with open('data/ML/pkl/encodingDevice Protection Plan.pkl', 'rb') as protection:
    encoding_protection = pickle.load(protection)

# encoding Gender
with open('data/ML/pkl/encodingGender.pkl', 'rb') as gender:
    encoding_gender = pickle.load(gender)

# encoding Internet Type
with open('data/ML/pkl/encodingGender.pkl', 'rb') as internet_type:
    encoding_internet_type = pickle.load(internet_type)

#encoding Married
with open('data/ML/pkl/encodingMarried.pkl', 'rb') as married:
    encoding_married = pickle.load(married)

#encoding Online Backup
with open('data/ML/pkl/encodingOnline Backup.pkl', 'rb') as online_backup:
    encoding_online_backup = pickle.load(online_backup)

#encoding Online Security
with open('data/ML/pkl/encodingOnline Security.pkl', 'rb') as online_security:
    encoding_online_security = pickle.load(online_security)

#encoding Paperless Billing
with open('data/ML/pkl/encodingPaperless Billing.pkl', 'rb') as paperless:
    encoding_paperless = pickle.load(paperless)

#encoding Payment Method
with open('data/ML/pkl/encodingPayment Method.pkl', 'rb') as payment:
    encoding_payment_method= pickle.load(payment)

#encoding Premium Tech Support 
with open('data/ML/pkl/encodingPremium Tech Support.pkl', 'rb') as premium_support:
    encoding_premium_support = pickle.load(premium_support)

#encoding Unlimited Data
with open('data/ML/pkl/encodingUnlimited Data.pkl','rb') as unlimited_data:
    encoding_unlimited_data = pickle.load(unlimited_data)

# Best Model 

with open('data/ML/pkl/mejor_modelo.pkl', 'rb') as modelo:
    modelo = pickle.load(modelo)

def user_input_features():
    







def prediction_churn (user_dataframe, modelo):
    predic = modelo.predict(user_dataframe)[0]
    
    prob = modelo.predict_proba(user_dataframe)
    
    return predic, prob