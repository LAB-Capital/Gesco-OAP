
import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc, register_page, callback
import plotly.graph_objects as go

from assets.commons import normalizador_notas
from assets.commons import preguntas_df
from assets.commons import entidades,misvis
from assets.commons import resultados_2019_df,respuestas_2019_df
from assets.commons import resultados_2021_df,respuestas_2021_df
from assets.commons import resultados_2023_df,respuestas_2023_df

register_page(__name__, path='/dashboards')

###############################################################################################################################################################################################################
# LAYOUT
###############################################################################################################################################################################################################

layout = html.Div([

    dbc.Row([

        dbc.Col([
            html.H1(children=[],id='entidad',style={'font-weight':'bold'}),
            ],
            width=9,
        ),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                            dbc.Col([
                                html.P('Posición', style={'padding': '0em', 'margin': '0em 0em 0.5em','color':'#00000050'}),
                                html.H3(id='posicion')
                            ],
                            style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                            dbc.Col([
                                html.P('Puntaje', style={'padding': '0em', 'margin': '0em 0em 0.5em','color':'#00000050'}),
                                html.H3(id='puntaje')
                            ],
                            style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                        ]),
                ],
                
                ),
                style={'height': '100%'}
            )
            ],
            width=3,
        ),
    ],
    justify="between",
    ),
    html.Br(),

    dbc.Row([
        dbc.Col(html.Div([
                html.H3('Mision'),
                html.P(id='dash_mision',children=[])
            ],                        
            style={'text-justify':'auto','text-align': 'justify'}
            ),
        ),
        dbc.Col(html.Div([
                html.H3('Vision'),
                html.P(id='dash_vision',children=[])
            ],                        
            style={'text-justify':'auto','text-align': 'justify'}
            ),
        )
    ]),

    dbc.Row([
        #Fila resultados por componente
        html.H3('Resumen', style={'font-weight': 'bold'}),

        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H6('Componente 1',style={'color':'#00000050'}),
                    html.H4('Capacidad Institucional', style={'font-weight': 'bold'}),
                    html.P(
                        'Capacidad, recursos e insumos que tiene la entidad para desarrollar acciones relacionadas con la innovación',
                        style={'text-justify': 'auto', 'text-align': 'justify'}
                    ),
                    # Wrap the dbc.Row in a Div with sticky positioning
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.P('Peso', style={'padding': '0rem', 'margin': '0rem','color':'#00000050'}),
                                html.H5('25%', style={'padding': '0rem', 'margin': '0rem', 'font-weight': 'bold'})
                            ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                            dbc.Col(
                                html.H3(id='entidad_c1')
                            )
                        ])
                    ], style={"position": "sticky"})
                ],
                style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}  # Ensures card content stretches
                ),
                style={'height': '100%'}
            )
        ]),

        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H6('Componente 2',style={'color':'#00000050'}),
                    html.H4('Prácticas y Procesos', style={'font-weight': 'bold'}),
                    html.P(
                        'Identificación de procesos para el reconocimiento de retos públicos, generación de ideas, diseño de innovaciones, generación de capacidades de innovación y promoción de una cultura para la innovación',
                        style={'text-justify': 'auto', 'text-align': 'justify'}
                    ),
                    # Wrap the dbc.Row in a Div with sticky positioning
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.P('Peso', style={'padding': '0rem', 'margin': '0rem','color':'#00000050'}),
                                html.H5('35%', style={'padding': '0rem', 'margin': '0rem', 'font-weight': 'bold'})
                            ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                            dbc.Col(
                                html.H3(id='entidad_c2')
                            )
                        ])
                    ], style={"position": "sticky"})
                ],
                style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}  # Ensures card content stretches
                ),
                style={'height': '100%'}
            )
        ]),

        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H6('Componente 3',style={'color':'#00000050'}),
                    html.H4('Resultados', style={'font-weight': 'bold'}),
                    html.P(
                        'Medición de la materialización de acciones de innovación pública en la entidad. Generación de capacidades. Ahorro de recursos e impacto en ciudadanos',
                        style={'text-justify': 'auto', 'text-align': 'justify'}
                    ),
                    # Wrap the dbc.Row in a Div with sticky positioning
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.P('Peso', style={'padding': '0rem', 'margin': '0rem','color':'#00000050'}),
                                html.H5('25%', style={'padding': '0rem', 'margin': '0rem', 'font-weight': 'bold'})
                            ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                            dbc.Col(
                                html.H3(id='entidad_c3')
                            )
                        ])
                    ], style={"position": "sticky"})
                ],
                style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}  # Ensures card content stretches
                ),
                style={'height': '100%'}
            )
        ]),

        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H6('Componente 4',style={'color':'#00000050'}),
                    html.H4('Gestión del Conocimiento', style={'font-weight': 'bold'}),
                    html.P(
                        'Evidenciar compromiso por gestionar (dentro y fuera de la entidad) el conocimiento adquirido en innovación y temas propios de la entidad',
                        style={'text-justify': 'auto', 'text-align': 'justify'}
                    ),
                    # Wrap the dbc.Row in a Div with sticky positioning
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.P('Peso', style={'padding': '0rem', 'margin': '0rem','color':'#00000050'}),
                                html.H5('15%', style={'padding': '0rem', 'margin': '0rem', 'font-weight': 'bold'})
                            ], style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}),
                            dbc.Col(
                                html.H3(id='entidad_c4')
                            )
                        ])
                    ], style={"position": "sticky"})
                ],
                style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}  # Ensures card content stretches
                ),
                style={'height': '100%'}
            )
        ]),
    ],
    justify="between",
    ),
    
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H3('Componente 1',style={'font-weight':'bold'}),
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Variable 1',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Planeación'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 2',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Recursos Presupuestales'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 3',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Recursos Humanos'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 4',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Recursos digitales'),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v1'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v2'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v3'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v4'),
                        ]),
                    ])
                ],
                ),
            )
        ]),
    ]),

    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H3('Componente 2',style={'font-weight':'bold'}),
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Variable 5',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Proceso de identificación y uso de retos o áreas de oportunidad'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 6',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Generación de ideas'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 7',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Diseño de Innovaciones'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 8',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Generación de capacidades'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 9',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Cultura y liderazgo para la innovación pública'),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v5'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v6'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v7'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v8'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v9'),
                        ]),
                    ])
                ],
                ),
            )
        ]),
    ]),

    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H3('Componente 3',style={'font-weight':'bold'}),
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Variable 10',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Innovaciones Implementadas'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 11',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Generación de capacidades en innovación para funcionarios y/o contratistas'),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v10'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v11'),
                        ]),
                    ]),
                ],
                ),
            )
        ]),
    ]),
    
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H3('Componente 4',style={'font-weight':'bold'}),
            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Variable 12',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Gestión del conocimiento en la Capacidad Institucional'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 13',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Gestión del conocimiento en los Procesos y Procedimientos'),
                        ]),
                        dbc.Col([
                            html.H6('Variable 14',style={'color':'#00000050','font-weight':'bold'}),
                            html.P('Gestión del conocimiento en los Resultados'),
                        ]),
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v12'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v13'),
                        ]),
                        dbc.Col([
                            html.Br(),
                            dcc.Graph(id='entidad_v14'),
                        ]),
                    ]),
                    
                ],
                ),
            )
        ]),
    ]),

],
)

