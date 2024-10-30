import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc, register_page, callback

from assets.cards import card_oap
from assets.commons import lecc,buen
register_page(__name__, path='/explorador')

lecciones_aprendidas=lecc
buenas_practicas=buen

par_spacer='1rem'
progress_thickness='.8rem'

selector_categoria = dcc.Dropdown(
    id="selector_categoria",
    options=[{'label': x, 'value': x} for x in ['Eficiencia Administrativa','Transparencia y rendición de cuentas','Participación Ciudadana']],
    placeholder='Seleccione la categoría a analizar',
    value='Eficiencia Administrativa'
)

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = html.Div([

    dbc.Row([        
        dcc.Store(id='data_categoria',data=[],storage_type='memory'),

        dbc.Col([
            html.H1(children=['Titulo de sección'],style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=9,
        ),

        dbc.Col([
            selector_categoria
            ],
            width=3,
        )
        ],
        justify="between",
        
    ),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Buenas Prácticas'),
                        html.Div(id='buenas',children='',),
                    ]),
                ]),
            ]),
        ],
        ),
    ],
    justify="between",
    ),
    
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            html.H3('Lecciones Aprendidas'),
                            html.Div(id='lecciones',children='',),
                        ]),
                    ]),
                ]),
            ],
            ),
        ],
        justify="between",
        ),
],
)

###############################################################################################################################################################################################################
# callback guardar categoria seleccionada
###############################################################################################################################################################################################################

@callback(
    Output('data_categoria', 'data'),
    Input('selector_categoria', 'value')
)
def seleccion_categoria(value):
    if value is not None:
        salida=value
    else:
        salida = None
    return salida

###############################################################################################################################################################################################################
# callback ver respuestas
###############################################################################################################################################################################################################

@callback(
    Output('buenas', 'children'),
    Input('data_categoria', 'data'),
)
def visualizacion_buenas_practicas(categoria):
    
    estilo={'display':'flex','flex-wrap': 'wrap','justify-content':'space-between'}
    indices_carousel=[0]
    
    indices_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['_index']
    nombres_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['Nombre']
    creatividad_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['Creatividad']
    potencial_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['Potencial de Aprendizaje']
    eficiencia_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['Eficacia']
    capacidad_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['Capacidad de Replica']
    proceso_carousel = buenas_practicas[buenas_practicas['Macrocategoria'] == categoria]['Proceso']

    if indices_carousel.empty:
        buens = html.Div([dbc.Alert(
            children='Esta categoria no tiene iniciativas',
            color="warning",
            dismissable=True,
            is_open=True)])
        
    else:
        cards=[]
        
        for i in range(len(indices_carousel)):
            
            card=card_oap(
                ind_car=list(indices_carousel)[i],
                nom_car=list(nombres_carousel)[i],
                cre_car=list(creatividad_carousel)[i],
                pot_car=list(potencial_carousel)[i],
                efi_car=list(eficiencia_carousel)[i],
                cap_car=list(capacidad_carousel)[i],
                pro_car=list(proceso_carousel)[i])
                
            cards.append(card)
            
        buens = html.Div([
                html.Div(children=cards,style=estilo)
            ])

    return buens

@callback(
    Output('lecciones', 'children'),
    Input('data_categoria', 'data'),
)
def visualizacion_lecciones_aprendidas(categoria):
    
    estilo={'display':'flex','flex-wrap': 'wrap','justify-content':'space-between'}
    indices_carousel=[0]
    
    indices_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['_index']
    nombres_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['Nombre']
    creatividad_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['Creatividad']
    potencial_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['Potencial de Aprendizaje']
    eficiencia_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['Eficacia']
    capacidad_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['Capacidad de Replica']
    proceso_carousel = lecciones_aprendidas[lecciones_aprendidas['Macrocategoria'] == categoria]['Proceso']

    if indices_carousel.empty:
        
        lecci = html.Div([dbc.Alert(
            children='Esta categoria no tiene iniciativas',
            color="warning",
            dismissable=True,
            is_open=True)])
        
    else:
        cards=[]
        
        for i in range(len(indices_carousel)):
            
            card=card_oap(
                ind_car=list(indices_carousel)[i],
                nom_car=list(nombres_carousel)[i],
                cre_car=list(creatividad_carousel)[i],
                pot_car=list(potencial_carousel)[i],
                efi_car=list(eficiencia_carousel)[i],
                cap_car=list(capacidad_carousel)[i],
                pro_car=list(proceso_carousel)[i])
                
            cards.append(card)

        lecci = html.Div([
                html.Div(children=cards,style=estilo)
            ])

    return lecci