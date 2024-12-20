import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Price Prediction App")

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs')

Facing= st.selectbox('Facing',['West', 'South', 'North-East', 'East', 'North', 'South-East', 'South-West', 'North-West'])
bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['No_Bedroom'].unique().tolist())))
bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['No_Bathroom'].unique().tolist())))
balcony = st.selectbox('Balconies',sorted(df['No_Balcony'].unique().tolist()))
Corner_Property = st.selectbox('Corner Property',sorted(df['Corner_Property'].unique().tolist()))
furnishing_type = st.selectbox('Furnishing Type',sorted(df['Furnishing'].unique().tolist()))
servant_room = float(st.selectbox('servant room',[0.0, 1.0]))
store_room = float(st.selectbox('store Room',[0.0, 1.0]))
pooja_room = float(st.selectbox('pooja room',[0.0, 1.0]))
study_room = float(st.selectbox('study room',[0.0, 1.0]))
Overlooking_main_road = float(st.selectbox('Overlooking_main road',[0.0, 1.0]))
Overlooking_club = float(st.selectbox('Overlooking_club',[0.0, 1.0]))
Overlooking_pool = float(st.selectbox('Overlooking_pool',[0.0, 1.0]))
Overlooking_NA = float(st.selectbox('Overlooking_NA',[0.0, 1.0]))
property_age = st.selectbox('Property Age',sorted(df['flat_age'].unique().tolist()))
sector = st.selectbox('Sector',sorted(df['sector_num'].unique().tolist()))
Super_Built_up_Area = float(st.number_input('Super Built-up Area'))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    # form a dataframe
    data = [[ Facing, bedrooms, bathroom, balcony, Corner_Property, furnishing_type, servant_room, store_room, pooja_room, study_room, Overlooking_main_road, Overlooking_club, Overlooking_pool, Overlooking_NA, property_age, sector,  Super_Built_up_Area, luxury_category, floor_category ]]
    columns = ['Facing', 'No_Bedroom', 'No_Bathroom', 'No_Balcony', 'Corner_Property',
       'Furnishing', 'study room', 'servant room', 'store room', 'pooja room',
       'Overlooking_main road', 'Overlooking_club', 'Overlooking_pool',
       'Overlooking_NA', 'flat_age', 'sector_num', 'Super Built-up Area',
       'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.15
    high = base_price + 0.15

    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))