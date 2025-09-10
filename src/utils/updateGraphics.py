def updateLayout(graph, tipo):
        if (tipo == 'line'):
            graph.update_layout(xaxis_tickformat = '%d/%m/%Y', 
                legend= dict(orientation = 'h', x=0, y=1.20, xanchor='left', yanchor='top', traceorder = 'normal', itemwidth = 70, valign = 'middle'),
                font = dict(family = 'Arial', size = 13, color = 'black'),
                paper_bgcolor = '#FEFAE0',
                margin = dict (l = 75, r = 25, t = 70),
                xaxis_title=None,
                yaxis_title=None,
                xaxis=dict(autorange=True),
                yaxis=dict(autorange=True)
                )
            
        elif (tipo == 'bar'):
            graph.update_layout(xaxis_tickformat = '%d/%m/%Y', barmode = 'stack',
                legend= dict(orientation = 'h', x=0.20, y=1.13 , xanchor='left', yanchor='top'),
                font = dict(family = 'Arial', size = 14.5, color = 'black' ),
                paper_bgcolor = '#FEFAE0',
                margin = dict (l = 75, r = 25, t = 0 , b = 0),
                yaxis = dict (range = [0, 5000]),
                xaxis_title=None,
                yaxis_title=None)
            

        elif (tipo == 'table'):
            graph.update_layout(
                margin = dict(l=0, r=40, t=40, b=0),
                paper_bgcolor = '#FEFAE0',
            )
        
        elif (tipo == 'pie'):
            graph.update_layout(
                paper_bgcolor = '#FEFAE0',
                margin=dict(l=0, r=0, t=10, b=10)
            )
            graph.update_traces(
                pull=[0, 0, 0],    
                marker=dict(line=dict(width=0)), 
                rotation=0,
                sort=False
            )
        elif (tipo == 'histogram'):
            graph.update_layout(
                xaxis_title=None,
                yaxis_title=None,
                font = dict(family = 'Arial', size = 14.5, color = 'black' ),
                paper_bgcolor = '#FEFAE0',
                margin = dict (l = 75, r = 25, t = 0 , b = 0),
                yaxis = dict (range = [0, 20000]),
            )
        elif(tipo == 'area'):
            graph.update_layout(
                xaxis_tickformat = '%d/%m/%Y', 
                legend= dict(orientation = 'h', x=0, y=1.20, xanchor='left', yanchor='top', traceorder = 'normal', itemwidth = 70, valign = 'middle'),
                font = dict(family = 'Arial', size = 14.5, color = 'black' ),
                paper_bgcolor = '#FEFAE0',
                margin = dict (l = 75, r = 25, t = 0 , b = 50),
                yaxis = dict (range = [0, 10000]),
                xaxis_title=None,
                yaxis_title=None,
                showlegend = False
            )
        return graph