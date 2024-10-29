import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc, register_page, callback
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from assets.tarjeta_resumen import tarjeta_resumen_2021

register_page(__name__, path='/')

###############################################################################################################################################################################################################
# LAYOUT
###############################################################################################################################################################################################################

layout = html.Div([

    dbc.Row([

        dcc.Store(id='pregunta_seleccionada',storage_type='memory'),
        dbc.Col([
            html.H1(children=[],id='home_nom_ent',style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=12,
        ),

        ],
        justify="between",

    ),

    dbc.Row([

        dbc.Col([
            dcc.Graph(id='grafico_pos'),
            ],
            width=6,
        ),

        dbc.Col([
            dcc.Graph(id='grafico_pos'),
            ],
            width=6,
        )

        ],
        justify="between",

    ),

],
)

###############################################################################################################################################################################################################
# Callback nombre entidad
###############################################################################################################################################################################################################

@callback(
    Output('home_nom_ent', 'children'),
    Input('data_entidad_human', 'data'),
)
def get_entidad(nom_ent):
    return nom_ent

###############################################################################################################################################################################################################
# Callback tablas resumen
###############################################################################################################################################################################################################
'''
@callback(
    Output('posicion_2023', 'children'),
    Output('st', 'label'),
    Output('sc1', 'label'),
    Output('sc2', 'label'),
    Output('sc3', 'label'),
    Output('sc4', 'label'),
    Output('st', 'value'),
    Output('sc1', 'value'),
    Output('sc2', 'value'),
    Output('sc3', 'value'),
    Output('sc4', 'value'),
    Input('data_pos', 'data'),
    Input('data_res', 'data'),
    Input('data_res_c1', 'data'),
    Input('data_res_c2', 'data'),
    Input('data_res_c3', 'data'),
    Input('data_res_c4', 'data'),
)
def tabla_resumen_2023(p,r,com1,com2,com3,com4):

    pos=p[2]
    res=r[2]
    c1=com1[2]
    c2=com2[2]
    c3=com3[2]
    c4=com4[2]

    posi =pos
    res_total,st = res,res
    
    res_c1,res_c2,res_c3,res_c4 = c1,c2,c3,c4
    sc1,sc2,sc3,sc4 = c1,c2,c3,c4

    return posi,res_total,res_c1,res_c2,res_c3,res_c4,st,sc1,sc2,sc3,sc4
#'''

###############################################################################################################################################################################################################
# Callback graficar lineas
###############################################################################################################################################################################################################

@callback(
    Output('grafico_pos', 'figure'),
    Input('data_entidad_uuid', 'data'),
    Input('data_pos', 'data'),
    Input('data_res', 'data'),
)
def plotear_resultados(entidad,pos,res):
    
    diccionario={
        'Labels x':['Medición 2019','Medición 2021','Medición 2023'],
        'Puntaje Distrito':[36.7,41.28,45.02],
        'Puntaje':res,
        'Posición':pos,
    }

    v1 = line_gen(diccionario)

    return v1

###############################################################################################################################################################################################################
# Grafico lineas 
###############################################################################################################################################################################################################

def line_gen(dic):

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
	    x=dic['Labels x'],
	    y=dic['Puntaje Distrito'],
	    mode='lines+markers+text',
  	    name="Puntaje Distrito",
	    text=dic['Puntaje Distrito'],
        textposition="top center"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
	    x=dic['Labels x'],
	    y=dic['Puntaje'],
	    mode='lines+markers+text',
	    name="Puntaje",
	    text=dic['Puntaje'],
	    textposition="top center"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
	    x=dic['Labels x'],
	    y=dic['Posición'],
	    mode='lines+markers+text',
	    name="Posición",
	    text=dic['Posición'],
	    textposition="top center"),
        secondary_y=True,
    )

    fig.update_yaxes(range=[0, 100], title_text="Puntaje", secondary_y=False)
    fig.update_yaxes(range=[100, 0], title_text="Posición", secondary_y=True)

    fig.update_layout(
        template='plotly_white',
        xaxis=dict(tickmode='linear', dtick=1),
        yaxis=dict(tickmode='linear', dtick=10),
        yaxis2=dict(tickmode='linear', dtick=10),
    )

    return fig
