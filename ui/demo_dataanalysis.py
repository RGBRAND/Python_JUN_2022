
# streamlit run ui\demo_dataanalysis.py
# use Clt+J 


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns 
# import dtale as dt

@st.cache
def load_dataset():
    df = pd.read_excel('ui/Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=20,
            skipfooter=2)
    return preprocess(df)


def preprocess(df):
    #step 1
    cols_to_drop= ['Type','Coverage','AREA','REG','DEV']  # for removing columns
    df.drop(columns=cols_to_drop, inplace=True) 

    #Steap 2: rename column
    df.rename({'OdName':'Country',
        'AreaName':'Continent',
        'RegName':'Region',
        'DevName':'Status',}, axis=1, inplace=True)
    
    #step3 col as string
    df.columns = df.columns.astype(str)

    #step 4 : add a total column
    year = list(map(str, range(1980,2014)))
    df['Total'] = df[year].sum(axis=1)

    # step 5: set country as index
    df.set_index('Country', inplace=True)
    return df 



# loading the data 
canadadf = load_dataset()

st.header("Canada Immigration data analysis of 30 Years")

if st.checkbox("View Raw Datasheet"):
    st.write(canadadf)


menu_choices = ['Vosualize Country Immigrats', 'Compare Contries', 'About']
choice = st.sidebar.radio('Select an option from the menu', menu_choices)       # we can use selectbox insted of radio

if choice == menu_choices[0]:
    country_list = canadadf.index.to_list()
    country = st.selectbox('Select a country', country_list)
    graph = st.radio('Select a Graph',['Bar Chart','Line Chart', 'Area Chart'],horizontal=True) #horizontal=True for show radio horozontaly
    years = list(map(str,range(1980,2013)))
    data = canadadf.loc[country, years]

    if graph == 'Bar Chart':
        st.bar_chart(data)
    elif graph == 'Line Chart':
        st.line_chart(data)
    elif graph == 'Area Chart':
        st.area_chart(data)


    st.table(data)          # to show data in table , if want to see only graph the remove st.table(data) 


elif choice == menu_choices[1]:
    country_list = canadadf.index.to_list()
    countries = st.multiselect('Select a country', country_list)
    years = list(map(str,range(1980,2013)))
    graph = st.radio('Select a Graph',['Bar Chart','Line Chart', 'Area Chart'],horizontal=True)
    if not len(countries)>= 1:
        st.warning("Please select at least one country")
    else:
        data = canadadf.loc[countries, years].T
        if graph == 'Bar Chart':
            fig = px.bar(data, x = years, y=countries, title="Comparing Countries")
        elif graph == 'Line Chart':
            fig = px.line(data, x = years, y=countries, title="Comparing Countries")
            st.plotly_chart(fig)
        elif graph == 'Area Chart':
            fig = px.area(data, x = years, y=countries, title="Comparing Countries")
       

    
else:
    st.header("About")
    st.markdown('''### This is the data ananalysis aap for the Canada
    - This is from United Nation
    - It's from year 1980 to 2013
    - It contains 195 Countries''')