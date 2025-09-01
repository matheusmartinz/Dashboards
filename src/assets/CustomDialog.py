import dash_bootstrap_components as dbc 

def CustomDialog(headerText: str, btn_left_text: str, btn_right_text: str, id_btn_left: str, id_btn_right: str, clicks: int, id_modal: str, open: bool, className = str):
    return dbc.Modal([
        dbc.ModalHeader(headerText),
        dbc.ModalFooter([
        dbc.Button(btn_left_text, id = id_btn_left, className = className, n_clicks = clicks),
        dbc.Button(btn_right_text, id = id_btn_right, className = className, n_clicks = clicks),
        ])
    ], id=id_modal, is_open = open)