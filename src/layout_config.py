from collections.abc import Sequence
from xml.dom.xmlbuilder import Options
from dash import html, dcc  
import previews_dash
import pandas as pd
import dash_bootstrap_components as dbc 
from components.CustomDialog import CustomDialog 
from components.CustomButton import CustomButton

DF = previews_dash.DF
DF = DF.rename(columns={'ID Loja' : 'Região Lojas'})
DF['Data'] = pd.to_datetime(DF['Data'],format = '%Y/%m/%d', errors= 'coerce')
DF = DF.dropna(subset=['Valor Final', 'Data'])

fig_bar = previews_dash.graph_bar
fig_line = previews_dash.graph_line
fig_pie = previews_dash.graph_pie
fig_area = previews_dash.graph_area
# fig_table = previews_dash.graph_table

dialog = html.Div([
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle([
            html.I(className = 'fas fa-chart-pie', style = {'margin-right': '10px'}),
            'Configuração'
            ])),
        dbc.ModalBody([
            html.Div([
                html.H6('Gráfico(s) Superior', style = {'font-weight': '600', 'margin-bottom': '12px'}),
                dbc.Checklist([
                    {'label': 'Gráfico de Barra', 'value': 1},
                    {'label': 'Gráfico de Linha', 'value': 2},
                    {'label': 'Gráfico de Fúnil', 'value': 3},
                    {'label': 'Gráfico de Pizza', 'value': 4}
                ],[1,2] ,id = 'checklist-config-graphics-top', style = {'border-radius': '6px'}),
            ],  id = 'top-checklist-layout'),
                html.Hr(style = {'margin': '10px 0'}),
            html.Div([
                html.H6('Gráfico(s) Inferior', style = {'font-weight': '600', 'margin-bottom': '12px'}),
                dbc.Checklist([
                    {'label': 'Gráfico de Barra', 'value': 1},
                    {'label': 'Gráfico de Linha', 'value': 2},
                    {'label': 'Gráfico de Fúnil', 'value': 3},
                    {'label': 'Gráfico de Pizza', 'value': 4}
                ],[1,2] ,id = 'checklist-config-graphics-lower'),
            ],  id = 'lower-checklist-layout')
        ])
    ],
        id = 'config-dialog',
        is_open = False
    )
])

checklist_layout = html.Div([
    dbc.Label('Proporção do Dashboard', style = {'justify-content': 'center', 'display': 'flex', 'font-weight': '600'}),
    dcc.RadioItems(
        id='select_layout',
        options=[
            {'label': '1:2', 'value': '1:2'},
            {'label': '2:2', 'value': '2:2'},
            {'label': '2:1', 'value': '2:1'},
            {'label': '2:3', 'value': '2:3'},
        ],
        value='1:2',
        className='radio-grid-layout',
        labelStyle={'display': 'block'}
    )
], style = {'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center', 'align-items': 'center'})


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
    dbc.Label('Tempo dos Gráficos', style = {'font-weight': '600'}),
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
            dbc.Label('Configurações', style = {'font-weight': '600', 'font-size': '20px', 'color': 'black'}),
            html.Hr(style = {'margin': '10px 0'}),
            dbc.Label('Troca Automática', html_for='switch-automatic-graphics', style = {'font-weight': '600'}),
            dbc.Checklist(
                options=[{"label": "Sim", "value": 1}],
                value=[],
                id='switch-automatic-graphics',
                switch=True
            ),
            html.Hr(style = {'margin': '10px 0'}),
            radio,
            html.Hr(style = {'margin': '10px 0'}),
            checklist_layout,
            html.Div(id = 'radio-container'),
        ], className = 'form', id = 'form-checklist-timer'),
        dialog,
        dialog_confirm,
        # CustomButton(
        #     nameIcon = 'fas fa-folder-open',
        #     idIcon = 'icon_button_export',
        #     textButton = 'Exportar CSV',
        #     idButton = 'button_export',
        #     clicks = 0
        # ),
        # dcc.Download(id="download_dataframe_csv"),
        dbc.DropdownMenu(
            label = html.Span([html.I(className = 'fa-solid fa-chart-pie', style = {'margin-right': '25px'}), 'Gráficos'], style = {'margin-right': '10px'}),
            direction = 'down',
            children = [
                dbc.DropdownMenuItem(html.Div('Layout', className = 'layout_graphics', id = 'btn-layout')),
                dbc.DropdownMenuItem(html.Div('Filtros', className = 'filter_graphics', id = 'btn-filter')),
            ], className = 'dropdown_config_graphics',toggle_class_name="btn_dropdown"),
    ]
)

