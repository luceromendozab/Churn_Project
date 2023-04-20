import streamlit as st
from src import soporte as sp


st.image("../images/churn1.jpeg")

st.header("Real Time  Prediction")
st.subheader("Optimize Your Profitability")
st.subheader("Will your customers stay or leave? Find out now!")

####################################

chest = pd.DataFrame(sp.encoding_chestpain.transform(df_resultados[["ChestPainType"]]), columns= ["ChestPainType"])
angina = pd.DataFrame(sp.encoding_angina.transform(df_resultados[["ExerciseAngina"]]), columns= ["ExerciseAngina"])
resting = pd.DataFrame(sp.encoding_resting.transform(df_resultados[["RestingECG"]]), columns= ["RestingECG"])
slope = pd.DataFrame(sp.encoding_slope.transform(df_resultados[["ST_Slope"]]), columns= ["ST_Slope"])
fasting = pd.DataFrame(sp.encoding_fasting.transform(df_resultados[["FastingBS"]]), columns= ["FastingBS"])
sex = pd.DataFrame(encoding_sex.transform(df_resultados[["Sex"]]).toarray(), columns=["Sex_F", "Sex_M"])

df_final = pd.concat([estandarizadas, sex, chest, angina, resting, slope, fasting], axis = 1)


user_options = sp.user_input_features()


pred, prob = prediction_churn (df_final, sp.modelo)

st.write(f"The prediction is : {pred}")
st.write(f"The probability is : {prob}")
