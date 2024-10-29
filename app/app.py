from assets.commons import ENTIDAD_INICIAL,LOGO_IIP,LOGO_LAB
from assets.commons import entidades,misvis
from assets.commons import resultados_2019_df,resultados_2021_df,resultados_2023_df
from assets.commons import respuestas_2019_df,respuestas_2021_df,respuestas_2023_df

import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, dcc, callback, page_container

annos=[resultados_2019_df,resultados_2021_df,resultados_2023_df]

selector_entidad = dcc.Dropdown(
    id="selector_entidad",
    options=[{'label': x, 'value': x} for x in entidades['entidad'].values.flatten().tolist()],
    placeholder='Seleccione una entidad',
    value=ENTIDAD_INICIAL,
)

app = Dash( 
    __name__,
    external_stylesheets=[dbc.themes.UNITED, dbc.icons.FONT_AWESOME],
    use_pages=True
)

server=app.server

navbar = dbc.Container(
    dbc.Row([
        dbc.Col(
            html.A(html.H3('Gestor de respuestas IIP 2023',style={'color':'white','margin':'0','font-weight':'bold'}), className="navbar-brand", href="/"),
        width=4
        ),
        dbc.Col(
            html.Div(selector_entidad),
        width=4
        )
    ],
    justify="between",
    ),
className='content',
style={'background-color':'#e95420'},
fluid=True,
)

sidebar = html.Div(
    [
        html.A([
                    html.Img(height="50px",src=LOGO_LAB,className='logolab',style={'max-width':'14.5em','object-fit': 'contain'}),
                    html.Img(height="50px",src=LOGO_IIP,className='logoiip'),
                    ],
                    href="/",
                    style={"textDecoration": "none"},
                    
                ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-building me-2"), 
                        html.Span("Inicio")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-chart-simple me-2"),
                        html.Span("Estadísticas"),
                    ],  
                    href="/dashboards",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-magnifying-glass me-2"),
                        html.Span("Explorador"),
                    ],
                    href="/explorador",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-wrench me-2"),
                        html.Span("Herramientas"),
                    ],
                    href="/herramientas",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-light",
)

###############################################################################################################################################################################################################
# LAYOUT
###############################################################################################################################################################################################################

