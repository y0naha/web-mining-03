# Nuuvem Database ☁
Este é um projeto criado para a disciplina de Web Mining da faculdade Impacta. O objetivo do projeto é criar uma interface que permita ao usuário filtrar jogos da plataforma Nuuvem por nome, plataforma, preço, sistema operacional e categoria.

## Instalação
Para executar o código deste projeto, é necessário ter as seguintes bibliotecas instaladas executando o seguinte comando:

```python
pip install -r requirements.txt
```

- streamlit
- pandas
- plotly

<br>

Além disso, é necessário ter o arquivo `base_tratada.csv` na pasta `2_bases_tratadas` do repositório `web-mining-03` e colocá-lo na mesma pasta que o código.


## Como executar
Para executar o código, basta abrir o terminal, navegar até a pasta que contém o arquivo e executar o seguinte comando:


```python
python -m streamlit run nuuvem_database.py
```

Isso abrirá a aplicação em uma nova aba do navegador.

## Como usar
Ao executar a aplicação, o usuário verá uma barra lateral à esquerda com os seguintes filtros:

- Busca por nome ou palavra-chave
- Plataforma (PC, Console ou Mobile)
- Intervalo de preço
- Sistema operacional (disponível apenas para PC, Console e Mobile)
Ao selecionar os filtros desejados, a tabela de jogos e os gráficos serão atualizados automaticamente.

## Autores
Este projeto foi criado por Larissa Ionafa realizado utilizando o Streamlit.