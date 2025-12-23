import streamlit as st
import pickle
import pandas as pd

model=pickle.load(open("pkl_files/model.pkl", "rb"))
poly_features=pickle.load(open("pkl_files/poly_features.pkl", "rb"))

st.title("☀️ Advanced Solar Power Predictor")

st.write("**Irradiation:** The intensity of sunlight hitting a specific area at a specific time.")
st.write("**Ambient Temperature:** The temperature of the surrounding air (the outside temperature you see on a weather app).")
st.write("**Module Temperature:** The actual temperature of the solar panel surface (the module).")

#Sliders
st.sidebar.header("Input Weather Data")
amb_temp = st.sidebar.slider("Ambient Temperature (°C)", 10.0, 50.0, 25.0)
mod_temp = st.sidebar.slider("Module Temperature (°C)", 10.0, 75.0, 35.0)
irradiation = st.sidebar.slider("Irradiation", 0.0, 1.5, 0.5)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)

#order must be same as in notebook
input_df = pd.DataFrame([[amb_temp, mod_temp, irradiation, hour]], 
                        columns=["AMBIENT_TEMPERATURE","MODULE_TEMPERATURE","IRRADIATION","HOUR"])

if st.sidebar.button("Predict"):
    input_poly = poly_features.transform(input_df)
    prediction = model.predict(input_poly)[0]
    #UI
    st.subheader("Results")
    final_output = max(0, prediction)
    st.metric(label="Predicted DC Power", value=f"{final_output:.2f} kW")
    
    #Difference between Ambient and Module
    temp_diff = mod_temp - amb_temp
    st.write(f"Note: Your panels are **{temp_diff:.1f}°C** hotter than the air.")