import dash_bootstrap_components as dbc
from dash import html

def criterio_1():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_2():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4,rowSpan=5),
                        html.Td(1.2),
                        html.Td('Asignado a todos automáticamente',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Comparación con 2021',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1.6,rowSpan=3),
                        html.Td(1.6),
                        html.Td('''Criterio 1: Relevancia estratégica'''),
                    ]),
                    html.Tr([
                        html.Td(1.6),
                        html.Td('''Criterio 2: Impacto potencial'''),
                    ]),
                    html.Tr([
                        html.Td(1.6),
                        html.Td('''Criterio 3: Nivel de novedad'''),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),

        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Tipo",colSpan=1),
                        html.Th("Nota",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.6,rowSpan=9),
                        html.Td(1.6),
                        html.Td('Resolución'),
                    ]),
                    html.Tr([
                        html.Td(1.6),
                        html.Td('Acuerdo concejo'),
                    ]),
                    html.Tr([
                        html.Td('1.3 - 1.6'),
                        html.Td('Proyecto de inversión'),
                    ]),
                    html.Tr([
                        html.Td('1 - 1.4'),
                        html.Td('Plan estratégico'),
                    ]),
                    html.Tr([
                        html.Td('1 - 1.4'),
                        html.Td('Plan institucional'),
                    ]),
                    html.Tr([
                        html.Td(.8),
                        html.Td('Enfoque'),
                    ]),
                    html.Tr([
                        html.Td(.8),
                        html.Td('Linea'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Circular'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Oficios'),
                    ]),

                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_3():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio
        
