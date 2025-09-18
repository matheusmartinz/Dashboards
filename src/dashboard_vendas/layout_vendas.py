from dash import html, dcc
import dash_bootstrap_components as dbc 
import dashboard_vendas.graphic_vendas as graphic_vendas


fig_bar = graphic_vendas.graph_bar
fig_line = graphic_vendas.graph_line
# fig_table = graphic_vendas.graph_table
data_table = graphic_vendas.data_table

layout_vendas = html.Div([
    html.Div([
        html.Div([
            html.Div(
                children=[data_table],
                style={
                    'height': '49vh',
                    'width': '100%',
                    'overflow': 'auto',
                    'padding-right': '15px',
                    'padding-left': '15px',
                    'padding-top': '20px'
                }
            )
        ], style={'display': 'flex', 'height': '50vh', 'background-color': '#FEFAE0'}),

        html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig_bar,
                style={'height': '50vh', 'width': '100%'},
                config={
                    'displaylogo': False,
                    'displayModeBar': False,
                }
            ),
        ], style={'padding': 0, 'margin': 0, 'display': 'flex', 'height': '50vh', 'width': '100%'}),

    ], className='main-container'),

    dcc.Interval(id='interval-atualizacao-vendas', interval=10*1000, n_intervals=0),
    dcc.Store(id='store-dados-graficos-vendas')
])