###############################################################################################################################################################################################################
# callback nombre
###############################################################################################################################################################################################################

@callback(
    Output('entidad', 'children'),
    Input('data_entidad_human', 'data'),
)
def actualizar_entidad(entidad):
    return entidad

###############################################################################################################################################################################################################
# callback misión y visión
###############################################################################################################################################################################################################

@callback(
    Output('dash_mision', 'children'),
    Output('dash_vision', 'children'),
    Input('data_mis', 'data'),
    Input('data_vis', 'data'),
)
def mision_vision_entidad_f(mision,vision):
    return mision,vision

###############################################################################################################################################################################################################
# generador de graficos gauge
###############################################################################################################################################################################################################

def gauge_gen(actual, anterior):
    fig = go.Figure(
        go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = actual,
            mode = "gauge+number+delta",
            delta = {'reference': anterior},
            gauge = {'axis': {'range': [None, 100]},
                        'steps' : [
                            {'range': [0, 33], 'color': "red"},
                            {'range': [33, 66], 'color': "yellow"},
                            {'range': [66, 100], 'color': "green"},
                        ],
                        'bar': {'color': "darkblue"},
                    },

        )
    )
    fig.update_layout(
        margin=dict(l=30, r=30, t=10, b=10),
        height=200,
    )

    return fig

###############################################################################################################################################################################################################
# callback generar graficos
###############################################################################################################################################################################################################

