import pandas as pd
import requests
import io
import os

from tools.Autocomputo import autocomputar_2019,autocomputar_2021,autocomputar_2023

LOGO_LAB='./static/logolab.png'
LOGO_IIP='./static/logoiip.png'
PREGUNTAS_TODAS=    ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BINARIAS= ['p1','p2','p13','p14','p15','p16',            'p19','p20',            'p23','p24','p25','p26','p27','p28','p29','p30','p31','p32','p33','p34','p35','p36','p37','p38','p39']
PREGUNTAS_BUCLES=   ['p1','p2','p13','p14','p15','p16','p17','p18','p19','p20','p21','p22','p23','p24_1','p24_2','p24_3','p24_4','p24_5','p25','p26','p27','p28',            'p31','p32','p33','p34','p35','p36','p37','p38','p39']
ENTIDAD_INICIAL='Veeduría Distrital'
PREGUNTA_INICIAL='p1'

baselink='https://raw.githubusercontent.com/LAB-Capital/Datos-indice/main'


try:
    sesh = requests.Session()
except Exception as e:
    print(e)

try:
    sesh.auth = (username, token)
except Exception as e:
    print(e)

def remote_excel_loader(sesh, file):
    try:
        response = sesh.get(f'{baselink}{file}')
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except Exception as e:
        print(f'Failed to get the file: {e}')
        return None  # Return None if request fails

    try:
        df = pd.read_excel(io.BytesIO(response.content))
        return df
    except Exception as e:
        print(f'Failed to load the Excel file: {e}')
        return None  # Return None if reading the Excel fails

sepa='2023/'

UBI_AR={
    'p1':             f'/separadas/{sepa}/repeat_p1.xlsx',
    'p2':             f'/separadas/{sepa}/repeat_p2.xlsx',
    'p13':            f'/separadas/{sepa}/repeat_p13.xlsx',
    'p14':            f'/separadas/{sepa}/repeat_p14.xlsx',
    'p15':            f'/separadas/{sepa}/repeat_p15.xlsx',
    'p16':            f'/separadas/{sepa}/repeat_p16.xlsx',
    'p17':            f'/separadas/{sepa}/repeat_p17.xlsx',
    'p18':            f'/separadas/{sepa}/repeat_p18.xlsx',
    'p19':            f'/separadas/{sepa}/repeat_p19.xlsx',
    'p20':            f'/separadas/{sepa}/repeat_p20.xlsx',
    'p21':            f'/separadas/{sepa}/repeat_p21.xlsx',
    'p22':            f'/separadas/{sepa}/repeat_p22.xlsx',
    'p23':            f'/separadas/{sepa}/repeat_p23.xlsx',
    'p24_1':          f'/separadas/{sepa}/repeat_p24_1.xlsx',
    'p24_2':          f'/separadas/{sepa}/repeat_p24_2.xlsx',
    'p24_3':          f'/separadas/{sepa}/repeat_p24_3.xlsx',
    'p24_4':          f'/separadas/{sepa}/repeat_p24_4.xlsx',
    'p24_5':          f'/separadas/{sepa}/repeat_p24_5.xlsx',
    'p25':            f'/separadas/{sepa}/repeat_p25.xlsx',
    'p26':            f'/separadas/{sepa}/repeat_p26.xlsx',
    'p27':            f'/separadas/{sepa}/repeat_p27.xlsx',
    'p28':            f'/separadas/{sepa}/repeat_p28.xlsx',
    'p31':            f'/separadas/{sepa}/repeat_p31.xlsx',
    'p32':            f'/separadas/{sepa}/repeat_p32.xlsx',
    'p33':            f'/separadas/{sepa}/repeat_p33.xlsx',
    'p34':            f'/separadas/{sepa}/repeat_p34.xlsx',
    'p35':            f'/separadas/{sepa}/repeat_p35.xlsx',
    'p36':            f'/separadas/{sepa}/repeat_p36.xlsx',
    'p37':            f'/separadas/{sepa}/repeat_p37.xlsx',
    'p38':            f'/separadas/{sepa}/repeat_p38.xlsx',
    'p39':            f'/separadas/{sepa}/repeat_p39.xlsx',
    'entidades':      '/entidades/entidades.xlsx',
    'misvis':         '/misvis/misvis.xlsx',
    'preguntas':      '/preguntas/preguntas.xlsx',
    'respuestas_2019':'/respuestas/2019/respuestas_2019.xlsx',
    'respuestas_2021':'/respuestas/2021/respuestas_2021.xlsx',
    'respuestas_2023':'/respuestas/2023/respuestas_2023.xlsx',
    'resultados_2019':'/resultados/2019/resultados_2019.xlsx',
    'resultados_2021':'/resultados/2021/resultados_2021.xlsx',
    'resultados_2023':'/resultados/2023/resultados_2023.xlsx',
}

