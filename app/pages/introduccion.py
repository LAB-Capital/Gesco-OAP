import dash_bootstrap_components as dbc
from dash import html, dcc, register_page

register_page(__name__, path='/')

par_spacer='1rem'
progress_thickness='.8rem'

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = dbc.Container(
    [
        dbc.Row([
            dcc.Store(id='data_pregunta',data=[],storage_type='memory'),
            dbc.Col([
                html.H1(
                    'Buenas prácticas y lecciones aprendidas 2020-2024',
                    style={'font-weight':'bold'}
                ),
            ],
            ),
        ],
        ),
        dbc.Row([
            dbc.Col([
                html.P(
                    '''La Veeduría Distrital, en cumplimiento de la Política de Gestión del conocimiento, realiza la documentación y evaluación de las Buenas Prácticas y Lecciones Aprendidas de la entidad, como acción clave de la estrategia de fortalecimiento de la cultura de compartir y difundir, con el objetivo de fortalecer los procesos de aprendizaje organizacional.''',
                    style={'textAlign': 'justify'}
                ),
                html.P(
                    '''Según el Departamento Administrativo de Función Pública - DAFP, las buenas prácticas se pueden entender como aquellas actuaciones concretas, prácticas o soluciones basadas en ciertos conocimientos, investigaciones o experimentos y que, gracias a su utilidad y sencillez, brindan herramientas, métodos y técnicas, que pueden aumentar las posibilidades de éxito de la gestión y servir de ejemplo para otras entidades.''',
                    style={'textAlign': 'justify'}
                ),
                html.P(
                    '''Para la vigencia del 2024, se documentaron en total 54 buenas prácticas y 49 lecciones aprendidas, las cuales entraron a una primera fase de evaluación en términos de cumplimiento de los criterios definidos por la Oficina Asesora de Planeación y posteriormente, se clasificación en las macro categorías propuestas por el Índice de Innovación Publica:''',
                    style={'textAlign': 'justify'}
                ),
            ],
            ),
        ],
        style={'padding-top':'2rem'}
        ),
        dbc.Row([
            dbc.Col([
                html.Img(
                    src='./static/BUENAS PRACTICAS.png',
                    style={
                        'width': '100%',  # Set the width
                        'height': 'auto',  # Maintain aspect ratio
                    }
                ),
            ],
            width=6
            ),
            dbc.Col([
                html.Img(
                    src='./static/LECCIONES APRENDIDAS.png',
                    style={
                        'width': '100%',  # Set the width
                        'height': 'auto',  # Maintain aspect ratio
                    }
                ),
            ],
            width=6
            ),
        ],
        style={'padding-top':'2rem','padding-bottom':'2rem'}
        ),
        dbc.Row([
            dbc.Col([
                html.P(
                    '''De esta primera fase se seleccionaron un total de 12 Buenas Prácticas y 11 Lecciones Aprendidas.''',
                    style={'textAlign': 'justify'}
                ),
                html.P(
                    '''En una segunda fase, las buenas prácticas y lecciones aprendidas, se evaluaron con la metodología del Banco de Buenas Prácticas del Departamento de Función Pública teniendo en cuenta los siguientes aspectos:''',
                    style={'textAlign': 'justify'}
                ),
            ],
            ),
        ],
        ),
        dbc.Row([
            dbc.Col([
                html.Img(
                    src='./static/2da_fase.png',
                    style={
                        'width': '100%',  # Set the width
                        'height': 'auto',  # Maintain aspect ratio
                    }
                ),
            ],
            ),
        ],
        ),
        dbc.Row([
            dbc.Col([
                html.P(
                    '''Los invitamos a consultar y aplicar las buenas prácticas y lecciones aprendidas como parte de la gestión del conocimiento de la entidad, con el fin de optimizar procesos y fortalecer el desempeño organizacional. ''',
                    style={'textAlign': 'justify'}
                ),
                html.P(
                    '''Al incorporar experiencias previas y metodologías probadas, no solo se mejora la eficiencia en la ejecución de tareas, sino que se minimizan riesgos y se evitan errores recurrentes. Implementar estas prácticas promueve un entorno de mejora continua, fomenta la innovación y asegura que el conocimiento generado en cada etapa de los procesos de la Veeduría Distrital se conserve y potencie para el beneficio de toda la entidad.''',
                    style={'textAlign': 'justify'}
                ),
            ],
            ),
        ],
        ),
    ],
    fluid=True
)
