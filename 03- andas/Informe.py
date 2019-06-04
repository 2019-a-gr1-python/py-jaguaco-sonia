# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:07:26 2019

@author: DELL
"""


import pandas as pd
import numpy as np
import math
import urllib.parse
import urllib.request
import json
import os
import tarfile
from pprint import pprint

path = 'C:/Users/DELL/Documents/R/trabajo.json'




with open(path) as texto_json:
    contenido_json=json.load(texto_json)
pprint(contenido_json)

    