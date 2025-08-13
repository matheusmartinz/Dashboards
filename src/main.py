#Dash = app - Ele cria o app
import streamlit as st
#Plotly = px - Ele gera os gráficos
import plotly.express as px
#Pandas = pd - Ele carrega os dados
import pandas as pd
import graphics as graphics
import tables as tables
import assets.generic_style as css
 
from streamlit_option_menu import option_menu 
css.inject_css()

def main():
    if 'tela_atual' not in st.session_state:
        st.session_state['tela_atual'] = "Dashboards"
        
    with st.sidebar:
        selected = option_menu(
        "Navegação",  
        ["Dashboards", "Relatório"],  
        icons=["bar-chart", "table"],  
        default_index=0,
        styles={
            "container": {"padding": "5px"},
            "icon": {"color": "orange", "font-size": "20px"},
            "nav-link-selected": {"background-color": "#6c757d"},
        }
    )
        st.session_state['tela_atual'] = selected
        
    if (st.session_state.get('tela_atual') == "Dashboards"):
        st.title('Dashboard Produtos e Cidades') 
        graphics.graphics()
    
    elif (st.session_state.get('tela_atual') == "Relatório"): 
        st.title('Relatório de Vendas por Região')
        tables.tables(10) 
        
if __name__ == '__main__':
    main()