from app_instance import app
from dash import dcc, html, Input, Output
import dashboard_vendas.layout_vendas as layout_vendas
import layoutConfig.layout_config as layout_config
import dashboard_logistica.layout_logistica as layout_logistica
import dashboardProducao.layoutProducao as layoutProducao
from datas import dataDashboards

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),  
    html.Div(id="page-content")              
])

app.title = 'Elite Board'
# app.sidebar = layout_view.sidebar

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/vendas":
        import route_vendas.atualizarDatasVendas
        return layout_vendas.layout_vendas
    elif pathname == '/config':
        # return layout_config.layout_config
        return layout_config.layoutConfig
    elif pathname == "/logistica":
        import route_logistica.atualizarDatasLogistica
        return layout_logistica.layout_logistica
    elif pathname == "/producao":
        return layoutProducao.layoutProducao
    else:
        return html.H1("404 - Página não encontrada")

if __name__ == '__main__':
    app.index_string = '''
    <!DOCTYPE html>
    <html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        <link rel="shortcut icon" href="/assets/favicon.ico" type="image/x-icon" />
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
    </html>
    '''

    app.run(debug=True)
    