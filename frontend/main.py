import dash #importa dash
import dash_bootstrap_components as dbc #importa los componentes bootstrap de dash como dbc
from dash import html #De dash importa html

#importamos el frontend

from .navegador.navegador import navegador #importa container de navegador
from .centro.centro import centro #importa container de centro
from .inferior.inferior import inferior #importa container de inferior


layout=dbc.Container([ #en la variable layout, crea container de toda la página web
    dbc.Row([ #crea una fila
        dbc.Col(navegador, md=12, style={'background-color': 'gray'}), 
        #crea columna con navegador espacio de 12 y color de fondo gris
        dbc.Col(centro, md=12, style={'background-color': 'gray'}),
        #crea columna con inferior espacio de 12 y color de fondo gris
        dbc.Col(inferior, md=12, style={'background-color': 'gray'}),
        #crea columna con inferior espacio de 12 y color de fondo gris
    ])
])