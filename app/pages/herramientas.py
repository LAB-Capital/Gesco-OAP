import os
import zipfile
import statistics
from datetime import datetime, timedelta

import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, dcc, register_page, callback

from assets.commons import overwrite_excels,load_from_local,load_from_remote

register_page(__name__, path='/herramientas')

path ='./files/separadas/'
loczip ='./files/exports/bucles.zip'
last_load_time = None

boton_recargar = dbc.Button(
    id='boton_recargar',
    children='Actualizar datasets',
    color="primary",)

boton_descargar = dbc.Button(
    id='boton_descargar',
    children='Descargar datasets',
    color="primary",)

###############################################################################################################################################################################################################
# LAYOUT    
###############################################################################################################################################################################################################

layout = html.Div([

    dbc.Row([
        dcc.Download(id='zip'),

        dbc.Col([
            html.H1(children=[],id='nom_ent',style={'font-weight':'bold'}),
            html.Br(),
            ],
            width=9,
        ),

        dbc.Col([
            boton_recargar,
            boton_descargar,
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Atención!")),
                    dbc.ModalBody("¡Se han actualizado los excel con los remotos!"),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Cerrar", id="close_recargar", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                id="modal_recargar",
                is_open=False,
            ),
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Atención!")),
                    dbc.ModalBody("¡Se han actualizado los excel con los remotos!"),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Cerrar", id="close_descargar", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                id="modal_descargar",
                is_open=False,
            ),
            ],
            width=3,
        )
        ],
        justify="between",
        
    ),
],
)

###############################################################################################################################################################################################################
# callback guardar pregunta seleccionada
###############################################################################################################################################################################################################

@callback(
    Output("modal_descargar", "is_open"),
    Output('zip', 'data'),
    Input("boton_descargar", "n_clicks"),
    Input("close_descargar", "n_clicks"),
    State("modal_descargar", "is_open"),
    prevent_initial_call=True,
)
def toggle_modal(n1, n2, is_open):
    load_from_local()
    zf = zipfile.ZipFile(loczip, "w")
    for dirname, subdirs, files in os.walk(path):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    if n1 or n2:
        return is_open,dcc.send_file(loczip)

###############################################################################################################################################################################################################
# callback guardar pregunta seleccionada
###############################################################################################################################################################################################################

@callback(
    Output("modal_recargar", "is_open"),
    Input("boton_recargar", "n_clicks"),
    Input("close_recargar", "n_clicks"),
    State("modal_recargar", "is_open"),
    prevent_initial_call=True,
)
def toggle_modal(n1, n2, is_open):
    global last_load_time

    rate_limit_interval = timedelta(minutes=5)
    current_time = datetime.now()
    if last_load_time is None or current_time >= last_load_time + rate_limit_interval:
        load_from_remote()
        overwrite_excels()
        last_load_time = current_time
    
    if n1 or n2:
        return not is_open