app.layout = html.Div(
[
    dcc.Store(id='data_entidad_uuid',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_human',data=[],storage_type='memory'),

    dcc.Store(id='data_mis',data=[],storage_type='memory'),
    dcc.Store(id='data_vis',data=[],storage_type='memory'),

    dcc.Store(id='data_pos',data=[],storage_type='memory'),
    dcc.Store(id='data_res',data=[],storage_type='memory'),

    dcc.Store(id='data_res_c1',data=[],storage_type='memory'),
    dcc.Store(id='data_res_c2',data=[],storage_type='memory'),
    dcc.Store(id='data_res_c3',data=[],storage_type='memory'),
    dcc.Store(id='data_res_c4',data=[],storage_type='memory'),

    dcc.Store(id='data_entidad_v1',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v2',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v3',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v4',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v5',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v6',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v7',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v8',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v9',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v10',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v11',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v12',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v13',data=[],storage_type='memory'),
    dcc.Store(id='data_entidad_v14',data=[],storage_type='memory'),

    navbar,
    sidebar,

    dbc.Container(
        [
            html.Div(
                [
                    page_container
                ],
                className="content",
            ),
        ],
        fluid=False,
    ),
],
style={'margin-left':'5em'}
)

###############################################################################################################################################################################################################
# callback entidad
###############################################################################################################################################################################################################

@callback(
    Output('data_entidad_uuid', 'data'),
    Output('data_entidad_human', 'data'),    
    Input('selector_entidad', 'value')
)
def sel_entidad(entidad):

    uuid = entidades[entidades['entidad'] == entidad][['_uuid']].iloc[0].item()

    '''
    print(f'{entidad} -> {uuid}')
    #'''
    return uuid,entidad

###############################################################################################################################################################################################################
# callback mision vision
###############################################################################################################################################################################################################

@callback(
    Output('data_mis', 'data'),
    Output('data_vis', 'data'),
    Input('data_entidad_uuid', 'data')
)
def misiones_y_visiones(entidad):

    mis = misvis[misvis['_uuid'] == entidad]['mision']
    vis = misvis[misvis['_uuid'] == entidad]['vision']

    if not mis.empty:
        m = mis.iloc[0]
    else:
        m = 'No se encuentra misión en listado'

    if not vis.empty:
        v = vis.iloc[0]
    else:
        v = 'No se encuentra visión en listado'

    '''
    print(f'{entidad} Mis: -> {m}')
    print(f'{entidad} Vis: -> {v}')
    #'''

    return m,v

###############################################################################################################################################################################################################
# callback posicion resultado
###############################################################################################################################################################################################################

@callback(
    Output('data_pos', 'data'),
    Output('data_res', 'data'),
    Input('data_entidad_uuid', 'data'),
)
def actualizar_pos_punt(entidad):

    lpos=[]
    lres=[]

    for anno in annos:

        res = anno[anno['_uuid'] == entidad][['res']].round(2)
        pos = anno[anno['_uuid'] == entidad][['pos']].round(2)

        if not pos.empty:
            p = pos.iloc[0].item()
        else:
            p=100

        if not res.empty:
            r = res.iloc[0].item()
        else:
            r=0

        lpos.append(p)
        lres.append(r)

    '''
    print(f'{entidad} Pos: -> {lpos}')
    print(f'{entidad} Res: -> {lres}')
    #'''

    return lpos,lres

###############################################################################################################################################################################################################
# callback resultados componentes
###############################################################################################################################################################################################################

@callback(
    Output('data_res_c1', 'data'),
    Output('data_res_c2', 'data'),
    Output('data_res_c3', 'data'),
    Output('data_res_c4', 'data'),
    Input('data_entidad_uuid', 'data'),
)
def comps_2023(entidad):

    lc1=[]
    lc2=[]
    lc3=[]
    lc4=[]

    for anno in annos:

        c1 = anno[anno['_uuid'] == entidad]['c1'].round(2)
        c2 = anno[anno['_uuid'] == entidad]['c2'].round(2)
        c3 = anno[anno['_uuid'] == entidad]['c3'].round(2)
        c4 = anno[anno['_uuid'] == entidad]['c4'].round(2)
        
        if not c1.empty:
            c1 = c1.iloc[0].item()
        else:
            c1=0.0

        if not c2.empty:
            c2 = c2.iloc[0].item()
        else:
            c2=0.0

        if not c3.empty:
            c3 = c3.iloc[0].item()
        else:
            c3=0.0

        if not c4.empty:
            c4 = c4.iloc[0].item()
        else:
            c4=0.0

        lc1.append(c1)
        lc2.append(c2)
        lc3.append(c3)
        lc4.append(c4)

    '''
    print(f'{entidad} c1:  -> {lc1}')
    print(f'{entidad} c2:  -> {lc2}')
    print(f'{entidad} c3:  -> {lc3}')
    print(f'{entidad} c4:  -> {lc4}')
    #'''

    return lc1,lc2,lc3,lc4

###############################################################################################################################################################################################################
# callback variables
###############################################################################################################################################################################################################

@callback(
    Output('data_entidad_v1', 'data'),
    Output('data_entidad_v2', 'data'),
    Output('data_entidad_v3', 'data'),
    Output('data_entidad_v4', 'data'),
    Output('data_entidad_v5', 'data'),
    Output('data_entidad_v6', 'data'),
    Output('data_entidad_v7', 'data'),
    Output('data_entidad_v8', 'data'),
    Output('data_entidad_v9', 'data'),
    Output('data_entidad_v10', 'data'),
    Output('data_entidad_v11', 'data'),
    Output('data_entidad_v12', 'data'),
    Output('data_entidad_v13', 'data'),
    Output('data_entidad_v14', 'data'),
    Input('data_entidad_uuid', 'data'),
)
def actualizar_variables(entidad):

    lv1=[]
    lv2=[]
    lv3=[]
    lv4=[]
    lv5=[]
    lv6=[]
    lv7=[]
    lv8=[]
    lv9=[]
    lv10=[]
    lv11=[]
    lv12=[]
    lv13=[]
    lv14=[]

    for anno in annos:

        v1  = anno[anno['_uuid'] == entidad]['v1'].round(2)
        v2  = anno[anno['_uuid'] == entidad]['v2'].round(2)
        v3  = anno[anno['_uuid'] == entidad]['v3'].round(2)
        v4  = anno[anno['_uuid'] == entidad]['v4'].round(2)
        v5  = anno[anno['_uuid'] == entidad]['v5'].round(2)
        v6  = anno[anno['_uuid'] == entidad]['v6'].round(2)
        v7  = anno[anno['_uuid'] == entidad]['v7'].round(2)
        v8  = anno[anno['_uuid'] == entidad]['v8'].round(2)
        v9  = anno[anno['_uuid'] == entidad]['v9'].round(2)
        v10 = anno[anno['_uuid'] == entidad]['v10'].round(2)
        v11 = anno[anno['_uuid'] == entidad]['v11'].round(2)
        v12 = anno[anno['_uuid'] == entidad]['v12'].round(2)
        v13 = anno[anno['_uuid'] == entidad]['v13'].round(2)
        v14 = anno[anno['_uuid'] == entidad]['v14'].round(2)

        if not v1.empty:
            v1 = v1.iloc[0].item()
        else:
            v1 = 0

        if not v2.empty:
            v2 = v2.iloc[0].item()
        else:
            v2 = 0

        if not v3.empty:
            v3 = v3.iloc[0].item()
        else:
            v3 = 0

        if not v4.empty:
            v4 = v4.iloc[0].item()
        else:
            v4 = 0

        if not v5.empty:
            v5 = v5.iloc[0].item()
        else:
            v5 = 0

        if not v6.empty:
            v6 = v6.iloc[0].item()
        else:
            v6 = 0

        if not v7.empty:
            v7 = v7.iloc[0].item()
        else:
            v7 = 0

        if not v8.empty:
            v8 = v8.iloc[0].item()
        else:
            v8 = 0

        if not v9.empty:
            v9 = v9.iloc[0].item()
        else:
            v9 = 0

        if not v10.empty:
            v10 = v10.iloc[0].item()
        else:
            v10 = 0

        if not v11.empty:
            v11 = v11.iloc[0].item()
        else:
            v11 = 0
        
        if not v12.empty:
            v12 = v12.iloc[0].item()
        else:
            v12 = 0

        if not v13.empty:
            v13 = v13.iloc[0].item()
        else:
            v13 = 0
        
        if not v14.empty:
            v14 = v14.iloc[0].item()
        else:
            v14 = 0

        lv1.append(v1)
        lv2.append(v2)
        lv3.append(v3)
        lv4.append(v4)
        lv5.append(v5)
        lv6.append(v6)
        lv7.append(v7)
        lv8.append(v8)
        lv9.append(v9)
        lv10.append(v10)
        lv11.append(v11)
        lv12.append(v12)
        lv13.append(v13)
        lv14.append(v14)

    '''
    print(f'{entidad} v1:  -> {lv1}')
    print(f'{entidad} v2:  -> {lv2}')
    print(f'{entidad} v3:  -> {lv3}')
    print(f'{entidad} v4:  -> {lv4}')
    print(f'{entidad} v5:  -> {lv5}')
    print(f'{entidad} v6:  -> {lv6}')
    print(f'{entidad} v7:  -> {lv7}')
    print(f'{entidad} v8:  -> {lv8}')
    print(f'{entidad} v9:  -> {lv9}')
    print(f'{entidad} v10:  -> {lv10}')
    print(f'{entidad} v11:  -> {lv11}')
    print(f'{entidad} v12:  -> {lv12}')
    print(f'{entidad} v13:  -> {lv13}')
    print(f'{entidad} v14:  -> {lv14}')
    #'''

    return lv1,lv2,lv3,lv4,lv5,lv6,lv7,lv8,lv9,lv10,lv11,lv12,lv13,lv14

###############################################################################################################################################################################################################
# Debug y puertos
###############################################################################################################################################################################################################    

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=1234)
    #app.run_server(debug=False, host='0.0.0.0', port=1234)