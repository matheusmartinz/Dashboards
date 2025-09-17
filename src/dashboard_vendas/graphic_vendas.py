from utils.updateGraphics import updateLayout
import datas.dataDashboards as dataDashboards
import plotly.graph_objects as go
from dash import dcc, dash_table  # type: ignore
from utils.colorsDashboards import cores_graficos
from utils.formaterToReal import formaterToReal
from components.CustomGraphics import CustomGraphics
from dash.dash_table.Format import Format, Group, Scheme, Symbol

data = dataDashboards.loadDataVendas()

DF = data["DF"]
DF_filtered_table = data["DF_filtered_table"]
DF_grouped = data["DF_grouped"]
DF_line = data["DF_line"]

graph_bar = CustomGraphics('bar', DF_grouped, horizontal = 'Data', vertical = 'Valor Final', color = 'Produto',
                           color_discrete_sequence = cores_graficos, custom_data = ['Valor Final Formatado'])
updateLayout(graph_bar,'bar')
graph_bar.update_traces(
    hovertemplate=(
        'Data Saída: %{x}<br>' +\
        'Produto: %{fullData.name}<br>' +     
        'Custo Frete: R$ %{customdata[0]}<br>' +
        '<extra></extra>'
    )
)

# graph_pie = px.pie(DF, names = 'Região Lojas', values = 'Valor Final', color = 'Região Lojas', color_discrete_sequence = cores_graficos)
# updateLayout(graph_pie, 'pie')

# graph_area = px.area(DF, x = 'Data', y = 'Valor Final', color = 'Produto')
# updateLayout(graph_area,'area')

# graph_line = px.line(DF_line, x='Data', y='Valor Unitário', color='Região Lojas', markers=True, line_shape='spline', color_discrete_sequence= cores_graficos)
graph_line = CustomGraphics('line', DF_line, horizontal = 'Data', vertical = 'Custo Frete', color = 'Região Lojas', color_discrete_sequence = cores_graficos,
                            markers = True, line_shape = 'spline', custom_data = 'Custo Frete Formatado')
updateLayout(graph_line, 'line')
graph_line.update_traces(
    hovertemplate=(
        'Data: %{x}<br>' +\
        'Região Lojas: %{fullData.name}<br>' +     
        'Custo Frete: R$ %{customdata[0]}<br>' +
        '<extra></extra>'
    )
)

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
            values=[
                DF_filtered_table["Data"],
                DF_filtered_table["Produto"],
                DF_filtered_table["Valor Final Formatado"]  
            ],
            fill_color='lavender',
            align='left',
            font=dict(color='black', size=12),
        )
    )])
updateLayout(graph_table, 'table')

data_table = dash_table.DataTable(
    columns=[
        {"name": "Data", "id": "Data"},
        {"name": "Produto", "id": "Produto"},
        {
            "name": "Valor Final",
            "id": "Valor Final",
            "type": "numeric",
            "format": Format(
                scheme=Scheme.fixed,
                precision=2,
                group=Group.yes,
                symbol=Symbol.yes,
                symbol_prefix="R$ "
            )
        }
    ],
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
