import os
import zipfile
import statistics

import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc, register_page, callback

import itertools

from assets.cards import card_p1_p2, card_p3_p4_p5_p6, card_p7_p8_p9_p10_p11_p12, card_p13
from assets.cards import card_p14_15_16_19_20, card_p17_18_21_22, card_p23, card_p24, card_p25_p26, card_p27
from assets.cards import card_p28, card_p29_p30
from assets.cards import card_p31_p32, card_p33_p34_p35_p36_p37_p38, card_p39

from assets.commons import p1_df, p2_df, p13_df
from assets.commons import p14_df, p15_df, p16_df, p17_df, p18_df, p19_df, p20_df, p21_df, p22_df, p23_df, p24_1_df, p24_2_df, p24_3_df, p24_4_df, p24_5_df,p25_df, p26_df, p27_df
from assets.commons import p28_df
from assets.commons import p31_df, p32_df, p33_df, p34_df, p35_df, p36_df, p37_df, p38_df, p39_df
from assets.commons import PREGUNTA_INICIAL, PREGUNTAS_TODAS, CRITS_PREGUNTAS_BASE
from assets.commons import preguntas_df
from assets.commons import entidades,misvis
from assets.commons import resultados_2019_df,respuestas_2019_df
from assets.commons import resultados_2021_df,respuestas_2021_df
from assets.commons import resultados_2023_df,respuestas_2023_df

from assets.criteria import criterio_1, criterio_2, criterio_3, criterio_4, criterio_5, criterio_6, criterio_7, criterio_8, criterio_9, criterio_10
from assets.criteria import criterio_11, criterio_12, criterio_13, criterio_14, criterio_15, criterio_16, criterio_17, criterio_18, criterio_19, criterio_20
from assets.criteria import criterio_21, criterio_22, criterio_23, criterio_24, criterio_25, criterio_26, criterio_27, criterio_28, criterio_29, criterio_30
from assets.criteria import criterio_31, criterio_32, criterio_33, criterio_34, criterio_35, criterio_36, criterio_37, criterio_38, criterio_39

register_page(__name__, path='/explorador')

par_spacer='1rem'
progress_thickness='.8rem'

