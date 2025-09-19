from utils.updateGraphics import updateLayout
import datas.dataDashboards as dataDashboards
import plotly.graph_objects as go
from dash import dcc, dash_table  # type: ignore
from utils.colorsDashboards import cores_graficos
from utils.formaterToReal import formaterToReal
from components.CustomGraphics import CustomGraphics
from dash.dash_table.Format import Format, Group, Scheme, Symbol

data = dataDashboards.loadDataVendas()
dataTable = dataDashboards.loadDataElite()

DF = data["DF"]
DF_filtered_table = data["DF_filtered_table"]
DF_grouped = data["DF_grouped"]
DF_line = data["DF_line"]


graph_bar = CustomGraphics('bar', DF_grouped, horizontal = 'Data', vertical = 'Valor Final', color = 'Produto',
                           color_discrete_sequence = cores_graficos, custom_data = ['Valor Final Formatado'], barmode = 'relative')
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

def generationTable(data):
 data_table = dash_table.DataTable(
    data = data['resumo'],
    columns=[
    {"name": ["Elite Board", "Coleção"], "id": "Coleção"},
    {"name": ["Elite Board", "Previsto"], "id": "Previsto", "type": "numeric"},
    {"name": ["Elite Board", "Criados"], "id": "Criados", "type": "text"},
    {"name": ["Andamento das coleções", "Não iniciado"], "id": "Não iniciado", "type": "text"},
    {"name": ["Andamento das coleções", "Desenvolvimento"], "id": "Desenvolvimento", "type": "text"},
    {"name": ["Andamento das coleções", "Aprovado"], "id": "Aprovado", "type": "text"},
    {"name": ["Andamento das coleções", "Reprovado"], "id": "Reprovado", "type": "text"},
    {"name": ["Andamento das coleções", "Cancelado"], "id": "Cancelado", "type": "text"},
],
    merge_duplicate_headers=True,
    fixed_rows={'headers': True},
    
    style_table={
        'height': '45vh',
        'overflowX': 'auto',       
        'overflowY': 'auto',
        'width': '100%',
    },
    
    style_cell_conditional= [
        {
        'if': {'column_id': 'Desenvolvimento'},
        'width': '12%',
        },
        {
        'if': {'column_id': 'Desenvolvimento %'},
        'width': '12%',
        }
    ],
    
    style_cell={
        'textAlign': 'center',
        'padding': '5px',
        'fontFamily': 'Arial',
        'whiteSpace': 'normal',
        'minWidth': '100px',       
        'width': '100px',
        'maxWidth': '200px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },

    style_header={
        'backgroundColor': '#263c2b',
        'color': 'white',
        'fontWeight': 'bold',
        'whiteSpace': 'normal',
    },
)
 return data_table


data_table = dash_table.DataTable(
    data = dataTable['resumo'],
    columns=[
    {"name": ["Elite Board", "Coleção"], "id": "Coleção"},
    {"name": ["Elite Board", "Previsto"], "id": "Previsto", "type": "numeric"},
    {"name": ["Elite Board", "Criados"], "id": "Criados", "type": "text"},
    {"name": ["Andamento das coleções", "Não iniciado"], "id": "Não iniciado", "type": "text"},
    {"name": ["Andamento das coleções", "Desenvolvimento"], "id": "Desenvolvimento", "type": "text"},
    {"name": ["Andamento das coleções", "Aprovado"], "id": "Aprovado", "type": "text"},
    {"name": ["Andamento das coleções", "Reprovado"], "id": "Reprovado", "type": "text"},
    {"name": ["Andamento das coleções", "Cancelado"], "id": "Cancelado", "type": "text"},
],
    merge_duplicate_headers=True,
    fixed_rows={'headers': True},
    
    style_table={
        'height': '45vh',
        'overflowX': 'auto',       
        'overflowY': 'auto',
        'width': '100%',
    },
    
    style_cell_conditional= [
        {
        'if': {'column_id': 'Desenvolvimento'},
        'width': '12%',
        },
        {
        'if': {'column_id': 'Desenvolvimento %'},
        'width': '12%',
        }
    ],
    
    style_cell={
        'textAlign': 'center',
        'padding': '5px',
        'fontFamily': 'Arial',
        'whiteSpace': 'normal',
        'minWidth': '100px',       
        'width': '100px',
        'maxWidth': '200px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },

    style_header={
        'backgroundColor': '#263c2b',
        'color': 'white',
        'fontWeight': 'bold',
        'whiteSpace': 'normal',
    },
)

