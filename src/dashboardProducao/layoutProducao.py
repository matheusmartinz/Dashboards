from dash import html , dcc 
import dashboardProducao


layoutProducao = html.Div([
    html.Div([
       html.Div([
            html.H1("Dashboard Produção", style={'background-color': 'purple'})
       ], style = {'height': '50vh'}),
       
       html.Div([
            html.H1("Dashboard Produção", style={'background-color': 'yellow'}),
       ], style = {'height': '50vh'})
    ])
], id = 'container_layout_producao', style = {'padding' : 0, 'margin': 0, 'height': '100vh'})