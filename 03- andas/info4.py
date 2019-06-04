# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:46:28 2019

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




filename='C:/Users/DELL/Documents/R/ter1/ec.json'
with open(filename) as f:
    data =pd.read_json(f)
    

pprint(data)

datos_poblacion=pd.DataFrame(data)
datos_poblacion.head()
pprint(datos_poblacion)
spliteador_edad = lambda x: x.split('.')[1].split()[0]
spliteador_genero=lambda x: x.split('.')[2].strip()
spliteador_edad_genero=lambda x: [x.split('.')[1].split()[0],x.split('.')[2].strip()]
panda_h=pd.DataFrame(data,columns=['population_proper','admin'])
panda_m=pd.DataFrame(data,columns=['population_proper','city'])


panda_poblacion=pd.merge(panda_h,panda_m,on='population_proper')
plt.plot(panda_poblacion['population_proper'],panda_poblacion['admin'],
         panda_poblacion['population_proper'],panda_poblacion['city'])
plt.xlim([0,105])
plt.locator_params(axis='x',nbins=25)
plt.locator_params(axis='y',nbins=10)
plt.xlabel('population_proper',size=16)
plt.ylabel('Poblacion',size=16)
plt.grid()
plt.legend(['admin','city'])
plt.title('Distribucion de population  proper y la oblacion total')
plt.savefig('distripoblacionedadsexo.png',dpi=600)

df3=pd.DataFrame(data,columns=['population_proper','population'])
df3.hist
df3['population_proper']
df3.hist

datos_poblacion.groupby('city')['population']
datos_poblacion.head

plt.title('Distribucion poblacion total por ciudades')

lmplot('population_proper', 'population', data=datos_poblacion, fit_reg=False)

plt.title('Distribucion poblacion ')
distplot(datos_poblacion.population_proper, rug=True, hist=False)

data.groupby('admin')['population_proper'].sum().plot(kind='barh',legend='Reverse')
plt.xlabel('Suma Rating ')
plt.ylabel('Genero de  Movies ')

filename2='C:/Users/DELL/Documents/R/ter/IMDB-Movie-Data.csv'

datos=pd.read_csv(filename2)
df=pd.DataFrame(datos)
plt.title('Ranting MAximo de movies x Genero')
df.groupby('Genre')['Rating'].sum().plot(kind='barh',legend='Reverse')
plt.xlabel('Suma Rating ')
plt.ylabel('Genero de  Movies ')
lista1=df.columns('Rating').max()
plt.title('Votos')
plt.plot(lista1) 
plt.xlabel('Suma Rating ')
plt.ylabel('Genero de  Movies ')




