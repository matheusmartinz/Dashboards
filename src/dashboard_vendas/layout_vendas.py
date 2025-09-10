from dash import html, dcc
import dash_bootstrap_components as dbc 
import dashboard_vendas.graphic_vendas as graphic_vendas


fig_bar = graphic_vendas.graph_bar
fig_line = graphic_vendas.graph_line
fig_pie = graphic_vendas.graph_pie
fig_area = graphic_vendas.graph_area
fig_histogram = graphic_vendas.graph_histogram
fig_table = graphic_vendas.graph_table
data_table = graphic_vendas.data_table

layout_vendas = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig_bar,
                style={'height': '50vh', 'width': '100%'},
                config = {
                    'displaylogo': False,
                    'displayModeBar': False,
                    'staticPlot': True
                }
            ),
        ], style={'padding': 0, 'margin': 0, 'display': 'flex', 'height': '50vh', 'width': '100%'}),

        html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'height': '50vh', 'width': '70%'},
                config = {
                    'displaylogo': False,
                    'displayModeBar': False,
                    'staticPlot': True
                }
            ),
            html.Div(
            children=[data_table],
            style={'height': '45vh', 'width': '35%','margin-right': '25px', 'margin-top': '35px'})
        ], style={'display': 'flex', 'height': '50vh'}),
    ], className='main-container'), 
])