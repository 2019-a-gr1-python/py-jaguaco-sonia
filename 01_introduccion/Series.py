# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd
lista_numeros=[1,2,3,4,5]
tupla_numeros=[1,2,3,4,5]
np_numeros=np.array((1,2,3,4,5))
numeros_series_a=pd.Series(lista_numeros)
numeros_series_b=pd.Series(tupla_numeros)
numeros_series_c=pd.Series(np_numeros)
numeros_series_d=pd.Series([1,2,3,4,5,6])
numeros_series_a[0]
lista_ciudades=["Ambato","Quito","Cuenca"]
serie_ciudades=pd.Series(lista_ciudades,index=["x","b","c"])
serie_ciudades["x"]
serie_ciudades[0]
serie_ciudades[1]
serie_ciudades[2]

print(type(serie_ciudades))
valores_ciudades={"Ibarra":9500,
                  "Guayaquil":10000,
                  "Cuenca":7000}
series.valor_ciudad =pd.Series(valores_ciudades)
serie_valor_ciudad["Ibarra"]
serie_valor_ciudad[0]
como concatenar series
como agregar algun indice y algun valor en 
ciudades_uno=pd.Series({"Montanita" :400})
ciudades_dos=pd.Series({"Uayaquil" :500,
                        "Quito" :600,
                        "Loja" :700
                        })
print(ciudades_uno ciudades_dos)
ciudades_uno.append(ciudades_dos)
ciudades_uno.append(ciudades_dos,ignore_index=True )
ciudades_uno.append(ciudades_dos,verify_integrity=True)
ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno = ciudades_uno.DataReader("ciudades_uno", 'yahoo', '2016-1-1', '2016-9-30')
ciudades_uno.head(2)
ciudades_uno.between(100,400)
def calculo(valor)
 if(valor<=100 ): return valor*1.5
ciudades_uno.map(calculo) 
 
