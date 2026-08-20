import numpy as np
import pandas as pd
import streamlit as st
import joblib
model = joblib.load(open('Water.pkl', 'rb'))

# Page configuration
st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon="💧",
    layout="centered"
)


st.title("💧 Water Potability Prediction")
st.write("Enter the water quality parameters to predict whether the water is potable.")

ph = st.number_input('Enter PH of water',min_value=0.0,max_value=14.0,step=0.1,value = None,placeholder='ph: 0.00 to 14.00' )

Hardness = st.number_input('Enter Hardness of water',min_value=47.43,max_value=323.12,step=0.1,value = None,placeholder='Hardness: 47.43 to 323.12' )

Solids = st.number_input('Enter Solids of water',min_value=320.94,max_value=61227.20,step=0.1,value = None,placeholder='Solids (TDS): 320.94 to 61,227.20' )

Chloramines = st.number_input('Enter Chloramines of water',min_value=0.35,max_value=13.13,step=0.1,value = None,placeholder='Chloramines: 0.35 to 13.13' )

Sulfate = st.number_input('Enter Sulfate of water',min_value=129.00,max_value=481.03,step=0.1,value = None,placeholder='Sulfate: 129.00 to 481.03' )

Conductivity = st.number_input('Enter Conductivity of water',min_value=181.48,max_value=753.34,step=0.1,value = None,placeholder='Conductivity: 181.48 to 753.34' )

Organic_carbon = st.number_input('Enter Organic carbon of water',min_value=2.20,max_value= 28.30,step=0.1,value = None,placeholder='Organic_carbon: 2.20 to 28.30' )

Trihalomethanes = st.number_input('Enter Trihalomethanes of water',min_value=0.74,max_value=124.00,step=0.1,value = None,placeholder='Trihalomethanes: 0.74 to 124.00' )

Turbidity = st.number_input('Enter Turbidity of water',min_value=1.45,max_value=6.74,step=0.1,value = None,placeholder='Turbidity: 1.45 to 6.74' )

if st.button('Predict'):
    input_data = pd.DataFrame({'ph':[ph],
                               'Hardness':[Hardness],
                               'Solids': [Solids],
                               'Chloramines':[Chloramines],
                               'Sulfate':[Sulfate],
                               'Conductivity':[Conductivity],
                               'Organic_carbon':[Organic_carbon],
                               'Trihalomethanes':[Trihalomethanes],
                               'Turbidity': [Turbidity]})
    pred = model.predict(input_data)[0]
    if pred == 1:
        st.write("The water is potable.")
    else:
        st.error("The water is not potable.")