@callback(
    Output('entidad_v1', 'figure'),
    Output('entidad_v2', 'figure'),
    Output('entidad_v3', 'figure'),
    Output('entidad_v4', 'figure'),
    Output('entidad_v5', 'figure'),
    Output('entidad_v6', 'figure'),
    Output('entidad_v7', 'figure'),
    Output('entidad_v8', 'figure'),
    Output('entidad_v9', 'figure'),
    Output('entidad_v10', 'figure'),
    Output('entidad_v11', 'figure'),
    Output('entidad_v12', 'figure'),
    Output('entidad_v13', 'figure'),
    Output('entidad_v14', 'figure'),
    Input('data_entidad_v1', 'data'),
    Input('data_entidad_v2', 'data'),
    Input('data_entidad_v3', 'data'),
    Input('data_entidad_v4', 'data'),
    Input('data_entidad_v5', 'data'),
    Input('data_entidad_v6', 'data'),
    Input('data_entidad_v7', 'data'),
    Input('data_entidad_v8', 'data'),
    Input('data_entidad_v9', 'data'),
    Input('data_entidad_v10', 'data'),
    Input('data_entidad_v11', 'data'),
    Input('data_entidad_v12', 'data'),
    Input('data_entidad_v13', 'data'),
    Input('data_entidad_v14', 'data'),
)
def actualizar_variables(resv1,resv2,resv3,resv4,resv5,resv6,resv7,resv8,resv9,resv10,resv11,resv12,resv13,resv14):
    
    v1      = gauge_gen(normalizador_notas(100,resv1[2],  4   ),1)
    v2      = gauge_gen(normalizador_notas(100,resv2[2],  7.7 ),1)
    v3      = gauge_gen(normalizador_notas(100,resv3[2],  8.7 ),1)
    v4      = gauge_gen(normalizador_notas(100,resv4[2],  4.6 ),1)
    v5      = gauge_gen(normalizador_notas(100,resv5[2],  9   ),1)
    v6      = gauge_gen(normalizador_notas(100,resv6[2],  8   ),1)
    v7      = gauge_gen(normalizador_notas(100,resv7[2],  7   ),1)
    v8      = gauge_gen(normalizador_notas(100,resv8[2],  6   ),1)
    v9      = gauge_gen(normalizador_notas(100,resv9[2],  5   ),1)
    v10     = gauge_gen(normalizador_notas(100,resv10[2], 20.5),1)
    v11     = gauge_gen(normalizador_notas(100,resv11[2], 4.5 ),1)
    v12     = gauge_gen(normalizador_notas(100,resv12[2], 3   ),1)
    v13     = gauge_gen(normalizador_notas(100,resv13[2], 6   ),1)
    v14     = gauge_gen(normalizador_notas(100,resv14[2], 6   ),1)

    return v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14

###############################################################################################################################################################################################################
# Mapeador colores
###############################################################################################################################################################################################################

def get_style(value, thresholds=(10, 50), colors=('green', 'yellow', 'red')):
    # Determine background color based on value and thresholds
    if thresholds[0] < value <= thresholds[1]:
        background_color = colors[1]
    elif value <= thresholds[0] and value > 0:
        background_color = colors[0]
    else:
        background_color = colors[2]
    
    # Return style with dynamic background color
    return {
        'background-color': background_color,
        'text-align': 'center',
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'height': '100%',
        'font-weight': 'bold',
        'padding': '0px',
        'margin': '0px',
        'border-radius': '10px'
    }

###############################################################################################################################################################################################################
# callback cambiador de colores background
###############################################################################################################################################################################################################

@callback(
    Output('posicion', 'style'),
    Output('puntaje', 'style'),
    Output('entidad_c1', 'style'),
    Output('entidad_c2', 'style'),
    Output('entidad_c3', 'style'),
    Output('entidad_c4', 'style'),
    Output('posicion', 'children'),
    Output('puntaje', 'children'),
    Output('entidad_c1', 'children'),
    Output('entidad_c2', 'children'),
    Output('entidad_c3', 'children'),
    Output('entidad_c4', 'children'),
    Input('data_pos', 'data'),
    Input('data_res', 'data'),
    Input('data_res_c1', 'data'),
    Input('data_res_c2', 'data'),
    Input('data_res_c3', 'data'),
    Input('data_res_c4', 'data'),
)
def cambiar_background(pos, res, c1, c2, c3, c4):
    pos_style = get_style(pos[2], (10, 50), ('green', 'yellow', 'red'))
    res_style = get_style(res[2], (30, 65), ('red', 'yellow', 'green'))
    c1_style = get_style(c1[2], (30, 65), ('red', 'yellow', 'green'))
    c2_style = get_style(c2[2], (30, 65), ('red', 'yellow', 'green'))
    c3_style = get_style(c3[2], (30, 65), ('red', 'yellow', 'green'))
    c4_style = get_style(c4[2], (30, 65), ('red', 'yellow', 'green'))

    return pos_style, res_style, c1_style, c2_style, c3_style, c4_style,pos[2],res[2],c1[2],c2[2],c3[2],c4[2]