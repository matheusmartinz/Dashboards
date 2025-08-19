import plotly.express as px
from api import fetch_Json_data
import pandas as pd
import re

DF = fetch_Json_data('dados/Vendas.json')
cores_graficos = ['#00BCD4', '#FF5722', '#4CAF50', '#8E24AA', '#D32F2F', '#1E88E5']
DF = DF.rename(columns={'ID Loja' : 'Região Lojas'})

if not isinstance(DF, pd.DataFrame):
    DF = pd.DataFrame(DF)
    
DF['Data'] = pd.to_datetime(DF['Data'], errors = 'coerce')
DF['Valor Final'] = DF['Valor Final'].astype(str).str.replace('R\$', '', regex=True)
DF['Vamor Unitário'] = DF['Valor Unitário'].astype(str).str.replace('R\$', '', regex=True)


def soma_valores(text):
    valores = re.findall(r'\d+\.\d+', text)
    return sum(float(v) for v in valores)

def updateLayout(graph, tipo):
        if (tipo == 'line'):
            graph.update_layout(xaxis_tickformat = '%d/%m/%Y', 
                legend= dict(orientation = 'h', x=0, y=1.20, xanchor='left', yanchor='top'),
                font = dict(family = 'Arial', size = 14.5, color = 'black' ))
            
        elif (tipo == 'bar'):
            graph.update_layout(xaxis_tickformat = '%d/%m/%Y', barmode = 'stack',
                legend= dict(orientation = 'h', x=0, y=1.20, xanchor='left', yanchor='top'),
                font = dict(family = 'Arial', size = 14.5, color = 'black' ))
            
        return graph
    
DF['Valor Final'] = DF['Valor Final'].apply(soma_valores)
DF['Valor Unitário'] = DF['Valor Unitário'].apply(soma_valores)


DF_grouped = DF.groupby(['Data', 'Produto'], as_index=False)['Valor Final'].sum()
max_valor = DF_grouped['Valor Final'].max()

DF_line = DF.groupby(['Data', 'Região Lojas'], as_index=False)['Valor Unitário'].sum()
max_valor_line = DF_line['Valor Unitário'].max()

graph_bar = px.bar(DF_grouped, x='Data', y = 'Valor Final', color = 'Produto', color_discrete_sequence = cores_graficos)
updateLayout(graph_bar,'bar')

graph_line = px.line(DF_line, x='Data', y='Valor Unitário', color='Região Lojas', markers=True, color_discrete_sequence= cores_graficos)
updateLayout(graph_line, 'line')

graph_bar.update_yaxes(range=[0, max_valor * 1.1], autorange = False)