def criterio_4():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4,rowSpan=9),
                    ]),
                    html.Tr([
                        html.Td(1.5,rowSpan=3),
                        html.Td('Comparativa contra mediana del Distrito',rowSpan=3),
                        html.Td(1.5),
                        html.Td('Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(.75),
                        html.Td('Si es menor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),
                    html.Tr([
                        html.Td(2.5,rowSpan=5),
                        html.Td('Categoría en la que entra',rowSpan=5),
                        html.Td(2.5),
                        html.Td('3% en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.8),
                        html.Td('1-3%'),
                    ]),
                    html.Tr([
                        html.Td(1.4),
                        html.Td('0.5-1%'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('0.2-0.5%'),
                    ]),
                    html.Tr([
                        html.Td(0.8),
                        html.Td('0-0.2%'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_5():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_6():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4,rowSpan=9),
                    ]),
                    html.Tr([
                        html.Td(1.35,rowSpan=3),
                        html.Td('Comparativa contra mediana del Distrito',rowSpan=3),
                        html.Td(1.35),
                        html.Td('Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('Si es menor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),
                    html.Tr([
                        html.Td(2.35,rowSpan=5),
                        html.Td('Categoría en la que entra',rowSpan=5),
                        html.Td(2.35),
                        html.Td('3% en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.7),
                        html.Td('1-3%'),
                    ]),
                    html.Tr([
                        html.Td(1.3),
                        html.Td('0.5-1%'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('0.2-0.5%'),
                    ]),
                    html.Tr([
                        html.Td(0.7),
                        html.Td('0-0.2%'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_7():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_8():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4,rowSpan=10),
                        html.Td(1.5,rowSpan=4),
                        html.Td('Mediana % Distrito',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(0.75),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),



                    html.Tr([
                        html.Td(2.5,rowSpan=6),
                        html.Td('Relación % 2.5',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(2.5),
                        html.Td('8% en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('4.5 - 8%'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('2.5 - 4.5%'),
                    ]),
                    html.Tr([
                        html.Td(0.9),
                        html.Td('1.5 - 2.5%'),
                    ]),
                    html.Tr([
                        html.Td(0.6),
                        html.Td('0 - 1.5%'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_9():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_10():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_11():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4.7,rowSpan=10),
                        html.Td(2,rowSpan=4),
                        html.Td('Mediana % Distrito',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(2),
                        html.Td('Si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Si es menor'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),



                    html.Tr([
                        html.Td(2.7,rowSpan=6),
                        html.Td('Relación % 2.5',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(2.7),
                        html.Td('8% en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.9),
                        html.Td('4.5 - 8%'),
                    ]),
                    html.Tr([
                        html.Td(1.4),
                        html.Td('2.5 - 4.5%'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('1.5 - 2.5%'),
                    ]),
                    html.Tr([
                        html.Td(0.8),
                        html.Td('0 - 1.5%'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_12():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_13():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(4.6,rowSpan=8),
                        html.Td(1.38,rowSpan=3),
                        html.Td('Comparación facilitar innovación 2021: 30%',rowSpan=3),
                        html.Td(1.38),
                        html.Td('si es mayor'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('similar'),
                    ]),
                    html.Tr([
                        html.Td(0.7),
                        html.Td('si es menor'),
                    ]),

                    html.Tr([
                        html.Td(3.22,rowSpan=4),
                        html.Td('Valoración de criterios: 70%',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Criterio 1: Grado de novedad'),
                    ]),
                    html.Tr([
                        html.Td(1.22),
                        html.Td('Criterio 2: Aporte a la innovación'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Criterio 3: Categoría a la que pertenece'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),

        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Categoría",colSpan=1),
                        html.Th("Nota",colSpan=1),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=7),
                        html.Td(0.5),
                        html.Td('Gestión documental'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Asistencia virtual y chatbot'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Seguridad y protección'),
                    ]),
                    html.Tr([
                        html.Td(.75),
                        html.Td('Geolocalización y cartografía'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Sistemas de información misional'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Comunicación y colaboración'),
                    ]),
                    html.Tr([
                        html.Td(.75),
                        html.Td('Analisis y visualización de datos'),
                    ]),

                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_14():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.8,rowSpan=9),
                        html.Td(1.4,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.5),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Socializó info'),
                    ]),

                    html.Tr([
                        html.Td(1.3,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.3),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.75),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.25),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_15():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=9),
                        html.Td(.5,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.2),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.2),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Socializó info'),
                    ]),

                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_16():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.8,rowSpan=9),
                        html.Td(1.4,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.5),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Socializó info'),
                    ]),

                    html.Tr([
                        html.Td(1.3,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.3),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.75),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.25),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_17():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.2,rowSpan=9),
                        html.Td(.6,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.3),
                        html.Td('Sólo funcionarios'),
                    ]),
                    html.Tr([
                        html.Td(0.3),
                        html.Td('Sólo Ciudadanos'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('Funcionarios y ciudadanos'),
                    ]),

                    html.Tr([
                        html.Td(.6,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_18():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.2,rowSpan=9),
                        html.Td(.6,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.3),
                        html.Td('Sólo funcionarios'),
                    ]),
                    html.Tr([
                        html.Td(0.3),
                        html.Td('Sólo Ciudadanos'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('Funcionarios y ciudadanos'),
                    ]),

                    html.Tr([
                        html.Td(.6,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_19():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(3,rowSpan=9),
                        html.Td(1.5,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.5),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Socializó info'),
                    ]),

                    html.Tr([
                        html.Td(1.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.9),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_20():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(3,rowSpan=9),
                        html.Td(1.5,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.5),
                        html.Td('Elaboró documento'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Planificó acciones'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Socializó info'),
                    ]),

                    html.Tr([
                        html.Td(1.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.9),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_21():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=9),
                        html.Td(.5,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.3),
                        html.Td('Sólo funcionarios'),
                    ]),
                    html.Tr([
                        html.Td(0.3),
                        html.Td('Sólo Ciudadanos'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Funcionarios y ciudadanos'),
                    ]),

                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_22():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima"),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=9),
                        html.Td(.5,rowSpan=3),
                        html.Td('Criterios',rowSpan=3),
                        
                        html.Td(0.3),
                        html.Td('Sólo funcionarios'),
                    ]),
                    html.Tr([
                        html.Td(0.3),
                        html.Td('Sólo Ciudadanos'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Funcionarios y ciudadanos'),
                    ]),

                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 retos'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 retos'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 retos'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 reto'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_23():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(7,rowSpan=8),
                        html.Td(3.5),
                        html.Td('Criterio del analista'),
                        html.Td('N/A',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1.5,rowSpan=4),
                        html.Td('De donde surgió la innovación',rowSpan=4),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Funcionarios'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Cuidadanía'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Nivel Directivo'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('¿Tiene prototipo?'),
                        html.Td('N/A',colSpan=2),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('¿Fue validado?'),
                        html.Td('N/A',colSpan=2),
                    ]),

                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_24():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(6,rowSpan=4),
                        html.Td(1.5),
                        html.Td('Eventos propios'),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('Eventos de otras entidades'),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('Formación propia'),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('Formación de otras entidades'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_25():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.8,rowSpan=9),
                        html.Td(1.4,rowSpan=3),
                        html.Td('Calidad',rowSpan=3),
                        html.Td(1.4),
                        html.Td('Esfuerzo'),
                    ]),
                    html.Tr([
                        html.Td(1.4),
                        html.Td('Alcance'),
                    ]),
                    html.Tr([
                        html.Td(1.4),
                        html.Td('Normativización'),
                    ]),
                    html.Tr([
                        html.Td(1.4,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.4),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('4 ideas'),
                    ]),
                    html.Tr([
                        html.Td(.8),
                        html.Td('3 ideas'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('2 ideas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('1 ideas'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),

        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Criterio",colSpan=5),

                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('alto'),
                        html.Td('medio alto'),
                        html.Td('medio'),
                        html.Td('medio bajo'),
                        html.Td('bajo'),
                    ]),
                    html.Tr([
                        html.Td(1.4),
                        html.Td(1.1),
                        html.Td(.8),
                        html.Td(.5),
                        html.Td(.2),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_26():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.1,rowSpan=9),
                        html.Td(.5,rowSpan=3),
                        html.Td('Calidad',rowSpan=3),
                        html.Td(.5),
                        html.Td('Esfuerzo'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alcance'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Normativización'),
                    ]),
                    html.Tr([
                        html.Td(.6,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('5 en adelante'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 ideas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 ideas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 ideas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 ideas'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),

        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Criterio",colSpan=5),

                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('alto'),
                        html.Td('medio alto'),
                        html.Td('medio'),
                        html.Td('medio bajo'),
                        html.Td('bajo'),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td(.4),
                        html.Td(.3),
                        html.Td(.2),
                        html.Td(.1),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_27():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1.1,rowSpan=5),
                        html.Td(1.1),
                        html.Td('Lab, semillero y observatorio'),
                    ]),
                    html.Tr([
                        html.Td(0.5),
                        html.Td('Mesas técnicas, comités, equipos u otras unidades que le apuntan a la innovación'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Otros no relacionados con innovación'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_28():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ]),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(20.5,rowSpan=15),
                        html.Td(6),
                        html.Td('Total de iniciativas'),
                        html.Td(6),
                        html.Td('Ver tabla abajo'),
                    ]),
                    html.Tr([
                        html.Td(3.5),
                        html.Td('Analista'),
                        html.Td(3.5),
                        html.Td('N/A'),
                    ]),
                    html.Tr([
                        html.Td(2,rowSpan=3),
                        html.Td('Comparación 2021',rowSpan=3),
                        html.Td(2),
                        html.Td('Mas'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Mismo nivel de innovacion'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Menos'),
                    ]),
                    html.Tr([
                        html.Td(5,rowSpan=5),
                        html.Td('Metodología usada',rowSpan=5),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Validó con usuarios'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Utilizó una metodología'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td('Befenició a los cuiudadanos'),
                    ]),
                    html.Tr([
                        html.Td(2),
                        html.Td('Ahorró recursos'),
                    ]),
                    html.Tr([
                        html.Td(4,rowSpan=5),
                        html.Td('Impacto potencial',rowSpan=5),
                        html.Td(4),
                        html.Td('Alto'),
                    ]),
                    html.Tr([
                        html.Td(3.2),
                        html.Td('Medio alto'),
                    ]),
                    html.Tr([
                        html.Td(2.4),
                        html.Td('Medio'),
                    ]),
                    html.Tr([
                        html.Td(1.6),
                        html.Td('Medio bajo'),
                    ]),
                    html.Tr([
                        html.Td(.8),
                        html.Td('Bajo'),
                    ]),

                ]),
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
        ),

        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Total de iniciativas",colSpan=8),
                    ]),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td('1 a 2'),
                        html.Td('3 a 4'),
                        html.Td('5 a 7'),
                        html.Td('8 a 10'),
                        html.Td('11 a 13'),
                        html.Td('14 a 16'),
                        html.Td('17 a 19'),
                        html.Td('20 o mas'),
                    ]),
                    html.Tr([
                        html.Td(1),
                        html.Td(2),
                        html.Td(3),
                        html.Td(4),
                        html.Td(4.5),
                        html.Td(5),
                        html.Td(5.5),
                        html.Td(6),
                    ]),
                ]),
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
        ),
    ],
    style={'width': '100%'})
    return salida_criterio

