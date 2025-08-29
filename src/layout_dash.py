from dash import html, dcc  # type: ignore
import graphics_dash
import pandas as pd
import dash_bootstrap_components as dbc # type: ignore

DF = graphics_dash.DF
DF = DF.rename(columns={'ID Loja' : 'Região Lojas'})
DF['Data'] = pd.to_datetime(DF['Data'],format = '%Y/%m/%d', errors= 'coerce')
DF = DF.dropna(subset=['Valor Final', 'Data'])

fig_bar = graphics_dash.graph_bar
fig_line = graphics_dash.graph_line
fig_pie = graphics_dash.graph_pie
fig_area = graphics_dash.graph_area
fig_table = graphics_dash.graph_table

dialog = html.Div([
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle([
            html.I(className = 'fas fa-chart-pie', style = {'margin-right': '10px'}),
            'Configuração'
            ])),
        dbc.ModalBody(
            html.Div([
                html.H6('Gráficos'),
                dbc.Checklist([
                    {'label': 'Gráfico de Barra', 'value': 1},
                    {'label': 'Gráfico de Linha', 'value': 2},
                    {'label': 'Gráfico de Fúnil', 'value': 3},
                    {'label': 'Gráfico de Pizza', 'value': 4}
                ],[1,2] ,id = 'checklist-config-graphics')
            ])
        )
    ],
        id = 'config-dialog',
        is_open = False
    )
])

dialog_confirm = html.Div([
    dbc.Modal([
        dbc.ModalHeader("Você tem certeza que deseja continuar?"),
        dbc.ModalFooter([
            dbc.Button("Cancelar", id="cancel-button", className="btn_confirm_dialog", n_clicks=0),
            dbc.Button("Continuar", id="accept-button", className = 'btn_confirm_dialog', n_clicks=0),
        ]),
    ], id="confirm-dialog-download", is_open=False),
])

radio = html.Div([
    dbc.Label('Tempo dos Gráficos'),
    dbc.RadioItems(
        options = [
            {'label': '10s', 'value': 10, "disabled": True},
            {'label': '20s', 'value': 20, "disabled": True},
            {'label': '30s', 'value': 30,"disabled": True}
        ],
        id = 'radioitens-input',
    )
], className = 'radio_timer_sidebar')

sidebar = html.Div(
    id='sidebar',
    children=[
        html.Button(
            html.I(className='fa-solid fa-xmark'),
            id='btn-close-sidebar'
        ),
        html.Button(
            html.I(className='fa-solid fa-gear'),
            id='btn-config'
        ),
        dbc.Form([
            dbc.Label('Troca Automática', html_for='switch-automatic-graphics'),
            dbc.Checklist(
                options=[{"label": "Sim", "value": 1}],
                value=[],
                id='switch-automatic-graphics',
                switch=True
            ),
            radio,
            html.Div(id = 'radio-container'),
        ], className = 'form', id = 'form-checklist'),
        html.Button([
            html.I(className = 'fas fa-folder-open', id = 'icon_button_export'),
            "Exportar CSV"
            ],id = 'button_export', n_clicks = 0),
        dcc.Download(id="download_dataframe_csv"),
        dbc.DropdownMenu(
            label = html.Span([html.I(className = 'fa-solid fa-chart-pie', style = {'margin-right': '25px'}), 'Gráficos'], style = {'margin-right': '10px'}),
            direction = 'down',
            children = [
                dbc.DropdownMenuItem(html.Div('Layout', className = 'layout_graphics', id = 'btn-layout')),
                dbc.DropdownMenuItem(html.Div('Filtros', className = 'filter_graphics', id = 'btn-filter')),
            ], className = 'dropdown_config_graphics',toggle_class_name="btn_dropdown"),
        dialog,
        dialog_confirm,
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
        ], style={'padding': 0, 'margin': 0, 'display': 'flex'}),

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
    dcc.Store(id='store-tempo-definido', data=False),
    
    dcc.Interval(
        id='meu_timer',
        interval=9999999,
        n_intervals=0
    )
])





