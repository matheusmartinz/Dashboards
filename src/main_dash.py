from app_instance import app
from dash import dcc, html, Input, Output
import dashboard_vendas.layout_vendas as layout_vendas
import layout_config
import dashboard_logistica.layout_logistica as layout_logistica
import callbacks  

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  
    html.Div(id="page-content")              
])
# app.sidebar = layout_view.sidebar

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/vendas":
        return layout_vendas.layout_vendas
    elif pathname == '/config':
        # return layout_config.layout_config
        return layout_config.layoutConfig
    elif pathname == "/logistica":
        return layout_logistica.layout_logistica
    else:
        return html.H1("404 - Página não encontrada")

if __name__ == '__main__':
    app.run(debug=True)
