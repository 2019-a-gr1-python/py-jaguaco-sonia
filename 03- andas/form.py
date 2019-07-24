# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:14:17 2019

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

df.to_excel('ejemplo_basico_sin_indices.xlsx', index=False)

columnas = ['artist','title','year']

df.to_excel('columnas.xlsx', columns = columnas)


# Multiples hojas de trabajos (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')

df.to_excel(writer, sheet_name = 'Preview Dos', index = False)

df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()
workbook  = writer.book
worksheet = writer.sheets['Preview']
# Light red fill with dark red text.
format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

# Light yellow fill with dark yellow text.
format2 = workbook.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})

# Green fill with dark green text.
format3 = workbook.add_format({'bg_color':   '#C6EFCE',
                               'font_color': '#006100'})
                

worksheet.conditional_format('A1:C1',
                             {'type': 'icon_set',
                              'icon_style': '3_flags',
                              'icons_only': True})


worksheet.conditional_format('E2:H2', {'type':     'cell',
                                    'criteria': 'between',
                                    'minimum':  100,
                                    'maximum':  200,
                                    'format':   format1,
                                    })
worksheet.conditional_format('B2:B40', {'type':     'text',
                                       'criteria': 'containing',
                                       'value':    'Wols',
                                       'format':   format1})



writer.save()