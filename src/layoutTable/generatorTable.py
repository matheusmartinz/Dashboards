from dash import dash_table
from layoutTable import stylesTable
from typing import List, Dict, Union

def generatorTable(dataTable, columnsTable: Union[List[Dict], None]):
   return dash_table.DataTable(
    id = 'table-elite',
    data = dataTable,
    columns = columnsTable,
    merge_duplicate_headers = True,
    fixed_rows={'headers': True},
    filter_action= 'native',
    filter_options = {'case': 'insensitive'},
    
    style_table = stylesTable.styleTable,
    
    style_cell_conditional = stylesTable.styleCelulaConditional,
    
    style_cell = stylesTable.styleCelula,

    style_header = stylesTable.styleHeader,
    
)