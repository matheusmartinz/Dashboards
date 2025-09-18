from app_instance import app
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import dash
from utils.colorsDashboards import cores_graficos
from datas.dataDashboards import loadDataVendas, loadDataLogistica
from dashboard_vendas.graphic_vendas import CustomGraphics, updateLayout


@app.callback(
    Output('store-dados-graficos-vendas', 'data'),
    Input('interval-atualizacao-vendas', 'n_intervals'),
    prevent_initial_call = True
)
def atualizarDadosGraficos(n_vendas):
    dadosVendas = loadDataVendas()
    
    dadosVendas =  {
        'DF_line': dadosVendas['DF_line'].to_dict('records'),
        'DF_grouped': dadosVendas['DF_grouped'].to_dict('records'),
    }
    
    return dadosVendas

@app.callback(
    # Output('grafico_line', 'figure'),
    Output('grafico_bar', 'figure'),
    Input('store-dados-graficos-vendas', 'data'),
    prevent_initial_call = True
)
def atualizar_graficos_fulltime_vendas(data):
    if (not data):
        raise dash.exceptions.PreventUpdate
    
    df_line = pd.DataFrame(data['DF_line'])
    df_bar = pd.DataFrame(data['DF_grouped'])
    
    fig_line = CustomGraphics('line', df_line, horizontal='Data', vertical='Custo Frete', color='Região Lojas', color_discrete_sequence= cores_graficos, markers=True, line_shape='spline')
    updateLayout(fig_line, 'line')
    fig_line.update_traces(
        hovertemplate=(
        'Data: %{x}<br>' +\
        'Região Lojas: %{fullData.name}<br>' +     
        'Custo Frete: R$ %{y:.2f}<br>' +
        '<extra></extra>'
    )
    )

    fig_bar = CustomGraphics('bar', df_bar, horizontal='Data', vertical='Valor Final', color='Produto', color_discrete_sequence=cores_graficos)
    updateLayout(fig_bar, 'bar')
    fig_bar.update_traces(
        hovertemplate = (
        'Data: %{x}<br>' +\
        'Produto: %{fullData.name}<br>' +     
        'Valor Final: R$ %{y:.2f}<br>' +
        '<extra></extra>'
        )
    )

    return fig_line, fig_bar