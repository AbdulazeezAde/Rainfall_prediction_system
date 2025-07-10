import streamlit as st
import sklearn
import joblib
 
# with open("rainfall_prediction.pkl", "rb") as file:
#     loaded_model = pickle.load(file)

model = joblib.load(r"rainfall_prediction")

st.title("Rainfall Prediction App")

st.write("This model is to predict the occurence of rainfall using some features such as pressure, humidity, temperature etc.")

day = st.slider("day", min_value=1, max_value= 30)
pressure = st.number_input("pressure")
temperature = st.number_input("maxtemp")
dew_point = st.number_input("dewpoint")
humidity = st.number_input("humidity")
cloud = st.number_input("cloud")
sunshine = st.number_input("sunshine")
wind_direction = st.number_input("wind_direction")
wind_speed = st.number_input("wind_speed")


if st.button("Predict"):
    prediction = model.predict([[day, pressure, temperature, dew_point, humidity, cloud, sunshine, wind_direction, wind_speed]])
    st.balloons()
    st.success("Rainfall" if prediction[0] == 1 else "No Rainfall")
