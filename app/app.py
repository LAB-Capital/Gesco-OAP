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
        ),
    ],
    justify="between",
    ),
className='content',
#style={'background-color':'#e95420'},
fluid=False,
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
                        html.I(className="fa-solid fas fa-book-open",style={'margin-right':'1rem'}),
                        html.Span("Introducción"),
                    ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fas fa-compass",style={'margin-right':'1rem'}),
                        html.Span("Consulta"),
                    ],
                    href="/consulta",
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