import dash_bootstrap_components as dbc
from dash import html

margenes_tarjetas = {"width": "31%",'padding':'1rem','margin':'1%','background-color':'#f8f9fa'}

def card_p1_p2(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),

                    html.H5(children='Codigo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),

                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p3_p4_p5_p6(**kwargs):

    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.H3(children=f"{kwargs['tip_preg']}", className="card-title me-2",style={'font-weight':'bold'}),
                    html.Br(),
                    html.Div([
                        html.H5(children='Presupuesto Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("$ 2021 "),
                                        html.Th("$ 2022"),
                                        html.Th("$ Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['pre_2021_dis']):,}"),
                                        html.Td(f"{round(kwargs['pre_2022_dis']):,}"),
                                        html.Td(f"{round(kwargs['pre_med_dis']):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        html.Br(),
                        html.H5(children='Gasto Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("$ 2021"),
                                        html.Th("$ 2022"),
                                        html.Th("$ Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['cos_2021_dis']):,}"),
                                        html.Td(f"{round(kwargs['cos_2022_dis']):,}"),
                                        html.Td(f"{round(kwargs['cos_med_dis']):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    style={'width': '48%','float': 'left','margin-right':'2%'}
                    ),
                    
                    html.Div([
                        html.H5(children='Presupuesto Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("$ 2021"),
                                        html.Th("$ 2022"),
                                        html.Th("$ Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['pre_2021_ent']):,}"),
                                        html.Td(f"{round(kwargs['pre_2022_ent']):,}"),
                                        html.Td(f"{round(kwargs['pre_med_ent']):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        html.Br(),
                        html.H5(children='Gasto Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("$ 2021"),
                                        html.Th("$ 2022"),
                                        html.Th("$ Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['cos_2021_ent']):,}"),
                                        html.Td(f"{round(kwargs['cos_2022_ent']):,}"),
                                        html.Td(f"{round(kwargs['cos_med_ent']):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    style={'width': '48%','float': 'right','margin-left':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Relacion Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=round(kwargs['res_dist'],2), className="card-text"),
                    ],
                    style={'width': '48%','float': 'left','margin-right':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Relacion Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=round(kwargs['res_enti'],2), className="card-text"),
                    ],
                    style={'width': '48%','float': 'right','margin-left':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=kwargs['sop_car_2023'], className="card-text"),
                    ],
                    style={'width': '100%','float': 'left'}
                    ),                    
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p7_p8_p9_p10_p11_p12(**kwargs):

    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.H3(children=f"{kwargs['tip_preg']}", className="card-title me-2",style={'font-weight':'bold'}),
                    html.Br(),
                    html.Div([
                        html.H5(children='Funcionarios Total Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['can_2021_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['can_2022_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['can_med_dis'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        html.Br(),
                        html.H5(children='Funcionarios Innovación Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['fun_2021_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_2022_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_med_dis'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    style={'width': '48%','float': 'left','margin-right':'2%'}
                    ),
                    
                    html.Div([
                        html.H5(children='Funcionarios Total Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['can_2021_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['can_2022_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['can_med_ent'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        html.Br(),
                        html.H5(children='Funcionarios Innovación Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['fun_2021_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_2022_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_med_ent'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    style={'width': '48%','float': 'right','margin-left':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Relacion Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=round(kwargs['res_dist'],2), className="card-text"),
                    ],
                    style={'width': '48%','float': 'left','margin-right':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Relacion Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=round(kwargs['res_enti'],2), className="card-text"),
                    ],
                    style={'width': '48%','float': 'right','margin-left':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=kwargs['sop_car'], className="card-text"),
                    ],
                    style={'width': '100%','float': 'left'}
                    ),                    
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p13(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Costo adquisición', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['cos_car'], className="card-text"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p14_15_16_19_20(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Actividades', className="card-title me-2",style={'font-weight':'bold'}),
                    dbc.Table(
                    children=[
                        html.Thead(html.Tr([html.Th("Act 1"), html.Th("Act 2"), html.Th("Act 3"), html.Th("Act 4"), html.Th("Act 5")])),
                        html.Tbody([html.Tr([html.Td(kwargs['act_1']), html.Td(kwargs['act_2']), html.Td(kwargs['act_3']), html.Td(kwargs['act_4']), html.Td(kwargs['act_5'])])])
                        ],
                    bordered=True,
                    #dark=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    ),

                    html.H5(children='Otra actividad', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['act_otr'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Realizó alguna acción para responder al reto', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['acc_car'], className="card-text"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p17_18_21_22(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Usuarios', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['usr_car'], className="card-title"),

                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p23(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Creado con', className="card-title me-2",style={'font-weight':'bold'}),
                    dbc.Table(
                    children=[
                        html.Thead([
                            html.Tr([
                                html.Th("Crea 1"),
                                html.Th("Crea 2"),
                                html.Th("Crea 3"),
                            ])
                        ]                            
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(kwargs['us1_car']),
                                html.Td(kwargs['us2_car']),
                                html.Td(kwargs['us3_car']),
                            ])
                        ]
                        )
                        ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    ),

                    html.H5(children='Prototipado', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['pro_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Validado', className="card-title me-2",style={'font-weight':'bold'}),
                    dbc.Table(
                    children=[
                        html.Thead([
                            html.Tr([
                                html.Th("Valida 1"),
                                html.Th("Valida 2"),
                                html.Th("Valida 3"),
                            ])
                        ]                            
                        ),
                        html.Tbody([
                            html.Tr([
                                html.Td(kwargs['va1_car']),
                                html.Td(kwargs['va2_car']),
                                html.Td(kwargs['va3_car']),
                            ])
                        ]
                        )
                        ],
                    bordered=True,
                    hover=True,
                    responsive=True,
                    striped=True,
                    ),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas,
    )

def card_p24(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Impartió', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['imp_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Asistentes', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['asi_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text"),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p25_p26(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Recomendaría', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['rec_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p27(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Temática', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['tem_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Tamaño del equipo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['tam_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p28(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['nom_car'], className="card-title"),

                    html.H5(children='Implementó', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['imp_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Validó', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['val_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Metodología', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['met_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Beneficia ciudadanos', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['ben_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Ciudadanos beneficiados', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['b1_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Ahorra recursos', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['aho_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Recursos ahorrados', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['a1_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p29_p30(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [   
                    html.H3(children=f"{kwargs['tip_preg']}", className="card-title me-2",style={'font-weight':'bold'}),
                    html.Br(),
                    html.Div([
                        html.H5(children='Funcionarios Total Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['can_2021_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['can_2022_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['can_med_dis'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        html.Br(),
                        html.H5(children='Funcionarios Innovación Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['fun_2021_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_2022_dis'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_med_dis'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    style={'width': '48%','float': 'left','margin-right':'2%'}
                    ),
                    
                    html.Div([
                        html.H5(children='Funcionarios Total Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['can_2021_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['can_2022_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['can_med_ent'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                        html.Br(),
                        html.H5(children='Funcionarios Innovación Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        dbc.Table(
                            children=[
                                html.Thead([
                                    html.Tr([
                                        html.Th("2021"),
                                        html.Th("2022"),
                                        html.Th("Mediana"),
                                    ])
                                ]                            
                                ),
                                html.Tbody([
                                    html.Tr([
                                        html.Td(f"{round(kwargs['fun_2021_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_2022_ent'],2):,}"),
                                        html.Td(f"{round(kwargs['fun_med_ent'],2):,}"),
                                    ])
                                ]
                                )
                                ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    style={'width': '48%','float': 'right','margin-left':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Relacion Distrito', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=round(kwargs['res_dist'],2), className="card-text"),
                    ],
                    style={'width': '48%','float': 'left','margin-right':'2%'}
                    ),

                    html.Div([
                        html.Br(),
                        html.H5(children='Relacion Entidad', className="card-title me-2",style={'font-weight':'bold'}),
                        html.P(children=round(kwargs['res_enti'],2), className="card-text"),
                    ],
                    style={'width': '48%','float': 'right','margin-left':'2%'}
                    ),
               
                ]
            ),
        ],
        style={"width": "96%",'padding':'1rem 1rem 1rem 1rem','margin':'2% 2% 2% 2%','background-color':'#f8f9fa'},
    )

def card_p31_p32(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Codigo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),

                    html.H5(children='Nombre', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['nom_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),

                    html.H5(children='Descripción', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['des_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p33_p34_p35_p36_p37_p38(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Codigo', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style=margenes_tarjetas
    )

def card_p39(**kwargs):
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5(children='Índice', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['ind_car'], className="card-title"),
                    
                    html.H5(children='Medio', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(kwargs['cod_car'], className="card-title"),
                    
                    html.H5(children='Soporte', className="card-title me-2",style={'font-weight':'bold'}),
                    html.P(children=kwargs['sop_car'], className="card-text",style={'text-justify':'auto','text-align': 'justify'}),
                ]
            ),
        ],
        style=margenes_tarjetas
    )