from app_instance import app
from dash.dependencies import Input, Output, State

@app.callback(
    Output('table-elite', 'data'),
    Input('table-elite', 'filter_query')
)
def filterTable(filter, data):
    if not filter:
        return data.to_dict('records')
