from app_instance import app
import layout_dash
import callbacks  

app.layout = layout_dash.layout
app.sidebar = layout_dash.sidebar

if __name__ == '__main__':
    app.run(debug=True)
