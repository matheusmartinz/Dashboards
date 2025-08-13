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
for coluna in ['Valor Final']: DF_Valores[coluna] = (DF_Valores[coluna].str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)).astype(float)
DF_Valores = DF_Valores.sort_values(by='Valor Final', ascending=True)
DF_Valores = DF_Valores.rename(columns={'ID Loja': 'Região da Loja'})
DF_Valores['Data'] = pd.to_datetime(DF_Valores['Data'], dayfirst=True, errors='coerce')


def graphics(): 
    placeholder = st.empty()
    
    if (st.session_state.get('tela_atual') != "Dashboards"):
        placeholder = st.empty()
        return
    
    with placeholder.container():  
        col_um, col_dois = st.columns(2)
        
        with col_um:
            grafico_selecionado = st.selectbox(SELECT_NAME, GRAFICOS, key='grafico1')
            if grafico_selecionado == 'Gráfico de Barras':
                graph2 = px.line(DF_Valores, x='Data', y='Produto', color='Região da Loja', markers=True)
                st.plotly_chart(graph2, use_container_width=True, key='2')
            elif grafico_selecionado == 'Gráfico de Linhas':
                graph = px.bar(DF_Valores, x='Quantidade', y='Produto', color='ID Loja')
                graph.update_xaxes(type = 'category')
                st.plotly_chart(graph, use_container_width=True, key='1')
                
        with col_dois:
            graficoSelecionado2 = st.selectbox(SELECT_NAME, GRAFICOS_DOIS, key='grafico2')
            if graficoSelecionado2 == 'Gráfico de Fúnil':
                graph3 = px.funnel_area(DF, names='Produto', values='Quantidade', color='Data')  
                st.plotly_chart(graph3, use_container_width=True, key='3')
            elif graficoSelecionado2 == 'Gráfico de Pizza':
                graph4 = px.pie(DF, names='Produto', values='Valor Final')
                st.plotly_chart(graph4, use_container_width=True, key='4')

        st.markdown("---")
       
        filtro_dados = st.multiselect('Filtrar por Região da Loja', DF_Valores['Região da Loja'].unique(), key='filtro_dados')
        
        if filtro_dados:
            DF_Valores_filtrado = DF_Valores[DF_Valores['Região da Loja'].isin(filtro_dados)]
        else:
            DF_Valores_filtrado = DF_Valores.copy()
            
        DF_grouped = DF_Valores_filtrado.groupby(['Data', 'Região da Loja'], as_index=False) ['Valor Final'].sum()
        graph5 = px.line(DF_grouped,x='Data', y='Valor Final', color='Região da Loja', title='Evolução de Vendas por Região', markers=True)

        st.plotly_chart(graph5, use_container_width=True, key='7')
 
    
