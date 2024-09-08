import pandas as pd
import streamlit as st
import sklearn as sk
import pickle

cars_df = pd.read_csv("./Cars_price.csv")

st.write(
    """
    # Cars24 used car price prediction
    """
)

st.dataframe(cars_df.head())

col1, col2 = st.columns(2)

fueltype = st.selectbox(
    "Select the fuel type",
    ["Diesel", "Petrol", "CNG", "LPG", "Electric"]
)

st.write("You selected:", fueltype)

engine = col1.slider("Set the engine power",
                   500, 5000, step=100)

transmission_type = col2.selectbox("Select the transmission type",
                                 ["Manual", "Automatic"])

seats = st.selectbox("Enter the number of seats",
                     [4, 5, 7, 9, 11])

#input_features = [[2018.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]

encode_dict = {
    "fueltype": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

def model_pred(fuel_type, transmission, engine, seats):

    ##load the model\
    with open("car_pred", 'rb') as file:
        reg_model = pickle.load(file)
        input_features = [[2018.0, 1, 4000, fueltype, \
                           transmission_type, 19.70, engine, 86.30, \
                           seats]]
        return reg_model.predict(input_features)

if (st.button("Predict Price")):

    fueltype = encode_dict['fueltype'][fueltype]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fueltype, transmission_type, engine, seats)

    st.text(f"The Price of the car is {price[0].round(2)} lakh rupees.")