def criterio_29():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.2,rowSpan=9),
                    ]),
                    html.Tr([
                        html.Td(2.2,rowSpan=3),
                        html.Td('Comparativa contra mediana del Distrito',rowSpan=3),
                        html.Td(2.2),
                        html.Td('Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('Si es menor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_30():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=2),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(2.3,rowSpan=9),
                    ]),
                    html.Tr([
                        html.Td(2.3,rowSpan=3),
                        html.Td('Comparativa contra mediana del Distrito',rowSpan=3),
                        html.Td(2.3),
                        html.Td('Si es mayor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(1.1),
                        html.Td('Si es menor a promedio distrital'),
                    ]),
                    html.Tr([
                        html.Td(0),
                        html.Td('Si no tiene valor'),
                    ]),
                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_31():
    salida_criterio=html.Div(children=[
                dbc.Table(
                    children=[
                        html.Thead(children=[

                            html.Tr([
                                html.Th("Nota máxima",colSpan=1),
                                html.Th("Nota por criterio",colSpan=1),
                                html.Th("Criterios",colSpan=1),
                            ],
                            ),
                        ]),

                        html.Tbody([
                            html.Tr([
                                html.Td(0,rowSpan=3),
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('N/A'),
                            ]),
                            html.Tr([
                                html.Td(0),
                                html.Td('''N/A'''),
                            ]),
                        ])
                    ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                ),
            ],style={'width': '100%'})
    return salida_criterio

def criterio_32():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(3,rowSpan=12),
                        html.Td(1.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.9),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(1.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(1.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.9),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_33():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=12),
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_34():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=12),
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_35():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=12),
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_36():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=12),
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_37():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=12),
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_38():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(1,rowSpan=12),
                        html.Td(.5,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.5,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(.5),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(.3),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.1),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio

