import random
import plotly.express as px
import pandas as pd
import streamlit as st
import time
from api import fetch_Json_data


st.set_page_config(layout="wide")

DF = fetch_Json_data('dados/Vendas.json')

# Gráficos disponíveis
GRAFICOS = ['Gráfico de Barras', 'Gráfico de Linhas']
GRAFICOS_DOIS = ['Gráfico de Fúnil', 'Gráfico de Pizza']
cores_graficos = ['#00BCD4', '#FF5722', '#4CAF50', '#8E24AA', '#D32F2F', '#1E88E5']

# Preparação dos dados
DF_Valores = DF[['ID Loja', 'Valor Unitário', 'Valor Final', 'Data', 'Produto']].copy()
for coluna in ['Valor Final', 'Valor Unitário']:
    DF_Valores[coluna] = (DF_Valores[coluna]
                          .str.replace('R$', '', regex=False)
                          .str.replace('.', '', regex=False)
                          .str.replace(',', '.', regex=False)
                          ).astype(float)
DF_Valores = DF_Valores.sort_values(by='Valor Final', ascending=True)
DF_Valores = DF_Valores.rename(columns={'ID Loja': 'Região da Loja'})
DF_Valores['Data'] = pd.to_datetime(DF_Valores['Data'], dayfirst=True, errors='coerce')

# Verificando o gráfico e o tempo de início
if 'grafico' not in st.session_state:
    st.session_state.grafico = 0  # 0 para gráfico 1, 1 para gráfico 2, etc.

if 'start_time' not in st.session_state: 
    st.session_state.start_time = time.time()

def graphic(): 
    placeholder = st.empty()

    # Verificar tempo passado para alternar gráficos a cada 5 segundos
    elapsed_time = time.time() - st.session_state.start_time
    if elapsed_time > 5:  # Se passou mais de 5 segundos, troca de gráfico
        st.session_state.grafico = (st.session_state.grafico + 1) % 4  # Ciclo entre 4 gráficos
        st.session_state.start_time = time.time()  # Reiniciar o tempo

    # Renderizar o gráfico com base no valor de 'grafico'
    with placeholder.container():
        col_um, col_dois = st.columns([1, 1])

        if st.session_state.grafico == 0:  # Gráfico de Linhas
            with col_um:
                DF_groupedLine = DF_Valores.groupby(['Data', 'Região da Loja'], as_index=False)['Valor Unitário'].sum()
                graph = px.line(DF_groupedLine, x='Data', y='Valor Unitário', color='Região da Loja', markers=True, color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph, use_container_width=True)
            
            with col_dois:
                graph2 = px.funnel_area(DF, names='Produto', values='Quantidade', color='Data', color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph2, use_container_width=True)

        elif st.session_state.grafico == 1:  # Gráfico de Barras
            with col_um:
                DF_groupedBar = DF_Valores.groupby(['Produto'], as_index=False)['Valor Unitário'].sum()
                graph = px.bar(DF_groupedBar, x='Produto', y='Valor Unitário', color='Produto', color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph, use_container_width=True)

            with col_dois:
                graph2 = px.pie(DF, names='Produto', values='Quantidade', color='Data', color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph2, use_container_width=True)

        elif st.session_state.grafico == 2:  # Gráfico de Fúnil
            with col_um:
                DF_groupedLine = DF_Valores.groupby(['Data', 'Região da Loja'], as_index=False)['Valor Unitário'].sum()
                graph = px.line(DF_groupedLine, x='Data', y='Valor Unitário', color='Região da Loja', markers=True, color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph, use_container_width=True)
            
            with col_dois:
                graph2 = px.funnel_area(DF, names='Produto', values='Quantidade', color='Data', color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph2, use_container_width=True)

        elif st.session_state.grafico == 3:  # Gráfico de Pizza
            with col_um:
                DF_groupedBar = DF_Valores.groupby(['Produto'], as_index=False)['Valor Unitário'].sum()
                graph = px.bar(DF_groupedBar, x='Produto', y='Valor Unitário', color='Produto', color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph, use_container_width=True)

            with col_dois:
                graph2 = px.pie(DF, names='Produto', values='Quantidade', color='Data', color_discrete_sequence=cores_graficos)
                st.plotly_chart(graph2, use_container_width=True)

# Executar a função de gráficos
graphic()
