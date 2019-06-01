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


filename='C:/Users/DELL/Documents/R/ec.json'
with open(filename) as f:
    data = json.load(f)
    

pprint(data)
wordcloud = WordCloud().generate(data)
# Generate plot
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
datos_poblacion=pd.DataFrame(data)

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
plt.title('Distribucion poblacion por edad y sexo')
plt.savefig('distripoblacionedadsexo.png',dpi=600)

df3=pd.DataFrame(data,columns=['population_proper','population'])
df3.hist
df3['population_proper']
df3.hist




















