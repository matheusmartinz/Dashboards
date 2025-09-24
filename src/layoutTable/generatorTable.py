from dash import dash_table, Dash, html
from layoutTable import stylesTable
from typing import List, Dict, Union

def generatorTable(dataTable, columnsTable: Union[List[Dict], None]):
    
    return dash_table.DataTable(
        id = 'table-elite',
        data = dataTable,
        columns = columnsTable,
        # merge_duplicate_headers = True,
        fixed_rows = {'headers': True, 'data': 0},
    
        style_table = stylesTable.styleTable,
    
        # style_cell_conditional = stylesTable.styleCelulaConditional,
    
        style_cell = stylesTable.styleCelula,

        style_header = stylesTable.styleHeader,
)
    
def create_table(data, columns):
    # Cabeçalho
    header = html.Thead(
        html.Tr(
            [html.Th(col["name"]) for col in columns]
        )
    )
    
    # Corpo da tabela
    celulas = html.Tbody([
        html.Tr([html.Td(
            row.get(col['id'], '')
        ) for col in columns]) for row in data
    ])
    
    return html.Table(
        id = 'table-elite',
        children = [header, celulas], 
        className='custom-table',
        style={'width': '100%', 'borderCollapse': 'collapse'}
    )   