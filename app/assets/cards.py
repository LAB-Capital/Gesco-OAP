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
