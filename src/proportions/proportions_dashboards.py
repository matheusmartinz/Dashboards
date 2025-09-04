import graphics_dash
from dash import html, dcc
import dash_bootstrap_components as dbc

fig_bar = graphics_dash.graph_bar
fig_line = graphics_dash.graph_line
fig_pie = graphics_dash.graph_pie
fig_area = graphics_dash.graph_area
fig_table = graphics_dash.graph_table


def layouts_by_proportion(proportion):
    if (proportion == '1:2'):
        layout_top = html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig_bar,
                config={'displaylogo': False,'displayModeBar': False},
                style={'height': '25vh', 'width': '100%'},
            )
        ])
        layout_lower = html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'height': '25vh', 'width': '50%'},
                config={'displaylogo': False, 'displayModeBar': False}
            ),
            dcc.Graph(
                id = 'grafico_pizza',
                figure = fig_pie,
                style = {'height': '25vh', 'width': '50%'},
                config = {'displaylogo': False, 'displayModeBar': False}
            )
        ], style = {'display': 'flex'})
        return layout_top, layout_lower
    
    elif (proportion == '2:2'):
        layout_top = html.Div([
            dcc.Graph(
                id = 'grafico_pizza',
                figure = fig_pie,
                style = {'height': '25vh', 'width': '50%'},
                config = {'displaylogo': False, 'displayModeBar': False}
            ),
            dcc.Graph(
                id='grafico_bar2',
                figure=fig_bar,
                style = {'height': '25vh', 'width': '50%'},
                config={'displaylogo': False,'displayModeBar': False},
            )
        ], style = {'display': 'flex'})
        layout_lower = html.Div([
                dcc.Graph(
                id = 'grafico_pizza2',
                figure = fig_pie,
                style = {'height': '25vh', 'width': '50%'},
                config = {'displaylogo': False, 'displayModeBar': False}
            ),
                dcc.Graph(
                    id = 'grafico_area2',
                    figure = fig_area,
                    style = {'height': '25vh', 'width': '50%'},
                    config = {'displaylogo': False, 'displayModeBar': False}
                )
        ], style = {'display': 'flex'})
        return layout_top, layout_lower
    
    elif (proportion == '2:1'):
        layout_top = html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'height': '25vh', 'width': '50%'},
                config={'displaylogo': False, 'displayModeBar': False}
            ),
            dcc.Graph(
                id = 'grafico_pizza',
                figure = fig_pie,
                style = {'height': '25vh', 'width': '50%'},
                config = {'displaylogo': False, 'displayModeBar': False}
            )
        ], style = {'display': 'flex'})
        layout_lower = html.Div([
            dcc.Graph(
                    id = 'grafico_area',
                    figure = fig_area,
                    style = {'height': '25vh', 'width': '100%'},
                    config = {'displaylogo': False, 'displayModeBar': False}
            )
        ])
        return layout_top, layout_lower