import dash_bootstrap_components as dbc
from dash import html

margenes_tarjetas = {"width": "31%",'padding':'1rem','margin':'1%','background-color':'#f8f9fa'}

def card_oap(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),

                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    dbc.Table(
                                        children=[
                                            html.Thead([
                                                html.Tr([
                                                    html.Th("Creatividad"),
                                                    html.Th("Potencial de Aprendizaje"),
                                                    html.Th("Eficacia"),
                                                    html.Th("Capacidad de Replica"),
                                                ])
                                            ]                            
                                            ),
                                            html.Tbody([
                                                html.Tr([
                                                    html.Td(kwargs['cre_car']),
                                                    html.Td(kwargs['pot_car']),
                                                    html.Td(kwargs['efi_car']),
                                                    html.Td(kwargs['cap_car']),
                                                ])
                                            ]
                                            )
                                            ],
                                        bordered=True,
                                        hover=True,
                                        responsive=True,
                                        striped=True,
                                        ),
                    
                    html.H5(children='Proceso', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['pro_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )
