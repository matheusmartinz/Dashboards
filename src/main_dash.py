from app_instance import app
from dash import dcc, html, Input, Output
import layout_view
import layout_config
import callbacks  

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  
    html.Div(id="page-content")              
])
app.sidebar = layout_view.sidebar

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/view":
        return layout_view.layout_view
    elif pathname == '/config':
        # return layout_config.layout_config
        return layout_config.layoutConfig
    else:
        return html.H1("404 - Página não encontrada")

if __name__ == '__main__':
    app.run(debug=True)
