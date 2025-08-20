from dash import html, dcc  # type: ignore
import graphics_dash
import pandas as pd
import dash_bootstrap_components as dbc # type: ignore

DF = graphics_dash.DF
DF = DF.rename(columns={'ID Loja' : 'Região Lojas'})
DF['Data'] = pd.to_datetime(DF['Data'], errors= 'coerce')
DF = DF.dropna(subset=['Valor Final', 'Data'])

fig_bar = graphics_dash.graph_bar
fig_line = graphics_dash.graph_line
fig_pie = graphics_dash.graph_pie

sidebar = html.Div(
    id='sidebar',
    children=[
        html.Button(
            html.I(className='fa-solid fa-xmark'),
            id='btn-close-sidebar'
        ),
        dbc.Form([
            dbc.Label('Troca Automática', html_for='switch-automatic-graphics'),
            dbc.Checklist(
                options=[{"label": "Sim", "value": 1}],
                value=[],
                id='switch-automatic-graphics',
                switch=True
            )
        ])
    ]
)


layout = html.Div([
    html.Div([
        html.Div([
            html.Button(
                html.I(className='fa-solid fa-arrow-right'),
                id='btn-icon-open',
                n_clicks=0
            )
        ], style={'height': '10vh', 'margin-left': '55px', 'margin-top': '25px'}),

        sidebar,

        html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig_bar,
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

    ], className='main-container'), 

    dcc.Interval(
        id='meu_timer',
        interval=6000,
        n_intervals=0
    )
])


