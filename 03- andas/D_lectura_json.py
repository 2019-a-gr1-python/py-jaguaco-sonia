# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:35:06 2019

@author: DELL
"""
import pandas as pd
import json


path = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/artwork'
archivo = '/a/000/a00001-1035.json'
path_archivo=path archivo
llaves= [[]
with oen(path_archivo) as texto_json:
    contenido_json=json.load(texto_json)
    print(type(contenido_json))
    print(contenido_json)
