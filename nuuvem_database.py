import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px
import numpy as np

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
        preco_min, preco_max = st.sidebar.slider('Selecione o intervalo de preço:', float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max()), (float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max())), step=0.1)
        df_filtrado = df[(df['Preço (R$)'] >= preco_min) & (df['Preço (R$)'] <= preco_max) & (df['Plataforma'] == 'pc')]
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['Steam','Windows', 'Mac', 'Linux'])
        sistema = sistema.lower()
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'].str.contains(sistema)]
    elif plataforma == 'Console':
        preco_min, preco_max = st.sidebar.slider('Selecione o intervalo de preço:', float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max()), (float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max())), step=0.1)
        df_filtrado = df[(df['Preço (R$)'] >= preco_min) & (df['Preço (R$)'] <= preco_max) & (df['Plataforma'] == 'console')]
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['Nintendo', 'Playstation', 'Xbox'])
        sistema = sistema.lower()
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'].str.contains(sistema)]
        st.info('Com exceção da Nintendo, aos demais sistemas são disponibilizados apenas créditos para a loja virtual da plataforma.', icon="ℹ️")
    else:
        preco_min, preco_max = st.sidebar.slider('Selecione o intervalo de preço:', float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max()), (float(df['Preço (R$)'].min()), float(df['Preço (R$)'].max())), step=0.1)
        df_filtrado = df[(df['Preço (R$)'] >= preco_min) & (df['Preço (R$)'] <= preco_max) & (df['Plataforma'] == 'mobile')]
        sistema = st.sidebar.selectbox('Selecione o sistema:', ['Android', 'iOS'])
        sistema = sistema.lower()
        df_filtrado = df_filtrado.loc[df_filtrado['Sistema'].str.contains(sistema)]
        st.info('São disponibilizados apenas créditos para a loja virtual da plataforma.', icon="ℹ️")

st.sidebar.markdown("---")

st.sidebar.write(f"Made in <img src='https://streamlit.io/images/brand/streamlit-mark-color.png' width='25px'> by [Larissa Ionafa](https://www.linkedin.com/in/larissa-ionafa/)", unsafe_allow_html=True)
# Fim da sidebar

# Inicio do index
st.write(
    '''
    ***Tabela filtrada***
    '''
)

if df_filtrado.empty:
    st.error('Nenhum jogo encontrado com essa palavra-chave ou seleção.')