###############################################################################################################################################################################################################
# Cargar desde local
###############################################################################################################################################################################################################

def load_from_local_basic():
    print('Loading basic from local')
    entidades =          pd.read_excel(f"./files{UBI_AR['entidades']}")
    misvis =             pd.read_excel(f"./files{UBI_AR['misvis']}")
    preguntas_df =       pd.read_excel(f"./files{UBI_AR['preguntas']}")
    return entidades,misvis,preguntas_df

def load_from_local_respuestas_resultados():
    print('Loading respuestas/resultados from local')
    respuestas_2019_df = pd.read_excel(f"./files{UBI_AR['respuestas_2019']}")
    respuestas_2021_df = pd.read_excel(f"./files{UBI_AR['respuestas_2021']}")
    respuestas_2023_df = pd.read_excel(f"./files{UBI_AR['respuestas_2023']}")

    r2019=remote_excel_loader(sesh,UBI_AR['resultados_2019'])
    r2021=remote_excel_loader(sesh,UBI_AR['resultados_2021'])
    r2023=remote_excel_loader(sesh,UBI_AR['resultados_2023'])
    resultados_2019_df=autocomputar_2019(r2019)
    resultados_2021_df=autocomputar_2021(r2021)
    resultados_2023_df=autocomputar_2023(r2023)
    return respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df

def load_from_local_separadas_c1():
    print('Loading c1 from local')
    p1_df =              pd.read_excel(f"./files/{UBI_AR['p1']}")
    p2_df =              pd.read_excel(f"./files/{UBI_AR['p2']}")
    p13_df =             pd.read_excel(f"./files/{UBI_AR['p13']}")
    return p1_df,p2_df,p13_df

def load_from_local_separadas_c2():
    print('Loading c2 from local')
    p14_df =             pd.read_excel(f"./files/{UBI_AR['p14']}")
    p15_df =             pd.read_excel(f"./files/{UBI_AR['p15']}")
    p16_df =             pd.read_excel(f"./files/{UBI_AR['p16']}")
    p17_df =             pd.read_excel(f"./files/{UBI_AR['p17']}")
    p18_df =             pd.read_excel(f"./files/{UBI_AR['p18']}")
    p19_df =             pd.read_excel(f"./files/{UBI_AR['p19']}")
    p20_df =             pd.read_excel(f"./files/{UBI_AR['p20']}")
    p21_df =             pd.read_excel(f"./files/{UBI_AR['p21']}")
    p22_df =             pd.read_excel(f"./files/{UBI_AR['p22']}")
    p23_df =             pd.read_excel(f"./files/{UBI_AR['p23']}")
    p24_1_df =           pd.read_excel(f"./files/{UBI_AR['p24_1']}")
    p24_2_df =           pd.read_excel(f"./files/{UBI_AR['p24_2']}")
    p24_3_df =           pd.read_excel(f"./files/{UBI_AR['p24_3']}")
    p24_4_df =           pd.read_excel(f"./files/{UBI_AR['p24_4']}")
    p24_5_df =           pd.read_excel(f"./files/{UBI_AR['p24_5']}")
    p25_df =             pd.read_excel(f"./files/{UBI_AR['p25']}")
    p26_df =             pd.read_excel(f"./files/{UBI_AR['p26']}")
    p27_df =             pd.read_excel(f"./files/{UBI_AR['p27']}")
    return p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df

def load_from_local_separadas_c3():
    print('Loading c3 from local')
    p28_df =             pd.read_excel(f"./files/{UBI_AR['p28']}")
    return p28_df

def load_from_local_separadas_c4():
    print('Loading c4 from local')
    p31_df =             pd.read_excel(f"./files/{UBI_AR['p31']}")
    p32_df =             pd.read_excel(f"./files/{UBI_AR['p32']}")
    p33_df =             pd.read_excel(f"./files/{UBI_AR['p33']}")
    p34_df =             pd.read_excel(f"./files/{UBI_AR['p34']}")
    p35_df =             pd.read_excel(f"./files/{UBI_AR['p35']}")
    p36_df =             pd.read_excel(f"./files/{UBI_AR['p36']}")
    p37_df =             pd.read_excel(f"./files/{UBI_AR['p37']}")
    p38_df =             pd.read_excel(f"./files/{UBI_AR['p38']}")
    p39_df =             pd.read_excel(f"./files/{UBI_AR['p39']}")
    return p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df

