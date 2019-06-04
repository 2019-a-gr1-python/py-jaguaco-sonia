# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:35:47 2019

@author: DELL
"""

import json
import pandas as pd
from pprint import pprint
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from seaborn import lmplot
from seaborn import kdeplot
from seaborn import distplot
filename='C:/Users/DELL/Documents/R/ter3/IMDB-Movie-Data.csv'

with open(filename) as f:
    datos=pd.read_csv(filename)
data = pd.DataFrame(columns=('Genre', 'Votes', 'Rating', 'Year','Metascore','Revenue (Millions),'))
df=pd.DataFrame(datos)  



plt.title('Ranting MAximo de movies x Genero')
df.groupby('Rating')['Votes'].max().plot(kind='pie',legend='Reverse')

