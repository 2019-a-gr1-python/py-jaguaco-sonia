# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:23:27 2019

@author: DELL
"""

import pandas as pd

import numpy as np

import math
path_guardado = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)
seccion_df=df.iloc[49980: 5009,: ].copy()
df_agruado_ay=seccion_df.groupby('acquisitionYear')
type(df_agruado_ay)
for acquisitionYear, registros in df_agruado_ay:
    print(acquisitionYear)
    print(registros)