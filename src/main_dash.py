import dash # type: ignore
import dash_bootstrap_components as dbc # type: ignore
import layout_dash
from dash.dependencies import Input, Output, State # type: ignore
import graphics_dash
from dash import callback_context as ctx # type: ignore

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"])

app.layout = layout_dash.layout
app.sidebar = layout_dash.sidebar

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
    print(index)
    return figs[index]


@app.callback( 
    Output('sidebar', 'style'), # OUTPUT - quem será atualizado - mexido
    Input('btn-icon-open', 'n_clicks'), # INPUT - o que vai dar o gatilho para mudar o elemento
    Input('btn-close-sidebar', 'n_clicks'),
    State('sidebar', 'style')
)

def toggle_sidebar(open_clicks, close_clicks, current_style):
    trigger = ctx.triggered_id

    if current_style is None:
        current_style = {
            'transform': 'translateX(-100%)'
        }
    if trigger == 'btn-icon-open':
        current_style['transform'] = 'translateX(0%)'
    elif trigger == 'btn-close-sidebar':
        current_style['transform'] = 'translateX(-100%)'
    return current_style;


@app.callback(
    Output('store-switch-value', 'data'),
    Input('switch-automatic-graphics', 'value')
)

def toggle_switch_value(value):
    return 1 if 1 in value else 0

# @app.calback(
#     Output('radio-items-input', 'value'),
#     Input('')
# )


def main():
    print('Teste: aplicação Dash está rodando')
if __name__ == '__main__':
    app.run(debug=True)
