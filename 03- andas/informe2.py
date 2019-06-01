# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:03:28 2019

@author: DELL
"""

import json

filename='C:/Users/DELL/Documents/R/test1.1.json'

data = ['name']
with open(filename) as json_file:  
    data_str = json_file.read()
    data_str = data_str.split('[',1)[-1]
    data_str = data_str.rsplit(']',1)[0]
    data_str = data_str.split('][')

for jsonStr in data_str:
    jsonStr = '[' + jsonStr + ']'

    temp_data = json.loads(jsonStr)
    for each in temp_data:
        data.append(each)
