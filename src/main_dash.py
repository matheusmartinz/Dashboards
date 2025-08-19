import dash # type: ignore
import dash_bootstrap_components as dbc # type: ignore
import layout_dash

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"])

app.layout = layout_dash.layout



def main():
    print('Teste: aplicação Dash está rodando')
if __name__ == '__main__':
    main() 
    app.run(debug=True)
