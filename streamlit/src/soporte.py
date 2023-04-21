import pickle
import pandas as pd
import streamlit as st


# encoding Gender
with open('../data/ML/pkl/encodingGender.pkl', 'rb') as gender:
    encoding_gender = pickle.load(gender)

# encoding Multiple Lines 
with open('../data/ML/pkl/encodingMultiple Lines.pkl', 'rb') as multiple_lines:
    encoding_multiple_lines = pickle.load(multiple_lines)

# encoding Streaming TV 
with open('../data/ML/pkl/encodingStreaming TV.pkl', 'rb') as streaming_tv:
    encoding_streaming_tv = pickle.load(streaming_tv)

# encoding Streaming Movies
with open('../data/ML/pkl/encodingStreaming Movies.pkl', 'rb') as streaming_movies:
    encoding_streaming_movies = pickle.load(streaming_movies)

# encoding Streaming Music
with open('../data/ML/pkl/encodingStreaming Music.pkl', 'rb') as streaming_music:
    encoding_streaming_music = pickle.load(streaming_music)

# encoding Device Protection 
with open('../data/ML/pkl/encodingDevice Protection Plan.pkl', 'rb') as protection:
    encoding_protection = pickle.load(protection)

# encoding Internet Type
with open('../data/ML/pkl/encodingInternet Type.pkl', 'rb') as internet_type:
    encoding_internet_type = pickle.load(internet_type)

#encoding Married
with open('../data/ML/pkl/encodingMarried.pkl', 'rb') as married:
    encoding_married = pickle.load(married)

#encoding Online Backup
with open('../data/ML/pkl/encodingOnline Backup.pkl', 'rb') as online_backup:
    encoding_online_backup = pickle.load(online_backup)

#encoding Online Security
with open('../data/ML/pkl/encodingOnline Security.pkl', 'rb') as online_security:
    encoding_online_security = pickle.load(online_security)

#encoding Paperless Billing
with open('../data/ML/pkl/encodingPaperless Billing.pkl', 'rb') as paperless:
    encoding_paperless = pickle.load(paperless)

#encoding Payment Method
with open('../data/ML/pkl/encodingPayment Method.pkl', 'rb') as payment:
    encoding_payment_method= pickle.load(payment)

#encoding Premium Tech Support 
with open('../data/ML/pkl/encodingPremium Tech Support.pkl', 'rb') as premium_support:
    encoding_premium_support = pickle.load(premium_support)

#encoding Unlimited Data
with open('../data/ML/pkl/encodingUnlimited Data.pkl','rb') as unlimited_data:
    encoding_unlimited_data = pickle.load(unlimited_data)

#encoding Phone Service 
with open('../data/ML/pkl/encodingPhone Service.pkl','rb') as phone_service:
    encoding_phone_service = pickle.load(phone_service)

# encoding map 

# encoding Contract

map_contract = {"Month-to-Month":  1, 
       "One Year": 0, "Two Year":0}

# encoding Offer
map_offer = {"Offer A":  0, "Offer B": 1,"Offer C":1,"Offer D":2,"Offer E":3, "None":4}



# Best Model 

with open('../data/ML/pkl/mejor_modelo.pkl', 'rb') as modelo:
    modelo = pickle.load(modelo)




# We define functions to predict my churn probability

def user_input_features():
    # encoding 
    married_ = st.selectbox('Married',("Yes","No") ) 
    Phone_Service_ = st.selectbox('Phone Service', ("Yes","No")) 
    Internet_Type_ = st.selectbox('Internet Type', ("Fiber Optic","DSL","None","Cable")) 
    Online_Security_ = st.selectbox('Online Security', ("Yes","No")) 
    Online_Backup_  = st.selectbox('Online Backup', ("Yes","No")) 
    Devive_protection_plan_  = st.selectbox('Device Protection Plan', ("No","Yes")) 
    Premium_Tech_Support_  = st.selectbox('Premium Tech Support', ("Yes","No")) 
    Unlimited_Data_  = st.selectbox('Unlimited Data', ("No","Yes")) 
    Paperless_Billing_ = st.selectbox('Paperless Billing', ("Yes","No")) 
    Payment_Method_ = st.selectbox('Payment Method', ("Credit Card","Mailed Check","Bank Withdrawal" ))
    Gender_ = st.selectbox('Gender', ("Female","Male"))
    Multiple_Lines_ = st.selectbox('Multiple Lines', ("Yes","No"))
    Streaming_TV_ = st.selectbox('Streaming TV',("Yes","No"))
    Streaming_Music_  = st.selectbox('Streaming Music', ("Yes","No"))
    Streaming_Movies_ = st.selectbox('Streaming Movies', ("Yes","No"))
    Contract_  = st.selectbox('Contract', ("One Year","Two Year","Month-to-Month"))
    Offer_ = st.selectbox('Offer', ("None","Offer A","Offer B","Offer C","Offer D","Offer E"))

    #numeric 

    Age_ = st.sidebar.slider('Age', 18,80,45)
    Number_of_Dependents = st.sidebar.slider('Number of Dependents', 0,10,2)
    Number_of_Referrals = st.sidebar.slider('Number of Referrals', 0,15,0)
    Avg_Monthly_GB_Download = st.sidebar.slider('Avg Monthly GB Download', 0,100,17)
    Total_Revenue = st.sidebar.slider('Total Revenue', 20, 15000,1024)
    Satisfaction_Score = st.sidebar.slider('Satisfaction Score',1,5,2)
    CLTV = st.sidebar.slider('CLTV',2000,7000, 3026)
   

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
                        
            'Age': Age_,
            'Number of Dependents': Number_of_Dependents,
            'Number of Referrals': Number_of_Referrals,
            'Avg Monthly GB Download': Avg_Monthly_GB_Download,
            'Total Revenue': Total_Revenue,
            'Satisfaction Score': Satisfaction_Score,
            'CLTV': CLTV,
            }

    return pd.DataFrame(data, index=[0])



def prediction_churn (user_dataframe, modelo):
    predic = modelo.predict(user_dataframe)[0]
    
    prob = modelo.predict_proba(user_dataframe)
    
    return predic, prob