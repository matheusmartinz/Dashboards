from dash import html, dcc  # type: ignore
import graphics_dash
import pandas as pd

DF = graphics_dash.DF
DF = DF.rename(columns={'ID Loja' : 'Região Lojas'})
DF['Data'] = pd.to_datetime(DF['Data'], errors= 'coerce')
DF = DF.dropna(subset=['Valor Final', 'Data'])

fig = graphics_dash.graph_bar
fig_line = graphics_dash.graph_line

layout = html.Div([
    html.Div([
        html.Div([
            html.Button(html.I(className = 'fa-solid fa-arrow-right'), id = 'btn-icon', n_clicks = 0)
            ], style={'height': '10vh', 'margin-left': '30px', 'margin-top': '15px'}),
        html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig,
                style={'height': '45vh', 'width': '100%'} 
            ),
        ], style={'padding': 0, 'margin': 0}),
        html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'height': '45vh', 'width': '100%'}  
            ),
        ], style={'padding': 0, 'margin': 0}),
    ], style={'height': '100vh', 'width': '100%', 'display': 'flex', 'flexDirection': 'column', 'padding': 0, 'margin': 0})
])

