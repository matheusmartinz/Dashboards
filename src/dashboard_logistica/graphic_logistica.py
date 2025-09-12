from utils.updateGraphics import updateLayout
from datas.dataDashboards import loadDataLogistica
from components.CustomGraphics import CustomGraphics
import plotly.express as px
import utils.colorsDashboards as colors
import plotly.graph_objects as go
from dash import dcc, dash_table  # type: ignore

colors_graficos = colors.cores_graficos

data = loadDataLogistica()

DF = data["DF"]
DF_grouped_line = data["DF_grouped_line"]
DF_grouped_CDPeso = data["DF_grouped_CDPeso"]

DF_grouped_CDPeso = DF.groupby(['Centro de Distribuição', 'Tipo de Carga'], as_index=False)['Peso'].sum()

# graph_line = CustomGraphics(chart_type='line', data=DF_grouped_line, horizontal='Data Saída', vertical='Custo Frete', color='Tipo de Carga', line_shape='spline', markers=True, color_discrete_sequence=colors_graficos)
graph_line = px.line(
    DF_grouped_line,
    x='Data Saída',                 #VER O PQ A MERDA DO CUSTOM NAO TA PEGANDO OS VALORES E SETANDO CERTINHO AQUI NO GRAPHIC_LOGISTA, NAO FAZ SENTIDO
    y='Custo Frete',
    color='Tipo de Carga',
    line_shape='spline',
    markers=True,
    title='Custo de Frete por Tipo de Carga e Data'
)
updateLayout(graph_line,'line')
# graph_line.update_traces(
#     customdata= DF_grouped_line[['Tipo de Carga']], #OS VALORES NAO ESTAO BATENDO O TIPO DE CARGA E SEU CUSTO FRETE / OLHAR ISSO
#     hovertemplate=(
#         'Data Saída: %{x}<br>' +
#         'Tipo de Carga: %{customdata[0]}<br>' +     
#         'Custo Frete: %{y}<br>' +
#         '<extra></extra>'
#     )
# )

graph_histogram = CustomGraphics(chart_type='histogram', data = DF_grouped_CDPeso, horizontal='Centro de Distribuição', vertical='Peso', color='Tipo de Carga', color_discrete_sequence=colors_graficos)
updateLayout(graph_histogram, 'histogram')
graph_histogram.update_traces(
    customdata=DF_grouped_CDPeso[['Tipo de Carga']],
    hovertemplate=(
        'CD: %{x}<br>' +
        'Tipo de Carga: %{customdata[0]}<br>' +
        'Peso Total: %{y} kg<extra></extra>'
    )
)

graph_donut = CustomGraphics(chart_type='pie', data=DF, names='Tipo de Carga', values='Peso', hole=0.4, color_discrete_sequence=colors_graficos)
updateLayout(graph_donut, 'pie')
graph_donut.update_traces(
    hovertemplate='%{label}: %{value} kg (<b>%{percent}</b>)<extra></extra>',
)

# graph_table = go.Figure(data=[go.Table(
#         columnwidth=[2, 2, 1],
#         header=dict(
#             values=list(DF_filtered_table.columns),
#             fill_color='#00BCD4',
#             align='left',
#             font=dict(color='white', size=13),
#         ),
#         cells=dict(
#             values=[DF_filtered_table[col] for col in DF_filtered_table.columns],
#             fill_color='lavender',
#             align='left',
#             font=dict(color='black', size=12),
#         )
#     )])
# updateLayout(graph_table, 'table')

# data_table = dash_table.DataTable(
#         columns=[{"name": i, "id": i} for i in DF_filtered_table.columns],
#         data=DF_filtered_table.to_dict('records'),
#         style_table={
#             'height': '35vh',
#             'overflowY': 'auto',
#         },
#         style_cell={
#             'textAlign': 'left',
#             'padding': '5px',
#             'fontFamily': 'Arial',
#             'fontSize': '13px',
#         },
#         style_header={
#             'backgroundColor': '#263c2b',
#             'color': 'white',
#             'fontWeight': 'bold'
#         }
#     )