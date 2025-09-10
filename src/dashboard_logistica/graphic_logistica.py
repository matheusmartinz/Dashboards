from utils.updateGraphics import updateLayout
from dataDashboards import loadDataLogistica
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, dash_table  # type: ignore

DF = loadDataLogistica()
cores_graficos = ['#00BCD4', '#FF5722', '#4CAF50', '#8E24AA', '#D32F2F', '#1E88E5','#FFC107','#009688','#9C27B0','#F44336','#3F51B5', '#795548']
DF_grouped = DF.groupby(['Data Saída', 'Tipo de Carga'], as_index=False)['Peso'].sum()

# Soma total por dia
peso_total_por_data = DF_grouped.groupby('Data Saída')['Peso'].transform('sum')

# Calcula a porcentagem
DF_grouped['Peso %'] = DF_grouped['Peso'] / peso_total_por_data * 100

graph_bar = px.bar(DF, x='Data Saída', y = 'Custo Frete', color = 'Tipo de Carga', color_discrete_sequence = cores_graficos)
updateLayout(graph_bar,'bar')

# graph_pie = px.pie(DF, names = 'Destino', values = 'Custo Frete', color = 'Destino', color_discrete_sequence = cores_graficos)
# updateLayout(graph_pie, 'pie')

graph_area = px.area(DF, x = 'Data Saída', y = 'Peso', color = 'Código Entrega',line_group = 'Tipo de Carga', color_discrete_sequence = cores_graficos)
updateLayout(graph_area,'area')

graph_line = px.line(DF, x='Data Saída', y='Custo Frete', color='Tipo de Carga',line_shape='spline' ,markers=True, color_discrete_sequence = cores_graficos)
updateLayout(graph_line,'line')

graph_histogram = px.histogram(DF, x='Tipo de Carga', y='Peso', color='Tipo de Carga', color_discrete_sequence= cores_graficos)
updateLayout(graph_histogram, 'histogram')

graph_donut = px.pie(DF, names='Tipo de Carga', values='Peso', hole=0.4, color_discrete_sequence=cores_graficos)
updateLayout(graph_donut, 'pie')



# graph_geo = px.scatter_geo(DF, locations="Destino", locationmode='country names', color="Tipo de Carga",
#                      hover_name="Código Entrega", size="Peso",
#                      projection="natural earth", color_discrete_sequence=cores_graficos)
# graph_geo.update_geos(showland=True, landcolor="LightGreen")
# graph_geo.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor = '#FEFAE0')

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