# layout_config = html.Div([
#     html.Div([
#         html.Div([
#             CustomButton(
#                 nameIcon='fa-solid fa-arrow-right',
#                 idIcon='icon-open-sidebar',
#                 clicks=0,
#                 idButton='btn-open-sidebar'
#             )
#         ], style={'height': '3vh', 'margin-left': '30px', 'margin-top': '10px', 'z-index': '10'}),

#         sidebar,

#         html.Div(id = 'layout_graphics_top', style = {'width': '100%'}),

#         html.Div(id = 'layout_graphics_lower', style = {'width': '100%'})
#     ], className='main-container'),

#     dcc.Store(id='store-switch-value', data=0),
#     dcc.Store(id='store-tempo-definido', data=False),

#     dcc.Interval(
#         id='meu_timer',
#         interval=9999999,
#         n_intervals=0
#     )
# ])

layoutConfig = html.Div([
    html.Div([
        html.Div([
            html.H1('Configurações', style = {'display': 'flex', 'justify-content': 'center', 'align-itens': 'center', 'width': '100%', }), 
            
        html.Div([
            html.Div([
                dbc.Label('Troca Automática', html_for='switch-automatic-graphics', style = {'font-weight': '600'}),
                dbc.Checklist(
                options=[{"label": "Sim", "value": 1}],
                value=[],
                id='switch-automatic-graphics',
                switch=True
            )], id = 'div-switch-automatic'),
                
            html.Div([
                radio
                ],  style= {'width': '30%', 'height': '100px','display': 'flex', 'justify-content': 'center'}),
        
            ],  id = 'div-timer-options'),
        
       html.Div([
           html.Div(checklist_layout, id = 'div-checklist-proportion'),
           
           html.Div(html.H1('TESTE'), id = 'div-checklist-layout-graphics')
           
       ], style = {'display': 'flex', 'justify-content': 'space-evenly', 'height': '100%', 'margin-top': '40px'})
    ], id = 'div-top-timer'),  
    

    
     dcc.Store(id='store-switch-value', data=0),
     dcc.Store(id='store-tempo-definido', data=False),

     dcc.Interval(
        id='meu_timer',
        interval=9999999,
        n_intervals=0
        
    )], style = {'height': '50vh'}),
        
    html.Div([
        html.Div(
            id = 'layout_graphics_top',
            #      dcc.Graph(
            #         id = 'grafico_pizza2',
            #         figure = fig_pie,
            #         config = {'displaylogo': False, 'displayModeBar': False, 'autosizable': True, 'responsive': True, 'staticPlot': True},
            #         style = {'width': '50%', 'height': '25vh', 'padding-top': '10px', 'box-sizing': 'border-box'}
            # ),
            #     dcc.Graph(
            #         id = 'grafico_area2',
            #         figure = fig_area,
            #         config = {'displaylogo': False, 'displayModeBar': False, 'staticPlot': True},
            #         style = {'width': '50%', 'height': '25vh','padding-top': '10px', 'box-sizing': 'border-box'}
            #     )
            #  style = {'display': 'flex', 'height': '100%', 'width': '100%'}    
        ),
        
        html.Div(
            id = 'layout_graphics_lower'
            # dcc.Graph(
            #         id = 'grafico_area2',
            #         figure = fig_area,
            #         style = {'height': '25vh', 'width': '50%', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
            #         config = {'displaylogo': False, 'displayModeBar': False, 'staticPlot': True}
            #     ),
            # dcc.Graph(
            #     id='grafico_bar2',
            #     figure=fig_bar,
            #     style = {'height': '25vh', 'width': '50%', 'padding-top': '10px', 'box-sizing': 'border-box', 'padding-bottom': '10px'},
            #     config={'displaylogo': False,'displayModeBar': False, 'staticPlot': True},
            # )
        # , style = {'display': 'flex', 'height': '100%', 'width': '100%'}
        )
        
    ], id = 'div-lower-graphics')
    
], style = {'height': '100vh ', 'display': 'flex !important'})