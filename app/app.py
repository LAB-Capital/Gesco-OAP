from assets.commons import LOGO_IIP,LOGO_LAB

import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, dcc, callback, page_container

app = Dash( 
    __name__,
    external_stylesheets=[dbc.themes.UNITED, dbc.icons.FONT_AWESOME],
    use_pages=True
)

server=app.server

navbar = dbc.Container(
    dbc.Row([
        dbc.Col(
            html.A(html.H3('Lecciones Aprendidas & Buenas Prácticas VD',style={'color':'white','margin':'0','font-weight':'bold'}), className="navbar-brand", href="/"),
        # width=4 #Solo se deja si varias columnas 
        ),
    ],
    justify="between",
    ),
className='content',
#style={'background-color':'#e95420'},
fluid=True,
)

sidebar = html.Div(
    [
        html.A([
                    html.Img(height="50px",src=LOGO_LAB,className='logolab',style={'max-width':'14.5em','object-fit': 'contain'}),
                    html.Img(height="50px",src=LOGO_IIP,className='logoiip'),
                    ],
                    href="/",
                    style={"textDecoration": "none"},
                    
                ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-magnifying-glass"),
                        html.Span("Instrumento"),
                    ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-magnifying-glass"),
                        html.Span("Explorador"),
                    ],
                    href="/explorador",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-light", # Tal vez cambiar a dark
)

###############################################################################################################################################################################################################
# LAYOUT
###############################################################################################################################################################################################################

app.layout = html.Div(
[
    navbar,
    sidebar,

    dbc.Container(
        [
            html.Div(
                [
                    page_container
                ],
                className="content",
            ),
        ],
        fluid=False,
    ),
],
style={'margin-left':'5em'}
)

###############################################################################################################################################################################################################
# Debug y puertos
###############################################################################################################################################################################################################    

if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=1234)