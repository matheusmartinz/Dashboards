import plotly.express as px
from typing import Optional, Any, List, Literal

def CustomGraphics(
    chart_type: Literal['bar', 'line', 'area', 'pie', 'histogram'],
    data: Any,
    horizontal: Optional[str] = None,
    vertical: Optional[str] = None,
    values: Optional[str] = None,
    names: Optional[str] = None,
    color: Optional[str] = None,
    line_group: Optional[str] = None,
    markers: Optional[bool] = False,
    **kwargs  # captura argumentos adicionais
):
    if (chart_type == 'bar'):
        return px.bar(data, x=horizontal, y=vertical, color=color, **kwargs)
    elif (chart_type == 'line'):
        return px.line(data, x=horizontal, y=vertical, color=color, line_group=line_group, markers=markers, **kwargs)
    elif (chart_type == 'area'):
        return px.area(data, x=horizontal, y=vertical, color=color, line_group=line_group,**kwargs)
    elif (chart_type == 'pie'):
        return px.pie(data, names=names, values=values, color=names, **kwargs)
    elif (chart_type == 'histogram'):
        return px.histogram(data, x=horizontal, y=vertical, color=color, **kwargs)
    else:
        raise ValueError("Tipo de gráfico inválido. Use 'bar', 'line', 'area', 'pie' ou 'histogram'.")

