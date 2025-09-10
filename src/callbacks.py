from dash.dependencies import Input, Output, State
from dash import callback_context as ctx
from dash import dcc
from app_instance import app
from proportions.proportions_dashboards import layouts_by_proportion
import dashboard_vendas.graphic_vendas as graphic_vendas
import dash

figs = [graphic_vendas.graph_bar, graphic_vendas.graph_line, graphic_vendas.graph_pie]

@app.callback(
    Output('grafico_bar', 'figure'),
    Input('store-switch-value', 'data'),
    Input('meu_timer', 'n_intervals')
)
def atualizar_grafico(valor_switch, n):
    if valor_switch == 1:
        return updateGraphic(n)
    else:
        return graphic_vendas.graph_bar

def updateGraphic(time):
    index = time % len(figs)
    return figs[index]

@app.callback(
    Output('radioitens-input', 'options'),
    Input('switch-automatic-graphics', 'value'),
    prevent_initial_call = True
)
def toggle_radio_disabled(switch_value):
    disabled = not (switch_value and 1 in switch_value)
    return [
        {'label': '10s', 'value': 10, 'disabled': disabled},
        {'label': '20s', 'value': 20, 'disabled': disabled},
        {'label': '30s', 'value': 30, 'disabled': disabled},
    ]

@app.callback( 
    Output('sidebar', 'style'),
    Input('btn-open-sidebar', 'n_clicks'),
    Input('btn-close-sidebar', 'n_clicks'),
    State('sidebar', 'style')
)
def toggle_sidebar(open_clicks, close_clicks, current_style):
    trigger = ctx.triggered_id
    if current_style is None:
        current_style = {'transform': 'translateX(-100%)'}
    if trigger == 'btn-open-sidebar':
        current_style['transform'] = 'translateX(0%)'
    elif trigger == 'btn-close-sidebar':
        current_style['transform'] = 'translateX(-100%)'
    return current_style

@app.callback(
    Output('store-switch-value', 'data'),
    Input('switch-automatic-graphics', 'value')
)
def toggle_switch_value(value):
    return 1 if 1 in value else 0

@app.callback(
    Output('meu_timer','interval'),
    Output('store-tempo-definido', 'data'),
    Input('radioitens-input', 'value'),
    State('store-switch-value', 'data'),
    prevent_initial_call=True
)
def handle_radio_and_interval(selected_value, switch_value):
    tempo_definido = True if selected_value else False
    if switch_value == 1 and tempo_definido:
        return selected_value * 1000, tempo_definido
    else:
        return 9999999999, tempo_definido

@app.callback(
    Output('radioitens-input', 'value'),
    Input('switch-automatic-graphics', 'value'),
    prevent_initial_call = True
)
def reset_radio_value(switch_value):
    if not switch_value or 1 not in switch_value:
        return None
    return dash.no_update

@app.callback( 
    Output('config-dialog','is_open'),
    Input('btn-layout', 'n_clicks'),
    prevent_initial_call=True
)
def open_dialog(click):
    if click: 
        return True
    return False

@app.callback(
    Output('download_dataframe_csv', 'data'),
    Output('confirm-dialog-download', 'is_open'),
    Input('button_export', 'n_clicks'),
    Input('cancel-button', 'n_clicks'),
    Input('accept-button', 'n_clicks'),
    State('confirm-dialog-download', 'is_open'),
    prevent_initial_call=True
)
def handle_modal_and_download(export_clicks, cancel_clicks, accept_clicks, is_open):
    triggered_id = ctx.triggered_id

    if triggered_id == 'button_export':
        return dash.no_update, True  

    elif triggered_id == 'cancel-button':
        return dash.no_update, False  

    elif triggered_id == 'accept-button':
        return (
            dcc.send_data_frame(DF.to_csv, 'dados_exportados.csv', index=False),
            False  
        )

    return dash.no_update, is_open

@app.callback(
    Output('layout_graphics_top', 'children'),
    Output('layout_graphics_lower', 'children'),
    Input('select_layout', 'value')
)
def proporcao_graficos(proporcao):
    return layouts_by_proportion(proporcao)