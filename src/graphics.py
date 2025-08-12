import plotly.express as px
import pandas as pd
import streamlit as st

DF = pd.read_excel('dados/Vendas.xlsx')

GRAFICOS = ['Gráfico de Barras', 'Gráfico de Linhas']
GRAFICOS_DOIS = ['Gráfico de Fúnil', 'Gráfico de Pizza']

SELECT_NAME = 'Selecione o gráfico';

DF_Valores = DF[['ID Loja','Valor Unitário', 'Valor Final', 'Data']]
DF_Valores['Valor Final'] = DF_Valores['Valor Final'].apply(lambda x: f'R$ {x:,.2f}')  
DF_Valores = DF_Valores.rename(columns={'ID Loja': 'Região da Loja'})  


st.set_page_config(layout="wide")

def graphics(): 
    col_um, col_dois = st.columns(2)
    
    with col_um:
            grafico_selecionado = st.selectbox(SELECT_NAME, GRAFICOS, key='grafico1')
            
            if (grafico_selecionado == 'Gráfico de Barras'):
             graph = px.bar(DF, x='Quantidade', y='Produto', color='ID Loja')
             st.plotly_chart(graph, use_container_width=True, key='1')
            elif (grafico_selecionado == 'Gráfico de Linhas'):
             graph2 = px.line(DF,x='Valor Final', y='Produto', color='ID Loja')
             st.plotly_chart(graph2, use_container_width=True, key='2')

    with col_dois:
            graficoSelecionado2 = st.selectbox(SELECT_NAME, GRAFICOS_DOIS, key='grafico2')
            
            if (graficoSelecionado2 == 'Gráfico de Fúnil'):
                graph3 = px.funnel_area(DF, names='Produto', values='Quantidade', color='Data')  
                st.plotly_chart(graph3, use_container_width=True, key='3')
            elif (graficoSelecionado2 == 'Gráfico de Pizza'):
                graph4 = px.pie(DF, names='Produto', values='Valor Final')
                st.plotly_chart(graph4, use_container_width=True, key='4')
                
    # with col_tres:
            # graficoSelecionado2 = st.selectbox(SELECT_NAME, GRAFICOS_DOIS, key='grafico3')
            
            # if (graficoSelecionado2 == 'Gráfico de Fúnil'):
            #     graph3 = px.funnel_area(DF, names='Produto', values='Quantidade', color='Data')  
            #     st.plotly_chart(graph3, use_container_width=True, key='5')
            # elif (graficoSelecionado2 == 'Gráfico de Pizza'):
            #     graph4 = px.pie(DF, names='Produto', values='Valor Final')
            #     st.plotly_chart(graph4, use_container_width=True, key='6')
                
    filtro_dados = st.multiselect('Filtrar por Região da Loja', DF_Valores['Região da Loja'].unique())
    
    if (filtro_dados):
        DF_Valores_filtrado = DF_Valores[DF_Valores['Região da Loja'].isin(filtro_dados)]
        graph5 = px.line(DF_Valores_filtrado, x='Data', y='Valor Final', color='Região da Loja')
    else:
        graph5 = px.line(DF_Valores, x='Data', y='Valor Final', color='Região da Loja')

    st.plotly_chart(graph5, use_container_width=True, key='7')
            
          