###############################################################################################################################################################################################################
# LLamar desde internet
###############################################################################################################################################################################################################

def load_from_remote_basic():
    print('Loading basic from remote')
    try:
        entidades =        remote_excel_loader(sesh,UBI_AR['entidades'])
        misvis =           remote_excel_loader(sesh,UBI_AR['misvis'])
        preguntas_df =     remote_excel_loader(sesh,UBI_AR['preguntas'])
        return entidades,misvis,preguntas_df
    except Exception as e:
        print(e)
        return None, None, None

def load_from_remote_respuestas_resultados():
    print('Loading respuestas/resultados from remote')
    try:
        respuestas_2019_df=remote_excel_loader(sesh,UBI_AR['respuestas_2019'])
        respuestas_2021_df=remote_excel_loader(sesh,UBI_AR['respuestas_2021'])
        respuestas_2023_df=remote_excel_loader(sesh,UBI_AR['respuestas_2023'])

        r2019=remote_excel_loader(sesh,UBI_AR['resultados_2019'])
        r2021=remote_excel_loader(sesh,UBI_AR['resultados_2021'])
        r2023=remote_excel_loader(sesh,UBI_AR['resultados_2023'])
        resultados_2019_df=autocomputar_2019(r2019)
        resultados_2021_df=autocomputar_2021(r2021)
        resultados_2023_df=autocomputar_2023(r2023)
        return respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df
    except Exception as e:
        print(e)
        return None, None, None, None, None, None

def load_from_remote_separadas_c1():
    print('Loading c1 from remote')
    try:
        p1_df=             remote_excel_loader(sesh,UBI_AR['p1'])
        p2_df=             remote_excel_loader(sesh,UBI_AR['p2'])
        p13_df=            remote_excel_loader(sesh,UBI_AR['p13'])
        return p1_df,p2_df,p13_df
    except Exception as e:
        print(e)
        return None, None, None

def load_from_remote_separadas_c2():
    print('Loading c2 from remote')
    p14_df=            remote_excel_loader(sesh,UBI_AR['p14'])
    p15_df=            remote_excel_loader(sesh,UBI_AR['p15'])
    p16_df=            remote_excel_loader(sesh,UBI_AR['p16'])
    p17_df=            remote_excel_loader(sesh,UBI_AR['p17'])
    p18_df=            remote_excel_loader(sesh,UBI_AR['p18'])
    p19_df=            remote_excel_loader(sesh,UBI_AR['p19'])
    p20_df=            remote_excel_loader(sesh,UBI_AR['p20'])
    p21_df=            remote_excel_loader(sesh,UBI_AR['p21'])
    p22_df=            remote_excel_loader(sesh,UBI_AR['p22'])
    p23_df=            remote_excel_loader(sesh,UBI_AR['p23'])
    p24_1_df=          remote_excel_loader(sesh,UBI_AR['p24_1'])
    p24_2_df=          remote_excel_loader(sesh,UBI_AR['p24_2'])
    p24_3_df=          remote_excel_loader(sesh,UBI_AR['p24_3'])
    p24_4_df=          remote_excel_loader(sesh,UBI_AR['p24_4'])
    p24_5_df=          remote_excel_loader(sesh,UBI_AR['p24_5'])
    p25_df=            remote_excel_loader(sesh,UBI_AR['p25'])
    p26_df=            remote_excel_loader(sesh,UBI_AR['p26'])
    p27_df=            remote_excel_loader(sesh,UBI_AR['p27'])
    return p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df

def load_from_remote_separadas_c3():
    print('Loading c3 from remote')
    p28_df=            remote_excel_loader(sesh,UBI_AR['p28'])
    return p28_df