selector_pregunta = dcc.Dropdown(
    id="selector_pregunta",
    options=[{'label': x, 'value': x} for x in PREGUNTAS_TODAS],
    placeholder='Seleccione la pregunta a analizar',
    value=PREGUNTA_INICIAL
)

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = html.Div([

    dbc.Row([        
        dcc.Store(id='data_pregunta',data=[],storage_type='memory'),

        dbc.Col([
            html.H1(children=[],id='nom_ent',style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=9,
        ),

        dbc.Col([
            selector_pregunta
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
                        html.H3('Pregunta'),
                        html.P(id='pregunta',children=[]),
                    ],                        
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),

                dbc.Col([
                    html.Div([
                        html.H3('Respuesta 2021'),
                        html.P(id='respuesta_2021',children=[]),
                    ],
                    style={'text-justify':'auto','text-align': 'justify'}
                    ),
                ]),
            ]),

            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3('Respuesta 2023'),
                        html.Div(id='respuesta_2023',children='',),
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
# callback guardar pregunta seleccionada
###############################################################################################################################################################################################################

@callback(
    Output('data_pregunta', 'data'),
    Input('selector_pregunta', 'value')
)
def seleccion_pregunta(value):
    if value is not None:
        salida=value
    else:
        salida = preguntas_df[preguntas_df["codigo 2023"] == "p1"]["codigo 2023"].tolist()[0]
    return salida

###############################################################################################################################################################################################################
# callback printear entidad
###############################################################################################################################################################################################################

@callback(
    Output('nom_ent', 'children'),
    Input('data_entidad_human', 'data'),
)
def get_entidad(nom_ent):
    return nom_ent

###############################################################################################################################################################################################################
# callback ver respuestas
###############################################################################################################################################################################################################

@callback(
    Output('pregunta', 'children'),
    Output('respuesta_2021', 'children'),
    Output('respuesta_2023', 'children'),

    Input('data_entidad_uuid', 'data'),
    Input('data_pregunta', 'data'),
)
def visualizacion_respuestas(entidad_seleccionada,data_pregunta):
  
    def test_empty_pregunta(entidad_seleccionada,data_pregunta):
        #pregunta textual
        try:
            pregunta = preguntas_df[preguntas_df['codigo 2023'] == data_pregunta]['pregunta 2023']
            salida_pregunta=pregunta
            out_pre='Success'
        except Exception as e_pre:
            pregunta = 'N/A'
            salida_pregunta=pregunta
            out_pre=f"|||PREGUNTA||| Couldn't load pregunta due to {e_pre}"
            print(out_pre)

        return salida_pregunta,out_pre
    
    def test_empty_respuesta_2021(entidad_seleccionada,data_pregunta):
        #respuesta 2021
        try:
            respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][data_pregunta]
            if not respuesta_2021.empty:
                salida_respuesta_2021=respuesta_2021.iloc[0]
            else:
                salida_respuesta_2021 = 'N/A'
            out_2021='Success'
        except Exception as e_res_2021:
            salida_respuesta_2021 = respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p1']
            out_2021=f"|||RESPUESTA 2021||| Couldn't load respuesta 2021 due to {e_res_2021}"
            print(out_2021)
        
        return salida_respuesta_2021,out_2021
    
    def test_empty_respuesta_2023(entidad_seleccionada,data_pregunta):
        #Respuesta 2023
        try:
            respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][data_pregunta]
            if not respuesta_2023.empty:
                salida_respuesta_2023=respuesta_2023.iloc[0]
            else:
                salida_respuesta_2023 = 'N/A'
            out_2023='Success'
        except Exception as e_res_2023:
            salida_respuesta_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p1']
            out_2023=f"|||RESPUESTA 2023||| Couldn't load respuesta 2023 due to {e_res_2023}"
            print(out_2023)

        return salida_respuesta_2023,out_2023

    pregunta,error_pregunta=test_empty_pregunta(entidad_seleccionada,data_pregunta)
    respuesta_2021,error_2021=test_empty_respuesta_2021(entidad_seleccionada,data_pregunta)
    respuesta_2023,error_2023=test_empty_respuesta_2023(entidad_seleccionada,data_pregunta)

    estilo={'display':'flex','flex-wrap': 'wrap','justify-content':'space-between'}
    indices_carousel=[0]


    if data_pregunta=='p1':

        indices_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        nombres_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        soportes_carousel = p1_df[p1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])

        
        

    elif data_pregunta=='p2':

        indices_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        nombres_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        soportes_carousel = p2_df[p2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p1_p2(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        

    elif data_pregunta=='p3':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df['p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df['p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df['p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df['p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis=0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent=0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p4':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df['p3_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df['p3_val_2'].median()
        costo_2021_dis = respuestas_2023_df['p4_val_1'].median()
        costo_2022_dis = respuestas_2023_df['p4_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p3_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p3_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p4_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p4_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis = 0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent=0

        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p5':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df['p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df['p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df['p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df['p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis =0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent=rel_enti_cos*100/rel_enti_pre
        except:
            res_ent =0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p6':

        try:
            costo_2019_2020 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            costo_2019_2020 = 'N/A'
        
        presupuesto_2021_dis = respuestas_2023_df['p5_val_1'].median()
        presupuesto_2022_dis = respuestas_2023_df['p5_val_2'].median()
        costo_2021_dis = respuestas_2023_df['p6_val_1'].median()
        costo_2022_dis = respuestas_2023_df['p6_val_2'].median()

        presupuesto_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p5_val_1']
        presupuesto_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p5_val_2']
        costo_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p6_val_1']
        costo_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p6_val_2']

        soporte_2023 = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Presupuesto: \n {costo_2019_2020}"

        cards=[]
        tipo_pregunta=['Presupuesto funcionamiento', 'Presupuesto inversión']

        rel_dist_pre = statistics.mean([float(presupuesto_2021_dis), float(presupuesto_2022_dis)])
        rel_dist_cos = statistics.mean([float(costo_2021_dis), float(costo_2022_dis)])
        try:
            res_dis = rel_dist_cos*100/rel_dist_pre
        except:
            res_dis = 0

        rel_enti_pre = statistics.mean([float(presupuesto_2021_ent.iloc[0]), float(presupuesto_2022_ent.iloc[0])])
        rel_enti_cos = statistics.mean([float(costo_2021_ent.iloc[0]), float(costo_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_cos*100/rel_enti_pre
        except:
            res_ent = 0
            
        card_2023=card_p3_p4_p5_p6(
            tip_preg=tipo_pregunta[0],

            pre_2021_dis=presupuesto_2021_dis,
            pre_2022_dis=presupuesto_2022_dis,
            pre_med_dis=rel_dist_pre,
            cos_2021_dis=costo_2021_dis,
            cos_2022_dis=costo_2022_dis,
            cos_med_dis=rel_dist_cos,
            res_dist=res_dis,

            pre_2021_ent=list(presupuesto_2021_ent)[0],
            pre_2022_ent=list(presupuesto_2022_ent)[0],
            pre_med_ent=rel_enti_pre,
            cos_2021_ent=list(costo_2021_ent)[0],
            cos_2022_ent=list(costo_2022_ent)[0],
            cos_med_ent=rel_enti_cos,
            res_enti=res_ent,

            sop_car_2023=list(soporte_2023)[0],
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p7':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df['p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df['p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df['p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df['p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df['p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df['p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis = 0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p8':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            funcionarios_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df['p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df['p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df['p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df['p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df['p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df['p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p9':

        try:
            funcionarios_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p8'])[0]
        except Exception:
            funcionarios_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df['p7_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df['p7_val_2'].median()
        manual_2021_dis = respuestas_2023_df['p8_val_1'].median()
        manual_2022_dis = respuestas_2023_df['p8_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df['p9_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df['p9_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p8_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p8_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p9_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p9_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Funcionarios: \n {funcionarios_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p10':
        
        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df['p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df['p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df['p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df['p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df['p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df['p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p11':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            contratistas_ent = 'N/A'
        
        cantidad_2021_dis = respuestas_2023_df['p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df['p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df['p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df['p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df['p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df['p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])

        
        
        
    elif data_pregunta=='p12':

        try:
            contratistas_ent = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p11'])[0]
        except Exception:
            contratistas_ent = 'N/A'

        cantidad_2021_dis = respuestas_2023_df['p10_val_1'].median()
        cantidad_2022_dis = respuestas_2023_df['p10_val_2'].median()
        manual_2021_dis = respuestas_2023_df['p11_val_1'].median()
        manual_2022_dis = respuestas_2023_df['p11_val_2'].median()
        ocasionales_2021_dis = respuestas_2023_df['p12_val_1'].median()
        ocasionales_2022_dis = respuestas_2023_df['p12_val_2'].median()
        
        cantidad_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_1']
        cantidad_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_2']
        manual_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p11_val_1']
        manual_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p11_val_2']
        ocasionales_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p12_val_1']
        ocasionales_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p12_val_2']

        soporte = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        salida_respuesta_2021=f"Funcionarios: \n {contratistas_ent}"

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(cantidad_2021_dis), float(cantidad_2022_dis)])
        rel_dist_man = statistics.mean([float(manual_2021_dis), float(manual_2022_dis)])
        rel_dist_oca = statistics.mean([float(ocasionales_2021_dis), float(ocasionales_2022_dis)])
        try:
            res_dis = rel_dist_man*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(cantidad_2021_ent.iloc[0]), float(cantidad_2022_ent.iloc[0])])
        rel_enti_man = statistics.mean([float(manual_2021_ent.iloc[0]), float(manual_2022_ent.iloc[0])])
        rel_enti_oca = statistics.mean([float(ocasionales_2021_ent.iloc[0]), float(ocasionales_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_man*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p7_p8_p9_p10_p11_p12(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=cantidad_2021_dis,
            can_2022_dis=cantidad_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=manual_2021_dis,
            fun_2022_dis=manual_2022_dis,
            fun_med_dis=rel_dist_man,
            oca_2021_dis=ocasionales_2021_dis,
            oca_2022_dis=ocasionales_2022_dis,
            oca_med_dis=rel_dist_oca,
            res_dist=res_dis,

            can_2021_ent=list(cantidad_2021_ent)[0],
            can_2022_ent=list(cantidad_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(manual_2021_ent)[0],
            fun_2022_ent=list(manual_2022_ent)[0],
            fun_med_ent=rel_enti_man,
            oca_2021_ent=list(ocasionales_2021_ent)[0],
            oca_2022_ent=list(ocasionales_2022_ent)[0],
            oca_med_ent=rel_enti_oca,
            res_enti=res_ent,

            sop_car=list(soporte)[0]
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p13':

        indices_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        costo_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cos']
        soportes_carousel = p13_df[p13_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p13(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        cos_car=list(costo_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p14':

        indices_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        act_1_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_1']
        act_2_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_2']
        act_3_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_3']
        act_4_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_4']
        act_5_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_5']
        acciones_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_post']
        soportes_carousel = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][data_pregunta])[0]
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:

                try:
                    act_4_otr = p14_df[p14_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]                
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p15':

        indices_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        act_1_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_1']
        act_2_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_2']
        act_3_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_3']
        act_4_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_4']
        act_5_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_5']
        acciones_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_post']
        soportes_carousel = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                try:
                    act_4_otr = p15_df[p15_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p16':

        indices_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_rom']
        act_1_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_1']
        act_2_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_2']
        act_3_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_3']
        act_4_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_4']
        act_5_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_5']
        acciones_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_post']
        soportes_carousel = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""
        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                try:
                    act_4_otr = p16_df[p16_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p17':
        
        indices_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_can']
        usuarios_carousel = p17_df[p17_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if indices_carousel.empty:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            
            
        
        
    elif data_pregunta=='p18':

        indices_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act']
        usuarios_carousel = p18_df[p18_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p17'])[0]

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if indices_carousel.empty:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad=["N/A"]
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            

        
        
    elif data_pregunta=='p19':

        indices_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        act_1_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_1']
        act_2_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_2']
        act_3_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_3']
        act_4_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_4']
        act_5_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_5']
        acciones_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_post']
        soportes_carousel = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                try:
                    act_4_otr = p19_df[p19_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p20':

        indices_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        act_1_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_1']
        act_2_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_2']
        act_3_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_3']
        act_4_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_4']
        act_5_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act/{data_pregunta}_act_5']
        acciones_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_post']
        soportes_carousel = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                try:
                    act_4_otr = p20_df[p20_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_otr']
                except:
                    act_4_otr=['N/A' for x in range(len(indices_carousel)+1)]

                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p14_15_16_19_20(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        act_1=list(act_1_carousel)[i],
                        act_2=list(act_2_carousel)[i],
                        act_3=list(act_3_carousel)[i],
                        act_4=list(act_4_carousel)[i],
                        act_5=list(act_5_carousel)[i],
                        act_otr=list(act_4_otr)[i],
                        acc_car=list(acciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p21':

        indices_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_can']
        usuarios_carousel = p21_df[p21_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if indices_carousel.empty:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            
            
        
        
    elif data_pregunta=='p22':

        indices_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_act']
        usuarios_carousel = p22_df[p22_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada]['p21'])[0]

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if indices_carousel.empty:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            salida_criterios_entidad='N/A'
        else:
            cards=[]
            
            for i in range(len(indices_carousel)):
                
                card=card_p17_18_21_22(
                    ind_car=list(indices_carousel)[i],
                    nom_car=list(codigos_carousel)[i],
                    usr_car=list(usuarios_carousel)[i])
                cards.append(card)

            salida_respuesta_2023 = html.Div([
                    html.Div(children=cards,style=estilo)
                ])
            
            
        
        
    elif data_pregunta=='p23':

        indices_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        soportes_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']
        usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr/{data_pregunta}_usr_1']
        usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr/{data_pregunta}_usr_2']
        usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_usr/{data_pregunta}_usr_3']
        prototipado = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_pro']
        
        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                try:
                    vali_usr_1_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_val/{data_pregunta}_val_1']
                    vali_usr_2_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_val/{data_pregunta}_val_2']
                    vali_usr_3_carousel = p23_df[p23_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_val/{data_pregunta}_val_3']
                except:
                    vali_usr_1_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_2_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                    vali_usr_3_carousel = ['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p23(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        us1_car=list(usr_1_carousel)[i],
                        us2_car=list(usr_2_carousel)[i],
                        us3_car=list(usr_3_carousel)[i],
                        pro_car=list(prototipado)[i],
                        va1_car=list(vali_usr_1_carousel)[i],
                        va2_car=list(vali_usr_2_carousel)[i],
                        va3_car=list(vali_usr_3_carousel)[i],
                        sop_car=list(soportes_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p24':

        p24_1_indices_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_1_codigos_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_1_nom']
        p24_1_descripciones_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_1_des']
        p24_1_impartio_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_1_imp']
        p24_1_asistentes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_1_asi']
        p24_1_soportes_carousel = p24_1_df[p24_1_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_1_sop']

        p24_2_indices_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_2_codigos_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_2_nom']
        p24_2_descripciones_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_2_des']
        p24_2_impartio_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_2_imp']
        p24_2_asistentes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_2_asi']
        p24_2_soportes_carousel = p24_2_df[p24_2_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_2_sop']

        p24_3_indices_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_3_codigos_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_3_nom']
        p24_3_descripciones_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_3_des']
        p24_3_impartio_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_3_imp']
        p24_3_asistentes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_3_asi']
        p24_3_soportes_carousel = p24_3_df[p24_3_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_3_sop']

        p24_4_indices_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_4_codigos_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_4_nom']
        p24_4_descripciones_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_4_des']
        p24_4_impartio_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_4_imp']
        p24_4_asistentes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_4_asi']
        p24_4_soportes_carousel = p24_4_df[p24_4_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_4_sop']

        p24_5_indices_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada]['_index']
        p24_5_codigos_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_5_nom']
        p24_5_descripciones_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_5_des']
        p24_5_impartio_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_5_imp']
        p24_5_asistentes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_5_asi']
        p24_5_soportes_carousel = p24_5_df[p24_5_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_5_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':

            if not p24_1_indices_carousel.empty:
                cards1=[]
                for i in range(len(p24_1_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_1_indices_carousel)[i],
                        nom_car=list(p24_1_codigos_carousel)[i],
                        des_car=list(p24_1_descripciones_carousel)[i],
                        imp_car=list(p24_1_impartio_carousel)[i],
                        asi_car=list(p24_1_asistentes_carousel)[i],
                        sop_car=list(p24_1_soportes_carousel)[i])
                    cards1.append(card)
            else:
                cards1=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if not p24_2_indices_carousel.empty:
                cards2=[]
                for i in range(len(p24_2_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_2_indices_carousel)[i],
                        nom_car=list(p24_2_codigos_carousel)[i],
                        des_car=list(p24_2_descripciones_carousel)[i],
                        imp_car=list(p24_2_impartio_carousel)[i],
                        asi_car=list(p24_2_asistentes_carousel)[i],
                        sop_car=list(p24_2_soportes_carousel)[i])
                    cards2.append(card)
            else:
                cards2=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if not p24_3_indices_carousel.empty:
                cards3=[]
                for i in range(len(p24_3_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_3_indices_carousel)[i],
                        nom_car=list(p24_3_codigos_carousel)[i],
                        des_car=list(p24_3_descripciones_carousel)[i],
                        imp_car=list(p24_3_impartio_carousel)[i],
                        asi_car=list(p24_3_asistentes_carousel)[i],
                        sop_car=list(p24_3_soportes_carousel)[i])
                    cards3.append(card)
            else:
                cards3=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            if not p24_4_indices_carousel.empty:
                cards4=[]
                for i in range(len(p24_4_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_4_indices_carousel)[i],
                        nom_car=list(p24_4_codigos_carousel)[i],
                        des_car=list(p24_4_descripciones_carousel)[i],
                        imp_car=list(p24_4_impartio_carousel)[i],
                        asi_car=list(p24_4_asistentes_carousel)[i],
                        sop_car=list(p24_4_soportes_carousel)[i])
                    cards4.append(card)
            else:
                cards4=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]
            
            if not p24_5_indices_carousel.empty:
                cards5=[]
                for i in range(len(p24_5_indices_carousel)):
                    
                    card=card_p24(
                        ind_car=list(p24_5_indices_carousel)[i],
                        nom_car=list(p24_5_codigos_carousel)[i],
                        des_car=list(p24_5_descripciones_carousel)[i],
                        imp_car=list(p24_5_impartio_carousel)[i],
                        asi_car=list(p24_5_asistentes_carousel)[i],
                        sop_car=list(p24_5_soportes_carousel)[i])
                    cards5.append(card)
            else:
                cards5=[html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)]),html.Br()]

            salida_respuesta_2023 = html.Div([
                    html.H5('Eventos Auspiciados y/o financiados directamente por esa entidad'),
                    html.Div(children=cards1,style=estilo),
                    html.H5('Eventos Auspiciados y/o financiados directamente por otras entidades'),
                    html.Div(children=cards2,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por esa entidad'),
                    html.Div(children=cards3,style=estilo),
                    html.H5('Formación Auspiciada y/o financiada directamente por otras entidades'),
                    html.Div(children=cards4,style=estilo),
                    html.H5('Otras actividades de esa entidad'),
                    html.Div(children=cards5,style=estilo),
                ])
            
            
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p25':

        indices_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        recomendacion_carousel = p25_df[p25_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_rec']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p26':

        indices_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        recomendacion_carousel = p26_df[p26_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_rec']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""
        except:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p25_p26(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        rec_car=list(recomendacion_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p27':

        indices_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        tematica_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des_001']
        tamano_carousel = p27_df[p27_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_c']

        try:
            salida_respuesta_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p27(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        tem_car=list(tematica_carousel)[i],
                        tam_car=list(tamano_carousel)[i])
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p28':

        indices_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['nom_inno']
        implementado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_imp']
        validado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_val']
        metodologia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['meto']
        beneficia_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_ben']
        ahorro_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_aho']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                if list(beneficia_carousel)[0]=='Si':
                    beneficiados_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['beneficiados']
                else:
                    beneficiados_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                
                if list(ahorro_carousel)[0]=='Si':
                    ahorrado_carousel = p28_df[p28_df['_submission__uuid'] == entidad_seleccionada]['recursos_ahorrados']
                else:
                    ahorrado_carousel=['N/A' for x in range(len(indices_carousel)+1)]
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p28(
                        ind_car=list(indices_carousel)[i],
                        nom_car=list(codigos_carousel)[i],
                        imp_car=list(implementado_carousel)[i],
                        val_car=list(validado_carousel)[i],
                        met_car=list(metodologia_carousel)[i],
                        ben_car=list(beneficia_carousel)[i],
                        aho_car=list(ahorro_carousel)[i],
                        b1_car=list(beneficiados_carousel)[i],
                        a1_car=list(ahorrado_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p29':

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df['p7_val_1'].median()
        total_2022_dis = respuestas_2023_df['p7_val_2'].median()
        formados_2021_dis = respuestas_2023_df['p29_val_1'].median()
        formados_2022_dis = respuestas_2023_df['p29_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p7_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p29_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p29_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        try:
            res_dis = rel_dist_for*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_for*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[0],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p30':

        try:
            form_2021 = list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]
        except Exception:
            form_2021 = 'N/A'

        salida_respuesta_2021=f"Funcionarios y contratistas formados: \n {form_2021}"

        total_2021_dis = respuestas_2023_df['p10_val_1'].median()
        total_2022_dis = respuestas_2023_df['p10_val_2'].median()
        formados_2021_dis = respuestas_2023_df['p30_val_1'].median()
        formados_2022_dis = respuestas_2023_df['p30_val_2'].median()
        
        total_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_1']
        total_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p10_val_2']
        formados_2021_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p30_val_1']
        formados_2022_ent = respuestas_2023_df[respuestas_2023_df['_uuid'] == entidad_seleccionada]['p30_val_2']

        cards=[]
        tipo_pregunta=['Funcionarios', 'Contratistas']

        rel_dist_tot = statistics.mean([float(total_2021_dis), float(total_2022_dis)])
        rel_dist_for = statistics.mean([float(formados_2021_dis), float(formados_2022_dis)])
        try:
            res_dis = rel_dist_for*100/rel_dist_tot
        except:
            res_dis=0

        rel_enti_tot = statistics.mean([float(total_2021_ent.iloc[0]), float(total_2022_ent.iloc[0])])
        rel_enti_for = statistics.mean([float(formados_2021_ent.iloc[0]), float(formados_2022_ent.iloc[0])])
        try:
            res_ent = rel_enti_for*100/rel_enti_tot
        except:
            res_ent=0
            
        card_2023=card_p29_p30(
            tip_preg=tipo_pregunta[1],

            can_2021_dis=total_2021_dis,
            can_2022_dis=total_2022_dis,
            can_med_dis=rel_dist_tot,
            fun_2021_dis=formados_2021_dis,
            fun_2022_dis=formados_2022_dis,
            fun_med_dis=rel_dist_for,
            res_dist=res_dis,

            can_2021_ent=list(total_2021_ent)[0],
            can_2022_ent=list(total_2022_ent)[0],
            can_med_ent=rel_enti_tot,
            fun_2021_ent=list(formados_2021_ent)[0],
            fun_2022_ent=list(formados_2022_ent)[0],
            fun_med_ent=rel_enti_for,
            res_enti=res_ent,
        )

        cards.append(card_2023)

        salida_respuesta_2023 = html.Div([
                html.Div(children=cards,style=estilo)
            ])
        
        
        
        
    elif data_pregunta=='p31':

        indices_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        nombres_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        soportes_carousel = p31_df[p31_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p32':

        indices_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        nombres_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_nom']
        descripciones_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_des']
        soportes_carousel = p32_df[p32_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p31_p32(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        nom_car=list(nombres_carousel)[i],
                        des_car=list(descripciones_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p33':

        indices_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p33_df[p33_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p34':

        indices_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p34_df[p34_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p35':

        indices_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p35_df[p35_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p36':

        indices_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p36_df[p36_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p37':

        indices_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p37_df[p37_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p38':

        indices_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p38_df[p38_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p33_p34_p35_p36_p37_p38(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    elif data_pregunta=='p39':

        indices_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada]['_index']
        codigos_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_cod']
        soportes_carousel = p39_df[p39_df['_submission__uuid'] == entidad_seleccionada][f'{data_pregunta}_sop']

        try:
            salida_respuesta_2021 = f"""{list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'{data_pregunta}'])[0]}\n a través de: {list(respuestas_2021_df[respuestas_2021_df['_uuid'] == entidad_seleccionada][f'r_{data_pregunta}'])[0]}"""

        except Exception:
            salida_respuesta_2021 = 'No registra iniciativas'

        if respuesta_2023 == 'Si':
            if indices_carousel.empty:
                salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
                
            else:
                cards=[]
                
                for i in range(len(indices_carousel)):
                    
                    card=card_p39(
                        ind_car=list(indices_carousel)[i],
                        cod_car=list(codigos_carousel)[i],
                        sop_car=list(soportes_carousel)[i],
                        )
                    cards.append(card)

                salida_respuesta_2023 = html.Div([
                        html.Div(children=cards,style=estilo)
                    ])
                
        elif respuesta_2023 == 'No':
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Esta entidad no tiene iniciativas',
                    color="warning",
                    dismissable=True,
                    is_open=True)])
            
        else:
            salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Respuesta 2023 != Si',
                    color="danger",
                    dismissable=True,
                    is_open=True)])
            

        
        
    else:
        salida_respuesta_2023 = html.Div([dbc.Alert(
                    children='Caso no definido',
                    color="danger",
                    dismissable=True,
                    is_open=True)])


    return pregunta,salida_respuesta_2021,salida_respuesta_2023