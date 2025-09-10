import dashboard_vendas.graphic_vendas as layout_vendas
from dash import html, dcc
import dash_bootstrap_components as dbc

fig_bar = layout_vendas.graph_bar
fig_line = layout_vendas.graph_line
fig_pie = layout_vendas.graph_pie
fig_area = layout_vendas.graph_area
fig_table = layout_vendas.graph_table

graphStyle = {
    'width': '50%',
    'height': '25vh',
    'padding-top': '10px',
    'padding-bottom': '10px',
    'box-sizing': 'border-box'
}

def layouts_by_proportion(proportion):
    if (proportion == '1:2'):
        layout_top = html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig_bar,
                config={'displaylogo': False,'displayModeBar': False},
                style={'height': '25vh', 'width': '100%', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
            )
        ], style = {'display': 'flex', 'height': '25vh'})
        layout_lower = html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style= graphStyle,
                config={'displaylogo': False, 'displayModeBar': False}
            ),
            dcc.Graph(
                id = 'grafico_pizza',
                figure = fig_pie,
                style = graphStyle,
                config = {'displaylogo': False, 'displayModeBar': False}
            )
        ] , style = {'display': 'flex'})
        return layout_top, layout_lower
    
    elif (proportion == '2:2'):
        layout_top = html.Div([
            dcc.Graph(
                id = 'grafico_pizza',
                figure = fig_pie,
                style = {'height': '25vh', 'width': '50%', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
                config = {'displaylogo': False, 'displayModeBar': False}
            ),
            dcc.Graph(
                id='grafico_bar2',
                figure=fig_bar,
                style = {'height': '25vh', 'width': '50%', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
                config={'displaylogo': False,'displayModeBar': False},
            )
        ])
        layout_lower = html.Div([
                dcc.Graph(
                id = 'grafico_pizza2',
                figure = fig_pie,
                style = graphStyle,
                config = {'displaylogo': False, 'displayModeBar': False}
            ),
                dcc.Graph(
                    id = 'grafico_area2',
                    figure = fig_area,
                    style = graphStyle,
                    config = {'displaylogo': False, 'displayModeBar': False}
                )
        ])
        return layout_top, layout_lower
    
    elif (proportion == '2:1'):
        layout_top = html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'width': '50%', 'height': '25vh', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
                config={'displaylogo': False, 'displayModeBar': False}
            ),
            dcc.Graph(
                id = 'grafico_pizza',
                figure = fig_pie,
                style = {'width': '50%', 'height': '25vh', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
                config = {'displaylogo': False, 'displayModeBar': False}
            )
        ], style = {'display': 'flex'})
        layout_lower = html.Div([
            dcc.Graph(
                    id = 'grafico_area',
                    figure = fig_area,
                    style = {'height': '25vh', 'width': '100%', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
                    config = {'displaylogo': False, 'displayModeBar': False}
            )
        ])
        return layout_top, layout_lower