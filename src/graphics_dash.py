import plotly.express as px
from api import fetch_Json_data
import pandas as pd
import re
import plotly.graph_objects as go
from dash import dash_table, dcc # type: ignore

DF = fetch_Json_data('dados/Vendas.json')
cores_graficos = ['#00BCD4', '#FF5722', '#4CAF50', '#8E24AA', '#D32F2F', '#1E88E5']
DF = DF.rename(columns={'ID Loja' : 'Região Lojas'})

if not isinstance(DF, pd.DataFrame):
    DF = pd.DataFrame(DF)
    
DF['Data'] = pd.to_datetime(DF['Data'], errors = 'coerce')
DF['Valor Final'] = DF['Valor Final'].astype(str).str.replace('R\$', '', regex=True)
DF['Vamor Unitário'] = DF['Valor Unitário'].astype(str).str.replace('R\$', '', regex=True)

DF_filtered_table = DF.loc[:, ["Data", "Produto", "Valor Final"]]
DF_filtered_table['Data'] = DF_filtered_table['Data'].dt.strftime('%d/%m/%Y')

def soma_valores(text):
    valores = re.findall(r'\d+\.\d+', text)
    return sum(float(v) for v in valores)

def updateLayout(graph, tipo):
        if (tipo == 'line'):
            graph.update_layout(xaxis_tickformat = '%d/%m/%Y', 
                legend= dict(orientation = 'h', x=0, y=1.20, xanchor='left', yanchor='top'),
                font = dict(family = 'Arial', size = 14.5, color = 'black'),
                paper_bgcolor = '#FEFAE0',
                )
            
        elif (tipo == 'bar'):
            graph.update_layout(xaxis_tickformat = '%d/%m/%Y', barmode = 'stack',
                legend= dict(orientation = 'h', x=0, y=1.20, xanchor='left', yanchor='top'),
                font = dict(family = 'Arial', size = 14.5, color = 'black' ),
                paper_bgcolor = '#FEFAE0',
                )

        elif (tipo == 'table'):
            graph.update_layout(
                margin = dict(l=0, r=40, t=40, b=0),
                paper_bgcolor = '#FEFAE0',
            )
        return graph
    
DF['Valor Final'] = DF['Valor Final'].apply(soma_valores)
DF['Valor Unitário'] = DF['Valor Unitário'].apply(soma_valores)


DF_grouped = DF.groupby(['Data', 'Produto'], as_index=False)['Valor Final'].sum()
max_valor = DF_grouped['Valor Final'].max()

DF_line = DF.groupby(['Data', 'Região Lojas'], as_index=False)['Valor Unitário'].sum()
max_valor_line = DF_line['Valor Unitário'].max()

graph_bar = px.bar(DF_grouped, x='Data', y = 'Valor Final', color = 'Produto', color_discrete_sequence = cores_graficos)
graph_bar.update_yaxes(range=[0, max_valor * 1.1], autorange = False)
updateLayout(graph_bar,'bar')

graph_pie = px.pie(DF, names = 'Região Lojas', values = 'Valor Final', color = 'Região Lojas', color_discrete_sequence = cores_graficos)

graph_area = px.area(DF_grouped, x = 'Data', y = 'Valor Final', color = 'Produto')
updateLayout(graph_area,'bar')

graph_line = px.line(DF_line, x='Data', y='Valor Unitário', color='Região Lojas', markers=True, color_discrete_sequence= cores_graficos)
updateLayout(graph_line, 'line')

graph_table = go.Figure(data = [go.Table(
    columnwidth=[2, 2, 1],
    header = dict(
        values = list(DF_filtered_table.columns),
        fill_color='#00BCD4',
        align='left',
        font=dict(color='white', size=13),
    ),
    cells = dict(
        values = [DF_filtered_table[col] for col in DF_filtered_table.columns],
        fill_color='lavender',
        align='left',
        font=dict(color='black', size=12),
    )
)])
updateLayout(graph_table,'table')

data_table = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in DF_filtered_table.columns],
    data=DF_filtered_table.to_dict('records'),
    style_table={
        'height': '35vh', 
        'overflowY': 'auto',
    },
    style_cell={
        'textAlign': 'left',
        'padding': '5px',
        'fontFamily': 'Arial',
        'fontSize': '13px',
    },
    style_header={
        'backgroundColor': '#263c2b',
        'color': 'white',
        'fontWeight': 'bold'
    }
)