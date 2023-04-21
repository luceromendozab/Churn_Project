import streamlit as st
from src import soporte as sp
import pandas as pd

st.image("images/churn1.jpeg")

st.header("Real Time  Prediction")
st.subheader("Optimize Your Profitability")
st.subheader("Will your customers stay or leave? Find out now!")

####################################

user_options = sp.user_input_features()
st.dataframe(user_options)


married_ = pd.DataFrame(sp.encoding_married.transform(user_options[["Married"]]), columns= ["Married"])
Phone_Service_= pd.DataFrame(sp.encoding_phone_service.transform(user_options[["Phone Service"]]), columns= ["Phone Service"])
Internet_Type_ = pd.DataFrame(sp.encoding_internet_type.transform(user_options[["Internet Type"]]), columns= ["Internet Type"])
Online_Security_  = pd.DataFrame(sp.encoding_online_security.transform(user_options[["Online Security"]]), columns= ["Online Security"])
Online_Backup_= pd.DataFrame(sp.encoding_online_backup.transform(user_options[["Online Backup"]]), columns= ["Online Backup"])
Devive_protection_plan_  = pd.DataFrame(sp.encoding_protection.transform(user_options[["Device Protection Plan"]]), columns= ["Device Protection Plan"])
Premium_Tech_Support_  = pd.DataFrame(sp.encoding_premium_support.transform(user_options[["Premium Tech Support"]]), columns= ["Premium Tech Support"])
Unlimited_Data_ = pd.DataFrame(sp.encoding_unlimited_data.transform(user_options[["Unlimited Data"]]), columns= ["Unlimited Data"])
Paperless_Billing_  = pd.DataFrame(sp.encoding_paperless.transform(user_options[["Paperless Billing"]]), columns= ["Paperless Billing"])
Payment_Method_ = pd.DataFrame(sp.encoding_payment_method.transform(user_options[["Payment Method"]]), columns= ["Payment Method"])
Gender_ = pd.DataFrame(sp.encoding_gender.transform(user_options[["Gender"]]).toarray(), columns= ["Gender_Female","Gender_Male"])
Multiple_Lines_  = pd.DataFrame(sp.encoding_multiple_lines.transform(user_options[["Multiple Lines"]]).toarray(), columns= ["Multiple Lines_No","Multiple Lines_Yes"])
Streaming_TV_= pd.DataFrame(sp.encoding_streaming_tv.transform(user_options[["Streaming TV"]]).toarray(), columns= ["Streaming TV_No","Streaming TV_Yes"])
Streaming_Music_ = pd.DataFrame(sp.encoding_streaming_music.transform(user_options[["Streaming Music"]]).toarray(), columns= ["Streaming Music_No","Streaming Music_Yes"])
Streaming_Movies_  = pd.DataFrame(sp.encoding_streaming_movies.transform(user_options[["Streaming Movies"]]).toarray(), columns= ["Streaming Movies_No","Streaming Movies_Yes"])

user_options["Contract_mapeada"]= user_options["Contract"].map(sp.map_contract)
user_options["Offer_mapeada"]= user_options["Offer"].map(sp.map_offer)

user_options.drop(["Offer","Contract","Internet Type","Married","Phone Service","Online Security","Online Backup","Device Protection Plan","Premium Tech Support","Unlimited Data","Paperless Billing","Payment Method","Gender","Multiple Lines","Streaming TV","Streaming Music","Streaming Movies"], axis=1, inplace=True)
df_final = pd.concat([user_options, married_,Phone_Service_,Internet_Type_,Online_Security_,Online_Backup_,Devive_protection_plan_,Premium_Tech_Support_,Unlimited_Data_,Paperless_Billing_,Payment_Method_,Gender_,Multiple_Lines_,Streaming_TV_,Streaming_Music_,Streaming_Movies_], axis = 1)
print(df_final.shape)

nuevo_orden=['Age', 'Married', 'Number of Dependents', 'Number of Referrals',
       'Phone Service', 'Internet Type', 'Avg Monthly GB Download',
       'Online Security', 'Online Backup', 'Device Protection Plan',
       'Premium Tech Support', 'Unlimited Data', 'Paperless Billing',
       'Payment Method', 'Total Revenue', 'Satisfaction Score',
       'CLTV', 'Gender_Female', 'Gender_Male', 'Multiple Lines_No',
       'Multiple Lines_Yes', 'Streaming TV_No', 'Streaming TV_Yes',
       'Streaming Music_No', 'Streaming Music_Yes', 'Streaming Movies_No',
       'Streaming Movies_Yes', 'Contract_mapeada', 'Offer_mapeada']

df_final=df_final.reindex(columns=nuevo_orden)
st.dataframe(df_final)


pred, prob = sp.prediction_churn (df_final, sp.modelo)

st.write(f"The prediction is : {pred}")
st.write(f"The probability is : {prob}")
