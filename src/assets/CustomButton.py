from dash import html

def CustomButton( idButton: str, textButton: str = None, clicks: int = None, nameIcon: str = None, idIcon: str = None):
        children = []
        
        if (nameIcon and idIcon):
            children.append(html.I(className = nameIcon, id = idIcon))
            
        if (textButton):
            children.append(textButton)
            
        return html.Button(children, id = idButton, n_clicks = clicks)