def load_from_remote_separadas_c4():
    print('Loading c4 from remote')
    p31_df=            remote_excel_loader(sesh,UBI_AR['p31'])
    p32_df=            remote_excel_loader(sesh,UBI_AR['p32'])
    p33_df=            remote_excel_loader(sesh,UBI_AR['p33'])
    p34_df=            remote_excel_loader(sesh,UBI_AR['p34'])
    p35_df=            remote_excel_loader(sesh,UBI_AR['p35'])
    p36_df=            remote_excel_loader(sesh,UBI_AR['p36'])
    p37_df=            remote_excel_loader(sesh,UBI_AR['p37'])
    p38_df=            remote_excel_loader(sesh,UBI_AR['p38'])
    p39_df=            remote_excel_loader(sesh,UBI_AR['p39'])
    return p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df

###############################################################################################################################################################################################################
# definir cargas
###############################################################################################################################################################################################################

def load_from_local():
    print('Loading from local:')
    global entidades,misvis,preguntas_df
    global respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df
    global p1_df,p2_df,p13_df
    global p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df
    global p28_df
    global p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df

    entidades,misvis,preguntas_df =                                                                                                           load_from_local_basic()
    respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df =                       load_from_local_respuestas_resultados()
    p1_df,p2_df,p13_df =                                                                                                                      load_from_local_separadas_c1()
    p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df = load_from_local_separadas_c2()
    p28_df =                                                                                                                                  load_from_local_separadas_c3()
    p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df =                                                                          load_from_local_separadas_c4()

def load_from_remote():
    print('Loading from remote:')
    global entidades,misvis,preguntas_df
    global respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df
    global p1_df,p2_df,p13_df
    global p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df
    global p28_df
    global p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df

    entidades,misvis,preguntas_df =                                                                                                           load_from_remote_basic()
    respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df =                       load_from_remote_respuestas_resultados()
    p1_df,p2_df,p13_df =                                                                                                                      load_from_remote_separadas_c1()
    p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df = load_from_remote_separadas_c2()
    p28_df =                                                                                                                                  load_from_remote_separadas_c3()
    p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df =                                                                          load_from_remote_separadas_c4()

try:
    load_from_local()
except Exception as e:
    print(e)
    load_from_remote()

###############################################################################################################################################################################################################
# Guardar como excel
###############################################################################################################################################################################################################

def overwrite_excels_basic(entidades,misvis,preguntas_df):
    entidades.to_excel(f"./files{UBI_AR['entidades']}")
    misvis.to_excel(f"./files{UBI_AR['misvis']}")
    preguntas_df.to_excel(f"./files{UBI_AR['preguntas']}")
    print('Files in basic have been overwritten with remote')

def overwrite_excels_respuestas_resultados(respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df):
    respuestas_2019_df.to_excel(f"./files{UBI_AR['respuestas_2019']}")
    respuestas_2021_df.to_excel(f"./files{UBI_AR['respuestas_2021']}")
    respuestas_2023_df.to_excel(f"./files{UBI_AR['respuestas_2023']}")

    resultados_2019_df.to_excel(f"./files{UBI_AR['resultados_2019']}")
    resultados_2021_df.to_excel(f"./files{UBI_AR['resultados_2021']}")
    resultados_2023_df.to_excel(f"./files{UBI_AR['resultados_2023']}")
    print('Files in respuestas/resultados have been overwritten with remote')

def overwrite_excels_separadas_c1(p1_df,p2_df,p13_df):
    p1_df.to_excel(f"./files/{UBI_AR['p1']}")
    p2_df.to_excel(f"./files/{UBI_AR['p2']}")
    p13_df.to_excel(f"./files/{UBI_AR['p13']}")
    print('Files in c1 have been overwritten with remote')

def overwrite_excels_separadas_c2(p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df):
    p14_df.to_excel(f"./files/{UBI_AR['p14']}")
    p15_df.to_excel(f"./files/{UBI_AR['p15']}")
    p16_df.to_excel(f"./files/{UBI_AR['p16']}")
    p17_df.to_excel(f"./files/{UBI_AR['p17']}")
    p18_df.to_excel(f"./files/{UBI_AR['p18']}")
    p19_df.to_excel(f"./files/{UBI_AR['p19']}")
    p20_df.to_excel(f"./files/{UBI_AR['p20']}")
    p21_df.to_excel(f"./files/{UBI_AR['p21']}")
    p22_df.to_excel(f"./files/{UBI_AR['p22']}")
    p23_df.to_excel(f"./files/{UBI_AR['p23']}")
    p24_1_df.to_excel(f"./files/{UBI_AR['p24_1']}")
    p24_2_df.to_excel(f"./files/{UBI_AR['p24_2']}")
    p24_3_df.to_excel(f"./files/{UBI_AR['p24_3']}")
    p24_4_df.to_excel(f"./files/{UBI_AR['p24_4']}")
    p24_5_df.to_excel(f"./files/{UBI_AR['p24_5']}")
    p25_df.to_excel(f"./files/{UBI_AR['p25']}")
    p26_df.to_excel(f"./files/{UBI_AR['p26']}")
    p27_df.to_excel(f"./files/{UBI_AR['p27']}")
    print('Files in c2 have been overwritten with remote')

