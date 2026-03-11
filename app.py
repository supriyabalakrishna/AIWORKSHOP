import streamlit as st
import pickle
import numpy as np

# page setup
st.set_page_config(page_title="Insurance Predictor", page_icon="💰", layout="wide")

# load model
model = pickle.load(open("model.pkl","rb"))

# title
st.title("💰 Medical Insurance Cost Predictor")
st.write("Fill the details below to estimate insurance cost")

st.divider()

# create two columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 65)
    sex = st.selectbox("Sex", ["female","male"])
    bmi = st.slider("BMI", 15.0, 45.0)

with col2:
    children = st.slider("Children",0,5)
    smoker = st.selectbox("Smoker",["no","yes"])
    region = st.selectbox("Region",["southwest","southeast","northwest","northeast"])

# encoding
sex = 1 if sex=="male" else 0
smoker = 1 if smoker=="yes" else 0

region_map = {
"southwest":0,
"southeast":1,
"northwest":2,
"northeast":3
}

region = region_map[region]

st.divider()

if st.button("Predict Insurance Cost 💰"):
    
    data = np.array([[age,sex,bmi,children,smoker,region]])
    
    prediction = model.predict(data)

    st.success(f"Estimated Cost: ${prediction[0]:,.2f}")