# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:35:06 2019

@author: DELL
"""
import pandas as pd
import json




path = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/artwork/a/000/a00001-1035.json'
pd.read_json



llaves=['id','all_artists','medium','dateText','acquisitionYear','height','width','units']

with open(path) as texto_json:
    contenido_json=json.load(texto_json)
    print(contenido_json)
    registro_df=[]
    for key in llaves:
        valor=contenido_json[key]
        registro_df.append(valor)

serie=tuple(registro_df)
    
df_small=pd.DataFrame(
        [registro_df]
        )

df_small_2=pd.DataFrame(
        [serie]
        )


def leer_json(path,llaves):
    with open(path) as texto_json:
        contenido_json=json.load(texto_json)
    registro_df_lista=[]
    for key in llaves:
        valor=contenido_json[key]
        registro_df.append(valor)
    return registro_df_lista

