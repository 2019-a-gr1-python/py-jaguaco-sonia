# -*- coding: utf-8 -*-
"""
Created on Fri May 31 15:41:29 2019

@author: DELL
"""

import pandas as pd
path = 'C:/Users/DELL/Documents/R/test1.1.json'
# read the entire file into a python array
with open(path) as f:
    data = f.readlines()

# remove the trailing "\n" from each line
data = map(lambda x: x.rstrip(), data)

# each element of 'data' is an individual JSON object.
# i want to convert it into an *array* of JSON objects
# which, in and of itself, is one large JSON object
# basically... add square brackets to the beginning
# and end, and have all the individual business JSON objects
# separated by a comma
data_json_str = "[" + ','.join(data) + "]"

# now, load it into pandas
data_df = pd.read_json(data_json_str)