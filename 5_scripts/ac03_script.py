import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px

# nome da app
st.write(
    '''
    ***AC03 - Web Mining***
    '''
)

st.sidebar.header("Nuuvem database")

def get_data():
    path = '../2_bases_tratadas/base_tratada.csv'
    return pd.read_csv(path, sep=';')

df = get_data()

plataforma = ['PC', 'Console','Mobile']

escolha_da_plataforma = st.sidebar.selectbox("Escolha a plataforma", plataforma)

if escolha_da_plataforma == 'PC':
    stock_choice = df['']
