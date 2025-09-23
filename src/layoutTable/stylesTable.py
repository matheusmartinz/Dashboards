styleTable = {
        'height': '45vh',
        'overflowX': 'auto',       
        'overflowY': 'auto',
        'whiteSpace': 'nowrap',
        'tableLayout': 'fixed',
        'width': '100%',
        'minWidth': '1000px'
    }
    
styleCelulaConditional = [
    {'if': {'column_id': 'Coleção'}, 'width': '140px'},
    {'if': {'column_id': 'Previsto'}, 'width': '99px'},
    {'if': {'column_id': 'Criados'}, 'width': '100px'},
    {'if': {'column_id': 'Não iniciado'}, 'width': '110px'},
    {'if': {'column_id': 'Desenvolvimento'}, 'width': '120px'}, 
    {'if': {'column_id': 'Aprovado'}, 'width': '119px'},
    {'if': {'column_id': 'Reprovado'}, 'width': '120px'},
    {'if': {'column_id': 'Cancelado'}, 'width': '110px'},
]
    
styleCelula = {
    'textAlign': 'center',
    'whiteSpace': 'nowrap',
    'overflow': 'hidden',
    'textOverflow': 'ellipsis',
    'padding': '5px',
    'fontFamily': 'Arial',
    'border': '1px solid #ccc',
    'width': '100px',
    'minWidth': '100px',
    'maxWidth': '100px'
}

styleHeader = {
    'backgroundColor': '#263c2b',
    'color': 'white',
    'fontWeight': 'bold',
    'border': '1px solid #ccc',
    'whiteSpace': 'nowrap'
    }
