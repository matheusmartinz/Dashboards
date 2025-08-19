import streamlit as st
import pandas as pd
import time
from api import fetch_data

salas = "http://localhost:8080/sala"

def tables(timeout):
    place_holder = st.empty();
    
    while True:
        DF = fetch_data(salas)
        Valores_Unicos = DF[['numeroSala', 'serieAno', 'capacidadeAlunos', 'alunos']]
        place_holder.write(Valores_Unicos)
        time.sleep(timeout)    
            
    # DF_Valores = DF[['ID Loja','Produto','Valor Unitário', 'Valor Final']]
    # DF_Valores = DF_Valores.rename(columns={'ID Loja': 'Região da Loja'})
    # options_slider = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    # value_max_default = max(options_slider)
    # st.select_slider('Selecione o valor máximo para exibir na tabela', options=options_slider, value=value_max_default, key='slider')
    
    # valor_max = st.session_state.slider
    # DF_Valores_filtrado = DF_Valores[DF_Valores['Valor Final'] <= valor_max]
    # DF_Valores_filtrado = DF_Valores_filtrado.sort_values(by='Valor Final', ascending=False)
    # DF_Valores_filtrado['Valor Unitário'] = DF_Valores_filtrado['Valor Unitário'].apply(lambda x: f'R$ {x:,.2f}')
    # DF_Valores_filtrado['Valor Final'] = DF_Valores_filtrado['Valor Final'].apply(lambda x: f'R$ {x:,.2f}')
    # st.table(DF_Valores_filtrado)