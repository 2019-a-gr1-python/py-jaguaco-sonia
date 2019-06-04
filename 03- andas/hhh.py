# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:07:10 2019

@author: DELL
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

filename='C:/Users/DELL/Documents/R/ter3/IMDB-Movie-Data.csv'
with open(filename) as f:
    datos=pd.read_csv(filename)
columnas_a_usar=['Rank','Genre','Director','Actors','Year','Runtime','Rating','Votes','Millions','Metascore']
df_completo = pd.read_csv(
        filename,usecols=columnas_a_usar
        )

#data = pd.DataFrame(columns=('Genre', 'Votes', 'Rating', 'Year','Metascore','Revenue (Millions),'))
df=pd.DataFrame(datos) 