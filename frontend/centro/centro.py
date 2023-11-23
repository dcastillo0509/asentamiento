import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las librerías necesarias
from dash import Dash, html,dcc, Input, Output
import plotly.graph_objs as go




#Base de datos
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://cagomezj:1234@cluster0.lg8bsx8.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.sensores.sensor_1
result = 0

# Declarar data_dist fuera de la función para evitar el UnboundLocalError
data_dist = []

centro=dbc.Container([#crea la variable inferior y en ella un Container
    dbc.Row([#crea una fila
        html.Hr(),#añade un espacio
        dbc.Col(html.H3("El asentamiento fue:"), md=6, style={'background-color':'#45ad7e'}),
        #crea una columna con titulo 3, espacio 6 y define el color de fondo
        html.Hr(),
        html.H4(id='distancia-actual', style={'text-align': 'center'}),
        dcc.Graph(id='asentamiento'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 500,  # en milisegundos, actualiza cada 1 segundo
            n_intervals=0
            ),
        html.Div(id='alerta-texto', style={'text-align': 'center', 'margin-top': '10px'})
    ])
])


def consultar(n):
    
    # Utilizar la variable global data_dist
    global data_dist , result , db
    result = db.find_one(sort=[('updated_at', -1)])
    distancia = int(result['distancia'])
    data_dist.append(distancia)
    
    # Crear el objeto de figura de Plotly
    fig = go.Figure(data=[go.Scatter(y=data_dist, mode='lines+markers')])
    
     # Agregar una línea horizontal en y=5
    fig.add_shape(
        type="line",
        x0=0,
        x1=len(data_dist),
        y0=1600,
        y1=1600,
        line=dict(color="red", width=2),
    )
    
    # Agregar un texto según la condición
    if distancia >= 1600:
        alerta_texto = html.Span("ALERTA", style={'color': 'red', 'font-size': '24px'})
    else:
        alerta_texto = html.Span("VAMOS BIEN", style={'color': 'green', 'font-size': '24px'})
    
    
    # Formatear la distancia para mostrarla en el H1
    distancia_texto = f"El asentamiento fue: {distancia} cm"
    
    return fig, distancia_texto,alerta_texto


