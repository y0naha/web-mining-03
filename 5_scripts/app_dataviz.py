import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px

# nome da app
st.write(
    '''
    ***Futebol Web App***
    '''
)

st.sidebar.header("Escolha os times")

def get_data():
    path = '../3_bases_uploud/gols.csv'
    return pd.read_csv(path, sep=';')

df = get_data()

df_data = df['anomes'].drop_duplicates()

min_data = min(df_data)
max_data = max(df_data)

indicador = ['temporal', 'específico']

escolha_do_indicador = st.sidebar.selectbox("Escolha o indicador", indicador)

if escolha_do_indicador=='temporal':
    stock = df['home_team_name'].drop_duplicates()
    stock_choice = st.sidebar.selectbox("Escolha um time", stock)

    start_date = st.sidebar.text_input("Digite uma data de inicio", min_data)
    end_date = st.sidebar.text_input("Digite uma data de fim", max_data)

    start = int(start_date)
    end = int(end_date)

    if start > end:
        st.error('A data final deve ser **MAIOR** que a data inicial')

    df = df[(df['home_team_name']==stock_choice)&(df['anomes']<=end)]
    df = df.set_index(df['anomes'].astype(str))

    ## criar grafico

    st.header('Time: ' + stock_choice_upper())
    st.write('Gols em casa')
    st.line_chart(df['gols'])

else:
    print('a') 