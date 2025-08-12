# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

#Dash = app - Ele cria o app
import streamlit as st
#Plotly = px - Ele gera os gráficos
import plotly.express as px
#Pandas = pd - Ele carrega os dados
import pandas as pd
import graphics as graphics
import tables as tables
 
from streamlit_option_menu import option_menu 


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
    
if (selected == "Dashboards"):
        st.title('Dashboard Produtos e Cidades') 
        graphics.graphics()
    
elif (selected == "Relatório"): 
        st.title('Relatório de Vendas por Região')
        tables.tables()  
    