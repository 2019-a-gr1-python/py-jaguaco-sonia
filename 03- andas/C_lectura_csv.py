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

path = 'C:/Users/DELL/Documents/GitHub/py-jaguaco-sonia/03- andas/data/csv/artwork_data.csv'

df = pd.read_csv(
        path,
        nrows=100,
        usecols=['id','artist'],
        index_col='id'
        )