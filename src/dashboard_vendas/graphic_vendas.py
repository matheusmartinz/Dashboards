from utils.updateGraphics import updateLayout
import datas.dataDashboards as dataDashboards
import plotly.graph_objects as go
from dash import dcc, dash_table  # type: ignore
from utils.colorsDashboards import cores_graficos
from components.CustomGraphics import CustomGraphics

data = dataDashboards.loadDataVendas()

DF = data["DF"]
DF_filtered_table = data["DF_filtered_table"]
DF_grouped = data["DF_grouped"]
max_valor = DF_grouped['Valor Final'].max()
DF_line = data["DF_line"]
max_valor_line = DF_line['Valor Unitário'].max()

 

graph_bar = CustomGraphics('bar', DF_grouped, horizontal = 'Data', vertical = 'Valor Final', color = 'Produto', color_discrete_sequence = cores_graficos)
updateLayout(graph_bar,'bar')

# graph_pie = px.pie(DF, names = 'Região Lojas', values = 'Valor Final', color = 'Região Lojas', color_discrete_sequence = cores_graficos)
# updateLayout(graph_pie, 'pie')

# graph_area = px.area(DF, x = 'Data', y = 'Valor Final', color = 'Produto')
# updateLayout(graph_area,'area')

# graph_line = px.line(DF_line, x='Data', y='Valor Unitário', color='Região Lojas', markers=True, line_shape='spline', color_discrete_sequence= cores_graficos)
graph_line = CustomGraphics('line', DF_line, horizontal = 'Data', vertical = 'Valor Unitário', color = 'Região Lojas', color_discrete_sequence = cores_graficos, markers = True, line_shape = 'spline')
updateLayout(graph_line, 'line')

# graph_histogram = px.histogram(DF, x='Produto', y='Valor Final', color='Produto', color_discrete_sequence= cores_graficos)
# updateLayout(graph_histogram, 'histogram')

graph_table = go.Figure(data=[go.Table(
        columnwidth=[2, 2, 1],
        header=dict(
            values=list(DF_filtered_table.columns),
            fill_color='#00BCD4',
            align='left',
            font=dict(color='white', size=13),
        ),
        cells=dict(
            values=[DF_filtered_table[col] for col in DF_filtered_table.columns],
            fill_color='lavender',
            align='left',
            font=dict(color='black', size=12),
        )
    )])
updateLayout(graph_table, 'table')

data_table = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in DF_filtered_table.columns],
        data=DF_filtered_table.to_dict('records'),
        style_table={
            'height': '35vh',
            'overflowY': 'auto',
        },
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'fontFamily': 'Arial',
            'fontSize': '13px',
        },
        style_header={
            'backgroundColor': '#263c2b',
            'color': 'white',
            'fontWeight': 'bold'
        }
    )