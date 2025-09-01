from dash import html, dcc  
import graphics_dash
import pandas as pd
import dash_bootstrap_components as dbc 
from assets.CustomDialog import CustomDialog 
from assets.CustomButton import CustomButton

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
    CustomDialog(
        headerText = "Você deseja continuar com o download?",
        btn_left_text = 'Cancelar',
        id_btn_left = 'cancel-button',
        btn_right_text = 'Continuar',
        id_btn_right = 'accept-button',
        open = False,
        clicks = 0,
        id_modal = 'confirm-dialog-download',
        className = 'btn_confirm_dialog'        
    )
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
        CustomButton(
            nameIcon = 'fa-solid fa-xmark',
            idIcon = 'icon-close-sidebar',
            idButton = 'btn-close-sidebar',
        ),
        CustomButton(
            nameIcon = 'fa-solid fa-gear',
            idIcon = 'icon-config-gear',
            idButton = 'btn-config'
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
        CustomButton(
            nameIcon = 'fas fa-folder-open',
            idIcon = 'icon_button_export',
            textButton = 'Exportar CSV',
            idButton = 'button_export',
            clicks = 0
        ),
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

layout_view = html.Div([
    html.Div([
        # html.Div([
        #     CustomButton(
        #         nameIcon = 'fa-solid fa-arrow-right',
        #         idIcon = 'icon-open-sidebar',
        #         clicks = 0,
        #         idButton = 'btn-open-sidebar'
        #     )
        # ], style={'height': '10vh', 'margin-left': '55px', 'margin-top': '25px'}),

        html.Div([
            dcc.Graph(
                id='grafico_bar',
                figure=fig_bar,
                style={'height': '45vh', 'width': '100%'},
                config = {
                    'displaylogo': False
                }
            ),
        ], style={'padding': 0, 'margin': 0, 'display': 'flex'}),

        html.Div([
            dcc.Graph(
                id='grafico_line',
                figure=fig_line,
                style={'height': '100%', 'width': '70%'},
                config = {
                    'displaylogo': False
                }
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