from utils.updateGraphics import updateLayout
from datas.dataDashboards import loadDataLogistica
from components.CustomGraphics import CustomGraphics
import plotly.express as px
import utils.colorsDashboards as colors
import plotly.graph_objects as go
from dash import dcc, dash_table  # type: ignore

DF = loadDataLogistica()
colors_graficos = colors.cores_graficos
DF_grouped = DF.groupby(['Data Saída', 'Tipo de Carga'], as_index=False)['Peso'].sum()

peso_total_por_data = DF_grouped.groupby('Data Saída')['Peso'].transform('sum')
DF_grouped = DF.groupby(['Data Saída', 'Tipo de Carga'])['Custo Frete'].sum().reset_index()


# graph_bar = px.bar(DF, x='Data Saída', y = 'Custo Frete', color = 'Tipo de Carga', color_discrete_sequence = colors_graficos)
# updateLayout(graph_bar,'bar')

# graph_pie = px.pie(DF, names = 'Destino', values = 'Custo Frete', color = 'Destino', color_discrete_sequence = cores_graficos)
# updateLayout(graph_pie, 'pie')

# graph_area = px.area(DF, x = 'Data Saída', y = 'Peso', color = 'Código Entrega',line_group = 'Tipo de Carga', color_discrete_sequence = colors_graficos)
# updateLayout(graph_area,'area')

# graph_line = px.line(DF_grouped, x='Data Saída', y='Custo Frete', color='Tipo de Carga',line_shape='spline' ,markers=True, color_discrete_sequence = colors_graficos)
graph_line = CustomGraphics(chart_type='line', data=DF_grouped, horizontal='Data Saída', vertical='Custo Frete', color='Tipo de Carga', line_shape='spline', markers=True, color_discrete_sequence=colors_graficos)
updateLayout(graph_line,'line')
# graph_line.update_traces(
#     customdata = DF_grouped[['Tipo de Carga']],
#     hovertemplate=('Data: %{x}<br>' +
#                    'Tipo de Carga: %{customdata[0]}<br>' +
#                    'Custo Frete: %{y:$,.2f}<br>' +
#                    '<extra></extra>')
# )

# graph_histogram = px.histogram(DF, x='Destino', y='Peso', color='Tipo de Carga', color_discrete_sequence= colors_graficos)
graph_histogram = CustomGraphics(chart_type='histogram', data=DF, horizontal='Destino', vertical='Peso', color='Tipo de Carga', color_discrete_sequence=colors_graficos)
updateLayout(graph_histogram, 'histogram')
graph_histogram.update_traces(
    customdata=DF_grouped[['Tipo de Carga']],
    hovertemplate=(
        'Data: %{x}<br>' +
        'Tipo de Carga: %{customdata[0]}<br>' +
        'Peso: %{y} kg<extra></extra>'
    )
)

# graph_donut = px.pie(DF, names='Tipo de Carga', values='Peso', hole=0.4, color_discrete_sequence=colors_graficos)
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