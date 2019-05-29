# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:53:29 2019

@author: DELL
"""

import pandas as pd
import os

# Archivos texto  --- JSON, CSV, HTML, XML.....
# Binary Files --- (asdasdasdasd)
# Relational Databases

path = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/test/artwork_data.csv'

columnas_a_usar = ['id','artist','title',
                   'medium','year','acquisitionYear',
                   'height','width','units']

df = pd.read_csv(
        path,
        nrows=100,
        usecols=columnas_a_usar,
        index_col='id'
        )

df_completo = pd.read_csv(
        path,
        usecols=columnas_a_usar,
        index_col='id'
        )

path_guardado = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/artwork_data.pickle'

df_completo.to_pickle(path_guardado)

df_completo_pickle = pd.read_pickle(path_guardado)

df_completo.shape