def criterio_39():
    salida_criterio=html.Div(children=[
        dbc.Table(
            children=[
                html.Thead(children=[

                    html.Tr([
                        html.Th("Nota máxima",colSpan=1),
                        html.Th("Nota por criterio",colSpan=1),
                        html.Th("Criterios",colSpan=2),
                    ],
                    ),
                ]),

                html.Tbody([
                    html.Tr([
                        html.Td(6,rowSpan=12),
                        html.Td(3,rowSpan=6),
                        html.Td('Cantidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(3),
                        html.Td('5 o mas Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(2.4),
                        html.Td('4 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(1.8),
                        html.Td('3 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('2 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('1 Iniciativas'),
                    ]),
                    html.Tr([
                        html.Td(3,rowSpan=6),
                        html.Td('Calidad',rowSpan=6),
                    ]),
                    html.Tr([
                        html.Td(3),
                        html.Td('Alta'),
                    ]),
                    html.Tr([
                        html.Td(2.4),
                        html.Td('Media alta'),
                    ]),
                    html.Tr([
                        html.Td(1.8),
                        html.Td('Media'),
                    ]),
                    html.Tr([
                        html.Td(1.2),
                        html.Td('Media baja'),
                    ]),
                    html.Tr([
                        html.Td(.6),
                        html.Td('Baja'),
                    ]),


                ])
            ],
            bordered=True,
            hover=True,
            responsive=True,
            striped=True,
            ),
        ],
    style={'width': '100%'})
    return salida_criterio