def overwrite_excels_separadas_c3(p28_df):
    p28_df.to_excel(f"./files/{UBI_AR['p28']}")
    print('Files in c3 have been overwritten with remote')

def overwrite_excels_separadas_c4(p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df):
    p31_df.to_excel(f"./files/{UBI_AR['p31']}")
    p32_df.to_excel(f"./files/{UBI_AR['p32']}")
    p33_df.to_excel(f"./files/{UBI_AR['p33']}")
    p34_df.to_excel(f"./files/{UBI_AR['p34']}")
    p35_df.to_excel(f"./files/{UBI_AR['p35']}")
    p36_df.to_excel(f"./files/{UBI_AR['p36']}")
    p37_df.to_excel(f"./files/{UBI_AR['p37']}")
    p38_df.to_excel(f"./files/{UBI_AR['p38']}")
    p39_df.to_excel(f"./files/{UBI_AR['p39']}")
    print('Files in c4 have been overwritten with remote')

def overwrite_excels():
    overwrite_excels_basic(entidades,misvis,preguntas_df)
    overwrite_excels_respuestas_resultados(respuestas_2019_df,respuestas_2021_df,respuestas_2023_df,resultados_2019_df,resultados_2021_df,resultados_2023_df)
    overwrite_excels_separadas_c1(p1_df,p2_df,p13_df)
    overwrite_excels_separadas_c2(p14_df,p15_df,p16_df,p17_df,p18_df,p19_df,p20_df,p21_df,p22_df,p23_df,p24_1_df,p24_2_df,p24_3_df,p24_4_df,p24_5_df,p25_df,p26_df,p27_df)
    overwrite_excels_separadas_c3(p28_df)
    overwrite_excels_separadas_c4(p31_df,p32_df,p33_df,p34_df,p35_df,p36_df,p37_df,p38_df,p39_df)

###############################################################################################################################################################################################################
# Definir criterios
###############################################################################################################################################################################################################

CRITS_PREGUNTAS_BASE={
    'p1':{},
    'p2':{'c1':0,'c2':0,'c3':0},
    'p3':{},
    'p4':{'c1':0,'c2':0},
    'p5':{},
    'p6':{'c1':0,'c2':0},
    'p7':{},
    'p8':{'c1':0,'c2':0},
    'p9':{},
    'p10':{},
    'p11':{'c1':0,'c2':0},
    'p12':{},
    'p13':{'c1':0,'c2':0},
    'p14':{'c1':0,'c2':0},
    'p15':{'c1':0,'c2':0},
    'p16':{'c1':0,'c2':0},
    'p17':{'c1':0,'c2':0},
    'p18':{'c1':0,'c2':0},
    'p19':{'c1':0,'c2':0},
    'p20':{'c1':0,'c2':0},
    'p21':{'c1':0,'c2':0},
    'p22':{'c1':0,'c2':0},
    'p23':{'c1':['c1'],'c2':['c2'],'c3':['c3'],'c4':['c4']},
    'p24':{'c1':0,'c2':0,'c3':0,'c4':0},
    'p25':{'c1':0,'c2':0},
    'p26':{'c1':0,'c2':0},
    'p27':{'c1':0},
    'p28':{'c1':0,'c2':0,'c3':0,'c4':['c4'],'c5':['c5']},
    'p29':{'c1':0},
    'p30':{'c1':0},
    'p31':{},
    'p32':{'c1':0,'c2':0},
    'p33':{'c1':0,'c2':0},
    'p34':{'c1':0,'c2':0},
    'p35':{'c1':0,'c2':0},
    'p36':{'c1':0,'c2':0},
    'p37':{'c1':0,'c2':0},
    'p38':{'c1':0,'c2':0},
    'p39':{'c1':0,'c2':0},
    }

def normalizador_notas(nota_normalizada_maxima,nota_obtenida,nota_maxima):
    return (nota_obtenida / nota_maxima) * nota_normalizada_maxima
