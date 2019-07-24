# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 02:26:10 2019

@author: DELL
"""

import pandas as pd
import numpy as np
import os
import sqlite3
from openpyxl.styles import Font

path_guardado = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

df = df_completo_pickle.iloc[49980:50019,:].copy()

writer = pd.ExcelWriter('multiples_formatos.xlsx', engine = 'xlsxwriter')

artistas_contados = df_completo_pickle['artist'].value_counts()

###################### DATA BAR ########################################

artistas_contados.to_excel(writer, sheet_name = 'Data Bar')
workbook  = writer.book
hoja_artistas = writer.sheets['Data Bar']
format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '0%'})
hoja_artistas.set_column('B:B', 18, format1)

# Set the format but not the column width.
hoja_artistas.set_column('C:C', None, format2)
rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)
def color_negative_red(value):
  """
  Colors elements in a dateframe
  green if positive and red if
  negative. Does not color NaN
  values.
  """

  if value < 200:
    color = 'red'
  elif value > 200:
    color = 'green'
  else:
    color = 'black'

  return 'color: %s' % color
df.style.applymap(color_negative_red, subset=['year','acquisitionYear'])



formato = {
        'type': 'data_bar',
        'bar_negative_color_same': True,
        'min_value': '10',
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile',
        'bar_color': 'green'
        }
# Light red fill with dark red text.
format1= {
        'type': 'cell',
        'bar_color':   '#FFC7CE',
        }

# Light yellow fill with dark yellow text.
format2 = workbook.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})

# Green fill with dark green text.
format3 = workbook.add_format({'bg_color':   '#C6EFCE',
                               'font_color': '#006100'})


hoja_artistas.conditional_format(rango_celdas, formato)
                               
artistas_contados = df['artist'].value_counts()
#hoja_artistas.conditional_format(rango_celdas, {'type':     'text',
#                                       'criteria': 'containing',
#                                       'value':    'foo',
#                                       'format':   format1})



################### FORMATO incon_set ######################

df.to_excel(writer, sheet_name = 'Icon Set')

hoja_artistas = writer.sheets['Icon Set']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)


formato1 = {
        'type': 'icon_set',
        'icon_style': '5_quarters'
        }


hoja_artistas.conditional_format(rango_celdas, formato1)


df.to_excel(writer, sheet_name = 'Ratings')

writer.save()