else:
    st.markdown('Esta tabela é resultado dos filtros utilizados do menu:')
    pd.set_option('display.max_colwidth', None)
    st.write(df_filtrado)
    st.warning('Dica: Ao selecionar a coluna ela já é filtrada por ordem', icon="💡")

    # calcula a porcentagem da maior e menor categoria
    df_filtrado_por_categoria = df_filtrado.groupby(['Plataforma', 'Categoria']).count().reset_index()[['Plataforma', 'Categoria', 'Nome do jogo']]
    df_filtrado_por_categoria = df_filtrado_por_categoria.pivot_table(values='Nome do jogo', index='Categoria', columns='Plataforma', fill_value=0)
    total_jogos_por_plataforma = df_filtrado_por_categoria.sum(axis=0)

    df_filtrado_por_categoria_porcentagem = df_filtrado_por_categoria / total_jogos_por_plataforma * 100

    categoria_maior_porcentagem = df_filtrado_por_categoria_porcentagem.idxmax().values[0]
    maior_porcentagem = df_filtrado_por_categoria_porcentagem.max().values[0]

    categoria_menor_porcentagem = df_filtrado_por_categoria_porcentagem.idxmin().values[0]
    menor_porcentagem = df_filtrado_por_categoria_porcentagem.min().values[0]

    df_filtrado_por_categoria = df_filtrado.groupby('Categoria').count().reset_index()
    fig = px.pie(df_filtrado_por_categoria, values='Nome do jogo', names='Categoria', title='Distribuição dos jogos por categoria')
    st.plotly_chart(fig)
    st.markdown(
        f"""
        Este gráfico de pizza representa a distribuição de categoria de acordo com a plataforma
        <br>
        Maior porcentagem: `{categoria_maior_porcentagem}` com `{maior_porcentagem:.2f}%` dos jogos
        <br>
        Menor porcentagem: `{categoria_menor_porcentagem}` com `{menor_porcentagem:.2f}%` dos jogos
        """,
        unsafe_allow_html=True
    )

    # calcula o maior e menor valor de preço e desconto
    df_desconto_jogo = df_filtrado[['Desconto (%)', 'Nome do jogo','Preço (R$)','Categoria']].dropna()
    df_maior_promocao = df_desconto_jogo.sort_values(by='Desconto (%)', ascending=False)
    df_menor_promocao = df_desconto_jogo.sort_values(by='Desconto (%)', ascending=True)

    maior_desconto_jogo = df_maior_promocao.iloc[0]['Nome do jogo']
    maior_desconto_valor = df_maior_promocao.iloc[0]['Desconto (%)']
    maior_desconto_preco = df_maior_promocao.iloc[0]['Preço (R$)']
    maior_desconto_categoria = df_maior_promocao.iloc[0]['Categoria']

    menor_desconto_jogo = df_menor_promocao.iloc[0]['Nome do jogo']
    menor_desconto_valor = df_menor_promocao.iloc[0]['Desconto (%)']
    menor_desconto_preco = df_menor_promocao.iloc[0]['Preço (R$)']
    menor_desconto_categoria = df_menor_promocao.iloc[0]['Categoria']

    fig = px.scatter(df_filtrado, x="Preço (R$)", y="Desconto (%)", color="Categoria", title="Preço x Desconto x Categoria")
    st.plotly_chart(fig)
    st.markdown(
        f"""
        Este gráfico de disperção representa a distribuição de desconto de acordo com o preço e categoria
        <br>
        Maior promoção: `{maior_desconto_jogo}` - `{maior_desconto_valor}%`: `R${maior_desconto_preco}` (`{maior_desconto_categoria}`)
        <br>
        Menor promoção: `{menor_desconto_jogo}` - `{menor_desconto_valor}%`: `R${menor_desconto_preco}` (`{menor_desconto_categoria}`)
        """,
        unsafe_allow_html=True
    )

    # calcula a quantidade de jogos por sistema
    df_sistemas = df_filtrado[['Sistema']].dropna()

    df_sistemas_count = df_sistemas.groupby('Sistema').size().sort_values(ascending=False)

    maior_quantidade = df_sistemas_count.index[0]
    menor_quantidade = df_sistemas_count.index[-1]

    fig = px.histogram(df_filtrado, x="Sistema", title="Número de jogos por sistema")
    st.plotly_chart(fig)
    st.markdown(
    f"""
    Este gráfico de barras representa o número total de compatibilidade de jogos por sistema
    <br>
    Maior compatibilidade: `{maior_quantidade}`
    <br>
    Menor compatibilidade: `{menor_quantidade}`
    """,
    unsafe_allow_html=True
)

    # calcular o numero de outliers
    Q1 = df_filtrado['Preço (R$)'].quantile(0.25)
    Q3 = df_filtrado['Preço (R$)'].quantile(0.75)
    IQR = Q3 - Q1

    outliers = df_filtrado[(df_filtrado['Preço (R$)'] < (Q1 - 1.5 * IQR)) | (df_filtrado['Preço (R$)'] > (Q3 + 1.5 * IQR))]
    num_outliers = len(outliers)

    fig = px.box(df_filtrado, x="Preço (R$)", y="Categoria", title="Bloxplot das categorias relacionados ao preço")
    st.plotly_chart(fig)
    if num_outliers != 0:
            st.markdown(
            f"""
            Este bloxplot representa a distribuição de categoria de acordo com o preço
            <br>
            Quantidade de outliers: `{num_outliers}`
            """,
            unsafe_allow_html=True
            )
    else:
            st.markdown(
            f"""
            Este bloxplot representa a distribuição de categoria de acordo com o preço
            <br>
            """,
            unsafe_allow_html=True
            )
            st.error("Não existe outliers neste bloxplot")

st.write(
'''
***Tabela geral***
'''
)

pd.set_option('display.max_colwidth', None)
st.write(df)
# Fim do index
