import dash_bootstrap_components as dbc
from dash import html, dcc, register_page

register_page(__name__, path='/')

par_spacer='1rem'
progress_thickness='.8rem'

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = html.Div([

    dbc.Row([        
        dcc.Store(id='data_pregunta',data=[],storage_type='memory'),

        dbc.Col([
            html.H1(children=[],id='nom_ent',style={'font-weight':'bold'}),
            ],
            #width=9,
        ),
        ],
        justify="between",
        
    ),
],
)
