import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px

# Filtragem e carregamento da base de dados
df = pd.read_csv('2_bases_tratadas/base_tratada.csv', delimiter=',')
df = df.drop(df.columns[0], axis=1)
df.rename(columns={'nome': 'Nome do jogo', 'porcentagem_desconto':'Desconto (%)', 'preco':'Preço (R$)', 'tipo':'Categoria', 'sistema':'Sistema', 'plataforma':'Plataforma'}, inplace=True)

# Inicio da sidebar
st.sidebar.title("Nuuvem database ☁")
st.sidebar.caption("Atividade contínua para a faculdade Impacta.")
st.sidebar.caption("Veja o código base deste projeto [aqui](https://github.com/y0naha/web-mining-03).")
st.sidebar.markdown("---")


palavra_chave = st.sidebar.text_input('Buscar o nome do jogo ou palavra-chave:')


if palavra_chave:
    df_filtrado = df.loc[df['Nome do jogo'].str.contains(palavra_chave, case=False)]
else:
    plataforma = st.sidebar.selectbox('Selecione a plataforma:', ['PC', 'Console', 'Mobile'])

    if plataforma == 'PC':
        preco_min, preco_max = st.sidebar.slider('Selecione o intervalo de preço:', float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max()), (float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max())), step=100.0)
        df_filtrado = df[(df['Preço (R$)'] >= preco_min) & (df['Preço (R$)'] <= preco_max) & (df['Plataforma'] == 'pc')]
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['Steam','Windows', 'Mac', 'Linux'])
        sistema = sistema.lower()
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'].str.contains(sistema)]
    elif plataforma == 'Console':
        preco_min, preco_max = st.sidebar.slider('Selecione o intervalo de preço:', float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max()), (float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max())), step=100.0)
        df_filtrado = df[(df['Preço (R$)'] >= preco_min) & (df['Preço (R$)'] <= preco_max) & (df['Plataforma'] == 'console')]
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['Nintendo', 'Playstation', 'Xbox'])
        sistema = sistema.lower()
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'].str.contains(sistema)]
    else:
        preco_min, preco_max = st.sidebar.slider('Selecione o intervalo de preço:', float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max()), (float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max())), step=100.0)
        df_filtrado = df[(df['Preço (R$)'] >= preco_min) & (df['Preço (R$)'] <= preco_max) & (df['Plataforma'] == 'mobile')]
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['Android', 'iOS'])
        sistema = sistema.lower()
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'].str.contains(sistema)]

st.sidebar.markdown("---")

st.sidebar.write(f"Made in <img src='https://streamlit.io/images/brand/streamlit-mark-color.png' width='25px'> by [Larissa Ionafa](https://www.linkedin.com/in/larissa-ionafa/)", unsafe_allow_html=True)

# Fim da sidebar

# Inicio do index
st.write(
    '''
    ***Tabela geral da Nuuvem***
    '''
)

# Verificar se há resultados de pesquisa
if df_filtrado.empty:
    st.error('Nenhum jogo encontrado com essa palavra-chave ou seleção.')
else:
    pd.set_option('display.max_colwidth', None)
    st.write(df_filtrado)

    df_filtrado_por_categoria = df_filtrado.groupby('Categoria').count().reset_index()
    fig = px.pie(df_filtrado_por_categoria, values='Nome do jogo', names='Categoria', title='Distribuição dos jogos por categoria')
    st.plotly_chart(fig)

    fig = px.scatter(df_filtrado, x="Preço (R$)", y="Desconto (%)", color="Categoria", title="Preço x Desconto")
    st.plotly_chart(fig)

    fig = px.histogram(df_filtrado, x="Sistema", title="Número de jogos por sistema")
    st.plotly_chart(fig)
# Fim do index
