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
- numpy
- jupyter

<br>

Além disso, é necessário ter o arquivo `base_tratada.csv` na pasta `2_bases_tratadas` do repositório `web-mining-03` e colocá-lo na mesma pasta que o código.

Para realizar isso segue os comandos:

```
cd 3_tratamento/ac02/
```

```
scrapy crawl promocoes-jogos -O ../../1_bases_originais/original.csv
```

Agora temos a base récem extraída pelo scrapy, agora vamos trata-lá:

Vá ao arquivo `preparacao_dos_dados_esqueleto_v2.ipynb` e execute tudo:

![Screenshot_1241](https://user-images.githubusercontent.com/65693484/233505816-ec3d135d-990a-447f-82aa-2a12134b4f24.png)

Pronto! Agora temos a base tratada pronta para o próximo passo.

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
