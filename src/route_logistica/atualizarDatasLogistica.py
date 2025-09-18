from app_instance import app
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import dash
from utils.colorsDashboards import cores_graficos
from datas.dataDashboards import loadDataLogistica
from utils.formaterToReal import formaterToReal
from dashboard_vendas.graphic_vendas import CustomGraphics, updateLayout


@app.callback(
    Output('store-dados-logistica', 'data'),
    Input('interval-atualizacao-logistica', 'n_intervals'),
)
def atualizarDadosGraficos(n_logistica):
    dadosLogistica = loadDataLogistica()
    
    dadosLogistica = {
        'DF_grouped_line': dadosLogistica['DF_grouped_line'].to_dict('records'),
        'DF_grouped_CDPeso': dadosLogistica['DF_grouped_CDPeso'].to_dict('records'),
        'DF_pie': dadosLogistica['DF'].to_dict('records')
    }
    
    return dadosLogistica

@app.callback(
    Output('grafico_line_logistica', 'figure'),
    Output('grafico_histogram_logistica', 'figure'),
    Output('grafico_donut_logistica', 'figure'),
    Input('store-dados-logistica', 'data')
)
def atualizar_graficos_fulltime_logistica(data):
    if (not data):
        raise dash.exceptions.PreventUpdate
    
    df_line = pd.DataFrame(data['DF_grouped_line'])
    df_histogram = pd.DataFrame(data['DF_grouped_CDPeso'])
    df_donut = pd.DataFrame(data['DF_pie'])
    
    fig_line = CustomGraphics(chart_type='line', data= df_line, horizontal='Data Saída', vertical='Custo Frete', color='Tipo de Carga', line_shape='spline',
                                markers=True, color_discrete_sequence=cores_graficos, custom_data=['Custo Frete Formatado'])
    updateLayout(fig_line, 'line')
    fig_line.update_traces(
        hovertemplate=(
            'Data Saída: %{x}<br>' +
            'Tipo de Carga: %{fullData.name}<br>' +
            'Custo Frete: R$ %{customdata[0]}<br>' +
            '<extra></extra>'
        )
    )
        
    fig_donut = CustomGraphics(chart_type='pie', data= df_donut, names='Tipo de Carga', values='Peso', hole=0.4, color_discrete_sequence=cores_graficos)
    updateLayout(fig_donut, 'pie')
    fig_donut.update_traces(
        hovertemplate=('%{label}: %{value} kg (<b>%{percent}</b>)<extra></extra>')
    )

    
    fig_histogram = CustomGraphics(chart_type='histogram', data = df_histogram, horizontal='Centro de Distribuição', vertical='Peso', 
                                   color='Tipo de Carga', color_discrete_sequence=cores_graficos)
    updateLayout(fig_histogram, 'histogram')
    fig_histogram.update_traces(
        hovertemplate=(
            'CD: %{x}<br>' +
            'Tipo de Carga: %{fullData.name}<br>' +
            'Peso: %{y} kg<br>' +
            '<extra></extra>'
        )
    )
    
    return fig_line, fig_histogram, fig_donut