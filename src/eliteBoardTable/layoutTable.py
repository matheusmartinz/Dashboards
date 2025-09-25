from dash import html, dcc
import dash_bootstrap_components as dbc 
import eliteBoardTable.graphicsTableBoard as graphic_vendas
from layoutTable.generatorTable import generatorTable
from layoutTable.columnsTable import columnsTables
from layoutTable.generatorTable import create_table


fig_bar = graphic_vendas.graph_bar
fig_line = graphic_vendas.graph_line
# fig_table = graphic_vendas.graph_table
data_table = graphic_vendas.data_table

data_table2 = graphic_vendas.dataTeste

layout_board = html.Div([
    html.Div([
        html.Div([
            html.Img(src = 'assets/peon_logo-removebg-preview.png', style = {'height': '100%', 'width': 'auto'}),
            html.H4("Andamento das coleções", style = {'flexGrow': 1, 'textAlign': 'center', 'margin': 0, 'color': 'white'})
        ], id = 'header-board'),
        
        html.Div([
            # html.Div(
            #     children= [generatorTable(data_table2, columnsTables)],
            #     style={
            #         'width': '100%',
            #         'padding': '20px 10px 0 10px',
            #     })
            
        html.Div(
            create_table(data_table2, columnsTables),
        style = {
            'height': '82vh',           
            'overflowY': 'auto',      
            'width': '100%',
            'padding': '0px 20px 10px 20px',
        }
        )], style={'display': 'flex', 'background-color': '#FEFAE0'}),

        # html.Div([
        #     dcc.Graph(
        #         id='grafico_bar',
        #         figure=fig_bar,
        #         style={'height': '50vh', 'width': '100%'},
        #         config={
        #             'displaylogo': False,
        #             'displayModeBar': False,
        #         }
        #     ),
        # ], style={'padding': 0, 'margin': 0, 'display': 'flex', 'height': '50vh', 'width': '100%'}),

    ], className='main-container'),

    dcc.Interval(id='interval-atualizacao-vendas', interval=10 *1000, n_intervals=0),
    dcc.Store(id='store-dados-graficos-vendas')
])
