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
fig_area = graphics_dash.graph_area
fig_table = graphics_dash.graph_table

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
            ),
            html.Div(id = 'radio-container'),
        ], className = 'form', id = 'form-checklist'),
        dbc.DropdownMenu(
            label = html.I(className = 'fa-solid fa-gear'),
            direction = 'center',
            nav = False,
            in_navbar = False,
            caret = False,
            toggle_class_name = 'btn-config',
            id = 'item-config',
            children = [
                dbc.DropdownMenuItem(
                    html.Span('Configuração', className = 'menu-item-config', n_clicks = 0)
                )
            ]
        )
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
                style={'height': '100%', 'width': '70%'}
            ),
            html.Div(
            children=[graphics_dash.data_table],
            style={'height': '70%', 'width': '35%','margin-right': '25px'})
        ], style={'display': 'flex', 'height': '45vh'}),
    ], className='main-container'), 

    dcc.Store(id = 'store-switch-value', data = 0),
    
    dcc.Interval(
        id='meu_timer',
        interval=10000,
        n_intervals=0
    )
])

radio = html.Div([
    dbc.Label('Tempo dos Gráficos'),
    dbc.RadioItems(
        options = [
            {'label': '10 Segundos', 'value': 10},
            {'label': '20 Segundos', 'value': 20},
            {'label': '30 Segundos', 'value': 30}
        ],
        id = 'radioitems-input',
        value = 10
    )
])

dialog = html.Div([
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('TESTE'))
    ])
])

