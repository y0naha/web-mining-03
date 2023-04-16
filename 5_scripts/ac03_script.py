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

df = pd.read_csv('../2_bases_tratadas/base_tratada.csv', delimiter=',')
df = df.drop(df.columns[0], axis=1)
df.rename(columns={'nome': 'Nome do jogo', 'porcentagem_desconto':'Desconto (%)', 'preco':'Preço (R$)', 'tipo':'Categoria', 'sistema':'Sistema', 'plataforma':'Plataforma'}, inplace=True)

palavra_chave = st.sidebar.text_input('Buscar o nome do jogo ou palavra-chave:')

if palavra_chave:
    df_filtrado = df.loc[df['Nome do jogo'].str.contains(palavra_chave, case=False)]
else:
    plataforma = st.sidebar.selectbox('Selecione a plataforma:', ['PC', 'Console', 'Mobile'])

    if plataforma == 'PC':
        df_filtrado = df.loc[df['Plataforma'] == 'pc']
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['steam,windows','windows', 'steam,mac', 'steam,linux'])
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'] == sistema]
    elif plataforma == 'Console':
        df_filtrado = df.loc[df['Plataforma'] == 'console']
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['nintendo', 'playstation', 'xbox'])
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'] == sistema]
    else:
        df_filtrado = df.loc[df['Plataforma'] == 'mobile']
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['android', 'ios'])
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'] == sistema]

st.write(df_filtrado)

