from dash.dependencies import Input, Output, State
from dash import callback_context as ctx
from app_instance import app
import graphics_dash
import layout_dash

figs = [graphics_dash.graph_bar, graphics_dash.graph_line, graphics_dash.graph_pie]

@app.callback(
    Output('grafico_bar', 'figure'),
    Input('store-switch-value', 'data'),
    Input('meu_timer', 'n_intervals')
)
def atualizar_grafico(valor_switch, n):
    if valor_switch == 1:
        return updateGraphic(n)
    else:
        return graphics_dash.graph_bar

def updateGraphic(time):
    index = time % len(figs)
    return figs[index]

@app.callback( 
    Output('sidebar', 'style'),
    Input('btn-icon-open', 'n_clicks'),
    Input('btn-close-sidebar', 'n_clicks'),
    State('sidebar', 'style')
)
def toggle_sidebar(open_clicks, close_clicks, current_style):
    trigger = ctx.triggered_id
    if current_style is None:
        current_style = {'transform': 'translateX(-100%)'}
    if trigger == 'btn-icon-open':
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
    Output('radio-container', 'children'),
    Input('switch-automatic-graphics', 'value'),
    prevent_initial_call=True
)
def construct_radio(switch_value):
    if switch_value and 1 in switch_value:
        return layout_dash.radio
    return None

@app.callback(
    Output('meu_timer','interval'),
    Input('radioitems-input', 'value'),
    prevent_initial_call=True
)    
def update_interval(selected_value):
    if selected_value:
        return selected_value * 1000
    return 1000

@app.callback( 
    Output('config-dialog','is_open'),
    Input('btn-config', 'n_clicks'),
    prevent_initial_call=True
)
def open_dialog(click):
    if click: 
        return True
    return False
