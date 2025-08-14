import random
import plotly.express as px
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
from api import fetch_Json_data

DF = fetch_Json_data('dados/Vendas.json')

# pd.read_excel('dados/Vendas.xlsx')

GRAFICOS = ['Gráfico de Barras', 'Gráfico de Linhas']
GRAFICOS_DOIS = ['Gráfico de Fúnil', 'Gráfico de Pizza']

SELECT_NAME = 'Selecione o gráfico';

DF_Valores = DF[['ID Loja','Valor Unitário', 'Valor Final', 'Data', 'Produto']].copy()
for coluna in ['Valor Final', 'Valor Unitário']: DF_Valores[coluna] = (DF_Valores[coluna].str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)).astype(float)
DF_Valores = DF_Valores.sort_values(by='Valor Final', ascending=True)
DF_Valores = DF_Valores.rename(columns={'ID Loja': 'Região da Loja'})
DF_Valores['Data'] = pd.to_datetime(DF_Valores['Data'], dayfirst=True, errors='coerce')


def graphics(): 
    placeholder = st.empty()
    
    if (st.session_state.get('tela_atual') != "Dashboards"):
        placeholder = st.empty()
        return
    
    with placeholder.container():  
        col_um, col_dois = st.columns([1,1])
        cores_graficos = ['#00BCD4','#FF5722','#4CAF50','#8E24AA','#D32F2F','#1E88E5']
        
        with col_um:
                DF_groupedLine = DF_Valores.groupby(['Data', 'Região da Loja'] , as_index=False)['Valor Unitário'].sum()
                graph2 = px.line(DF_groupedLine, x='Data', y='Valor Unitário', color='Região da Loja', markers=True,
                                 color_discrete_sequence = cores_graficos)
                st.plotly_chart(graph2, use_container_width=True, key='2')
                
        with col_dois:
                graph3 = px.funnel_area(DF, names='Produto', values='Quantidade', color='Data', color_discrete_sequence=cores_graficos)  
                st.plotly_chart(graph3, use_container_width=True, key='3')