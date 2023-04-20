import pickle
import pandas as pd
import streamlit as st


# encoding Gender
with open('data/ML/pkl/encodingGender.pkl', 'rb') as gender:
    encoding_gender = pickle.load(gender)

# encoding Multiple Lines 
with open('data/ML/pkl/encodingMultiple Lines.pkl', 'rb') as multiple_lines:
    encoding_multiple_lines = pickle.load(multiple_lines)

# encoding Streaming TV 
with open('data/ML/pkl/encodingStreaming TV.pkl', 'rb') as streaming_tv:
    encoding_streaming_tv = pickle.load(streaming_tv)

# encoding Streaming Movies
with open('data/ML/pkl/encodingStreaming Movies.pkl', 'rb') as streaming_movies:
    encoding_streaming_movies = pickle.load(streaming_movies)

# encoding Streaming Music
with open('data/ML/pkl/encodingStreaming Music.pkl', 'rb') as streaming_music:
    encoding_streaming_music = pickle.load(streaming_music)

# encoding Device Protection 
with open('data/ML/pkl/encodingDevice Protection Plan.pkl', 'rb') as protection:
    encoding_protection = pickle.load(protection)

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

#encoding Phone Service 
with open('data/ML/pkl/encodingPhone Service.pkl','rb') as phone_service:
    encoding_phone_service = pickle.load(phone_service)

# encoding map 

# encoding Contract

map_contract = {"Month-to-Month":  1, 
       "One Year": 0, "Two Year":0}

# encoding Offer
map_offer = {"Offer A":  0, "Offer B": 1,"Offer C":1,"Offer D":2,"Offer E":3, "None":4}


# Best Model 

with open('data/ML/pkl/mejor_modelo.pkl', 'rb') as modelo:
    modelo = pickle.load(modelo)




# We define functions to predict my churn probability

def user_input_features():
    married_ = st.sidebar.slider('Married', "Yes") 
    Phone_Service_ = st.sidebar.slider('Phone Service', "Yes") 
    Internet_Type_ = st.sidebar.slider('Internet Type', "Fiber Optic") 
    Online_Security_ = st.sidebar.slider('Online Security', "No") 
    Online_Backup_  = st.sidebar.slider('Online Backup', "Yes") 
    Devive_protection_plan_  = st.sidebar.slider('Device Protection Plan', "No") 
    Premium_Tech_Support_  = st.sidebar.slider('Premium Tech Support', "No") 
    Unlimited_Data_  = st.sidebar.slider('Unlimited Data', "No") 
    Paperless_Billing_ = st.sidebar.slider('Paperless Billing', "No") 
    Payment_Method_ = st.sidebar.slider('Payment Method', "Credit Card ")
    Gender_ = st.sidebar.slider('Gender', "Female")
    Multiple_Lines_ = st.sidebar.slider('Multiple Lines', "Yes")
    Streaming_TV_ = st.sidebar.slider('Streaming TV',"Yes" )
    Streaming_Music_  = st.sidebar.slider('Streaming Music', "No")
    Streaming_Movies_ = st.sidebar.slider('Streaming Movies', "No")
    Contract_  = st.sidebar.slider('Contract', "One Year")
    Offer_ = st.sidebar.slider('Offer', "None")
     

    data = {'Married': married_,
            'Phone Service': Phone_Service_,
            'Internet Type': Internet_Type_,
            'Online Security': Online_Security_,
            'Online Backup': Online_Backup_,
            'Device Protection Plan': Devive_protection_plan_,
            'Premium Tech Support': Premium_Tech_Support_,
            'Unlimited Data': Unlimited_Data_,
            'Paperless Billing': Paperless_Billing_,
            'Payment Method': Payment_Method_,
            'Gender': Gender_,
            'Multiple Lines': Multiple_Lines_,
            'Streaming TV': Streaming_TV_,
            'Streaming Music': Streaming_Music_,
            'Streaming Movies': Streaming_Movies_,
            'Contract': Contract_,
            'Offer': Offer_,
            }

    return pd.DataFrame(data, index=[0])



def prediction_churn (user_dataframe, modelo):
    predic = modelo.predict(user_dataframe)[0]
    
    prob = modelo.predict_proba(user_dataframe)
    
    return predic, prob