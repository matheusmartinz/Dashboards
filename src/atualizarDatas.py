from app_instance import app
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import dash
from utils.colorsDashboards import cores_graficos
from datas.dataDashboards import loadDataVendas
from dashboard_vendas.graphic_vendas import CustomGraphics, updateLayout


@app.callback(
    Output('store-dados-graficos', 'data'),
    Input('interval-atualizacao', 'n_intervals')
)
def atualizarDadosGraficos(n):
    dados = loadDataVendas()
    return {
        'DF_line': dados['DF_line'].to_dict('records'),
        'DF_grouped': dados['DF_grouped'].to_dict('records'),
    }

@app.callback(
    Output('grafico_line', 'figure'),
    Output('grafico_bar', 'figure'),
    Input('store-dados-graficos', 'data'),
)

def atualizar_graficos_em_tempo_real(data):
    if (not data):
        raise dash.exceptions.PreventUpdate
    
    df_line = pd.DataFrame(data['DF_line'])
    df_bar = pd.DataFrame(data['DF_grouped'])
    
    fig_line = CustomGraphics('line', df_line, horizontal='Data', vertical='Valor Unitário', color='Região Lojas', color_discrete_sequence= cores_graficos, markers=True, line_shape='spline')
    updateLayout(fig_line, 'line')

    fig_bar = CustomGraphics('bar', df_bar, horizontal='Data', vertical='Valor Final', color='Produto', color_discrete_sequence=cores_graficos)
    updateLayout(fig_bar, 'bar')

    return fig_line, fig_bar
