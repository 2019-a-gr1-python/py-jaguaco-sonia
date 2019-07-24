# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:51:49 2019

@author: DELL
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

df = df_completo_pickle.iloc[49980:50019,:].copy()
######################### Excel ###########################
df.to_excel('ejemplo_basico.xlsx')

#Quitar los indices

df.to_excel('ejemplo_basico_sin_indices.xlsx', index=False)

#Trear columnas especificas 
columnas = ['artist','title','year']

df.to_excel('columnas.xlsx', columns = columnas)


# Multiples hojas de trabajo (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')
df.to_excel(writer, sheet_name = 'Preview Dos', index = False)
df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()


# Formateo Condicional

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

#Cuantos artistas existen 
rango_celdas = 'B2:B{}'.format(len(artistas_contados.index)+1) #Para que se escogan todas las filas

formato = {
        'type': '2_color_scale',
        'min_value': '10',
        'min_type': 'percentile',
        'min_value': '99',
        'max_type': 'percentile'
        }

hoja_artistas.conditional_format(rango_celdas,formato)

writer.save()


######################### SQL ##################################


    
## with mysql.connect('mysql://user:password@ip:puerto/bd') as conexion
##    df.to_sql('Tabla', conexion)

######################### JSON #################################

df.to_json('artist.json')

df.to_json('artist_ordientados_tabla.json', orient='table')



################## Ejercicios ############################




artistas_contados = df_completo_pickle['artist'].value_counts()


artistas_contados2 = artistas_contados.iloc[1::]




writer = pd.ExcelWriter('colores3.xlsx', engine = 'xlsxwriter')


artistas_contados2.to_excel(writer, sheet_name = 'Ejemplo1')

hoja_ejemplo1= writer.sheets['Ejemplo1']


formato1 ={
        'type': 'icon_set',
        'icon_style': '5_ratings',
        'icons': [{'criteria': '>=', 'type': 'number',     'value': '100'},
                  {'criteria': '<',  'type': 'percentile', 'value': '50'},
                  {'criteria': '<=', 'type': 'percent',    'value': '10'}]
        }
hoja_ejemplo1.conditional_format(rango_celdas,formato1)

writer.save()



writer = pd.ExcelWriter('colores2.xlsx', engine = 'xlsxwriter')
artistas_contados2.to_excel(writer, sheet_name = 'Ejemplo2')
hoja_ejemplo2= writer.sheets['Ejemplo2']


formato2 ={
        'type': 'data_bar',
        'bar_color': '#668cff'
        }
    
hoja_ejemplo2.conditional_format(rango_celdas,formato2)

writer.save()






writer = pd.ExcelWriter('colores4.xlsx', engine = 'xlsxwriter')
artistas_contados2.to_excel(writer, sheet_name = 'Ejemplo4')
hoja_ejemplo2= writer.sheets['Ejemplo4']


formato2 ={
        'type': '3_color_scale',
        'min_color': "#C5D9F1",
        'mid_color': "#8DB4E3",
        'max_color': "#538ED5"}
    
hoja_ejemplo2.conditional_format(rango_celdas,formato2)

writer.save()







writer = pd.ExcelWriter('colores5.xlsx', engine = 'xlsxwriter')
artistas_contados.to_excel(writer, sheet_name = 'Ejemplo5')
hoja_ejemplo2= writer.sheets['Ejemplo5']


formato5 ={'type': 'icon_set',
           'icon_style': '3_traffic_lights',
           }
    
hoja_ejemplo2.conditional_format(rango_celdas,formato5)

writer.save()