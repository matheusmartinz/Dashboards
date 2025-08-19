import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit_app.graphic as graphic
import streamlit_app.tables as tables
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
            "container": {"background-color": "#5C7F54", },
            "icon": {"color": "#FEFAE0", "font-size": "20px"},
            "nav-link-selected": {"background-color": "#162419"},
        }
    )
        st.session_state['tela_atual'] = selected
        
    if (st.session_state.get('tela_atual') == "Dashboards"):
        st.markdown('<div class="title-custom">PRODUTOS E CIDADES</div>', unsafe_allow_html=True) 
        graphic.graphic()
    
    elif (st.session_state.get('tela_atual') == "Relatório"): 
        st.title('Relatório de Vendas por Região')
        tables.tables(10) 
        
if __name__ == '__main__':
    main()