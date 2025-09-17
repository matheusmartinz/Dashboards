from dash import html, dcc  
import pandas as pd
import apis.api as api
import dashboard_logistica.graphic_logistica as graphic_logistica 
import dash_bootstrap_components as dbc 

# fig_bar = graphic_logistica.graph_bar
fig_line = graphic_logistica.graph_line
# fig_pie = graphic_logistica.graph_pie
# fig_area = graphic_logistica.graph_area
fig_histogram = graphic_logistica.graph_histogram
# fig_table = graphic_logistica.graph_table
# data_table = graphic_logistica.data_table
fig_donut = graphic_logistica.graph_donut

layout_logistica = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'height': '50vh', 'width': '100%'},
                config = {
                    'displaylogo': False,
                    'displayModeBar': False,
                }
            ),
        ], style={'padding': 0, 'margin': 0, 'display': 'flex', 'height': '50vh', 'width': '100%' }),

        html.Div([
            dcc.Graph(
                id='grafico_histogram',
                figure=fig_histogram,
                style={'height': '50vh', 'width': '70%'},
                config = {
                    'displaylogo': False,
                    'displayModeBar': False,
                },
            ),
            html.Div([
                dcc.Graph(
                id='grafico_donut',
                figure=fig_donut,
                config = {
                    'displaylogo': False,
                    'displayModeBar': False,
                },
                style={'height': '45vh', 'width': '100%'})],
            style={'height': '50vh', 'width': '50%'})
            
        ], style={'display': 'flex', 'height': '50vh', 'width': '100%', 'background-color': '#FEFAE0' }),
    ], className='main-container'), 
])