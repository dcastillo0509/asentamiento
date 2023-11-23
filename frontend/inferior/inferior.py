import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
#importa las librerías necesarias

inferior=dbc.Container([#crea la variable inferior y en ella un Container
    dbc.Row([#crea una fila
        html.Hr(),#añade un espacio
        dbc.Col(html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Tuneladora_T%C3%BAnel_de_San_Pedro.JPG/500px-Tuneladora_T%C3%BAnel_de_San_Pedro.JPG'), md=6, style={'background-color': '#45ad7e'}),
                #crea una columna con titulo 3, espacio 6 y define el color de fondo
        dbc.Col(html.H5("El ensayo se llevó a cabo gracias a la instalación de un sensor que mide el asentamiento de la edificación. Este dispositivo recopila datos precisos que permiten determinar si el trabajo realizado por la tuneladora está afectando la estructura del edificio. En caso de detectar algún impacto negativo, el sensor emite una alerta para tomar las medidas necesarias y evitar daños mayores."), md=5, style={'color':'white', 'background-color':'#17242d'}),
        #crea una columna con titulo 3, espacio 3, define el color del texto y fondo
        html.Hr(),#añade un espacio
    ])
])
