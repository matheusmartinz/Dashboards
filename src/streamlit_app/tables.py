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