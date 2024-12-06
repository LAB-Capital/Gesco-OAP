import dash_bootstrap_components as dbc
from dash import html

# margenes_tarjetas = {"width": "31%",'padding':'1rem','margin':'1%','background-color':'#f8f9fa'}
#margenes_tarjetas = {'padding':'1rem', 'background-color':'#f8f9fa'}
margenes_tarjetas = {
    "padding": '1rem', 
    'margin': '1%', 
    'background-color': '#f8f9fa',
    "display": "flex",          # Enable flexbox to stretch content
    "flexDirection": "column",  # Arrange content vertically within the card
    "height": "100%"            # Allow the card to expand to fill the container's height
}

def card_oap(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5("Nombre", className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"), # ,style={'font-weight':'bold'}
                    html.H5("Puntaje", className="card-title me-2",style={'font-weight':'bold'}),
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                dbc.Progress(label="Creatividad", value=kwargs['cre_car'], max=5, color="success"),
                                html.Br()
                            ]
                            )
                        ]
                        ),
                        dbc.Row([
                            dbc.Col([
                                dbc.Progress(label="Potencial de Aprendizaje", value=kwargs['pot_car'], max=5, color="warning"),
                                html.Br()
                            ]
                            )
                        ]
                        ),
                        dbc.Row([
                            dbc.Col([
                                dbc.Progress(label="Eficacia", value=kwargs['efi_car'], max=5, color="danger"),
                                html.Br()
                            ]
                            )
                        ]
                        ),
                        dbc.Row([
                            dbc.Col([
                                dbc.Progress(label="Capacidad de Replica", value=kwargs['cap_car'], max=5, color="info"),
                                html.Br()
                            ]
                            )
                        ]
                        ),
                    ],
                    ),
                    
                    html.H5(children='Proceso', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['pro_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )
