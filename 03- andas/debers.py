


import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

filename='C:/Users/DELL/Documents/R/ter3/IMDB-Movie-Data.csv'
with open(filename) as f:
    datos=pd.read_csv(filename)
columnas_a_usar=['Rank','Genre','Director','Actors','Year','Runtime','Rating','Votes','Millions','Metascore']
df_completo = pd.read_csv(
        filename,usecols=columnas_a_usar
        )

#data = pd.DataFrame(columns=('Genre', 'Votes', 'Rating', 'Year','Metascore','Revenue (Millions),'))
df=pd.DataFrame(datos)  

#plt.title('Ranting MAximo de movies x Rating')
#df.groupby('Year')['Votes'].max().plot(kind='pie',legend='Reverse')

#plt.title('Ranting MAximo de movies x Genero')
#df.groupby('Rating')['Votes'].max().plot(kind='pie',legend='Reverse')

#plt.title('Ranting MAximo de Votos x Comentsrio')
#df.groupby('Metascore')['Votes'].sum().plot(kind='pie',legend='Reverse')





