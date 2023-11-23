import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de das como dbc
from dash.dependencies import Input, Output #de dash.dependencies se importa input y output
import math #se importa math
import pandas as pd
import plotly.tools as tls
import plotly.graph_objs as go
#importa las librerías necesarias

#Se importa frontend
from frontend.main import layout
from frontend.centro.centro import consultar

app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#crea la variable app y agrega __name__ y los estilos con bootstrap
server=app.server
app.layout = layout #se asigna el layout en la variable layout de app

@app.callback(
    [Output('asentamiento', 'figure'),
     Output('distancia-actual', 'children'),
     Output('alerta-texto', 'children')],
    [Input('interval-component', 'n_intervals')]
)

def consultar_centro(n):
    return centro.consultar(n)

if __name__ == '__main__': #si __name__ y __main__ son iguales
    app.run_server(debug=True) #Ejecuta la app
