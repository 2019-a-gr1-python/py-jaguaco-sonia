# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 08:23:52 2019

@author: DELL
"""

# -*- coding: utf-8 -*-
import sys
import unicodedata

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from scipy.misc import imread


if len(sys.argv) < 3:
   
    sys.exit()

tuit_file = sys.argv[1].strip()
mask_file = sys.argv[2].strip()

twitter_mask = imread(mask_file, flatten=True)

STOPWORDS = STOPWORDS.union(set([
    "a", "actualmente", "adelante", "además", "afirmó", "agregó", "ahí", "ahora",
    "cc", "this", "pa", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "al",
    "algo", "algún", "algún", "alguna", "algunas", "alguno", "algunos",
    "alrededor", "ambos", "ampleamos", "añadió", "ante", "anterior", "antes",
    "apenas", "aproximadamente", "aquel", "aquellas", "aquellos", "aqui",
    "aquí", "arriba", "aseguró", "así", "atras", "aún", "aunque", "ayer",
    "bajo", "bastante", "bien", "buen", "buena", "buenas", "bueno", "buenos",
    "cada", "casi", "cerca", "cierta", "ciertas", "cierto", "ciertos", "cinco",
    "comentó", "como", "cómo", "con", "conocer", "conseguimos", "conseguir",
    "considera", "consideró", "consigo", "consigue", "consiguen", "consigues",
    "contra", "cosas", "creo", "cual", "cuales", "cualquier", "cuando",
    "cuanto", "cuatro", "cuenta", "da", "dado", "dan", "dar", "de", "debe",
    "deben", "debido", "decir", "dejó", "del", "demás", "dentro", "desde",
    "después", "dice", "dicen", "dicho", "dieron", "diferente", "diferentes",
    "dijeron", "dijo", "dio", "donde", "dos", "durante", "e", "ejemplo", "el",
    "de", "la", "el", "porfas", "t", "p", "d", "est",
    "él", "ella", "ellas", "ello", "ellos", "embargo", "empleais", "emplean",
    "emplear", "empleas", "empleo", "en", "encima", "encuentra", "entonces",
    "entre", "era", "eramos", "eran", "eras", "eres", "es", "esa", "esas",
    "ese", "eso", "esos", "esta", "ésta", "está", "estaba", "estaban",
    "estado", "estais", "estamos", "estan", "están", "estar", "estará",
    "estas", "éstas", "este", "éste", "esto", "estos", "éstos", "estoy",
    "estuvo", "ex", "existe", "existen", "explicó", "expresó", "fin", "fue",
    "fuera", "fueron", "fui", "fuimos", "gran", "grandes", "gueno", "ha",
    "haber", "había", "habían", "habrá", "hace", "haceis", "hacemos", "hacen",
    "hacer", "hacerlo", "haces", "hacia", "haciendo", "hago", "han", "hasta",
    "hay", "haya", "he", "hecho", "hemos", "hicieron", "hizo", "hoy", "hubo",
    "igual", "incluso", "indicó", "informó", "intenta", "intentais",
    "intentamos", "intentan", "intentar", "intentas", "intento", "ir", "junto",
    "la", "lado", "largo", "las", "le", "les", "llegó", "lleva", "llevar",
    "lo", "los", "luego", "lugar", "manera", "manifestó", "más", "mayor", "me",
    "mediante", "mejor", "mencionó", "menos", "mi", "mientras", "mio", "misma",
    "mismas", "mismo", "mismos", "modo", "momento", "mucha", "muchas", "mucho",
    "muchos", "muy", "nada", "nadie", "ni", "ningún", "ninguna", "ningunas",
    "ninguno", "ningunos", "no", "nos", "nosotras", "nosotros", "nuestra",
    "nuestras", "nuestro", "nuestros", "nueva", "nuevas", "nuevo", "nuevos",
    "nunca", "o", "ocho", "otra", "otras", "otro", "otros", "para", "parece",
    "parte", "partir", "pasada", "pasado", "pero", "pesar", "poca", "pocas",
    "poco", "pocos", "podeis", "podemos", "poder", "podrá", "podrán", "podria",
    "podría", "podriais", "podriamos", "podrian", "podrían", "podrias",
    "poner", "por", "porque", "por qué", "posible", "primer", "primera",
    "primero", "primeros", "principalmente", "propia", "propias", "propio",
    "propios", "próximo", "próximos", "pudo", "pueda", "puede", "pueden",
    "puedo", "pues", "que", "qué", "quedó", "queremos", "quien", "quién",
    "quienes", "quiere", "realizado", "realizar", "realizó", "respecto",
    "sabe", "sabeis", "sabemos", "saben", "saber", "sabes", "se", "sea",
    "sean", "según", "segunda", "segundo", "seis", "señaló", "ser", "será",
    "serán", "sería", "si", "sí", "sido", "siempre", "siendo", "siete",
    "sigue", "siguiente", "sin", "sino", "sobre", "sois", "sola", "solamente",
    "solas", "solo", "sólo", "solos", "somos", "son", "soy", "su", "sus",
    "tal", "también", "tampoco", "tan", "tanto", "tendrá", "tendrán", "teneis",
    "tenemos", "tener", "tenga", "tengo", "tenía", "tenido", "tercera",
    "tiempo", "tiene", "tienen", "toda", "todas", "todavía", "todo", "todos",
    "total", "trabaja", "trabajais", "trabajamos", "trabajan", "trabajar",
    "trabajas", "trabajo", "tras", "trata", "través", "tres", "tuvo", "tuyo",
    "tu", "te", "pq", "mas", "qie", "us", "has", "ti", "ahi", "mis", "tus",
    "do", "X", "Ven", "mo", "Don", "dia", "PT", "sua", "q", "x", "i", 
    "última", "últimas", "ultimo", "último", "últimos", "un", "una", "unas",
    "uno", "unos", "usa", "usais", "usamos", "usan", "usar", "usas", "uso",
    "usted", "va", "vais", "valor", "vamos", "van", "varias", "varios", "vaya",
    "veces", "ver", "verdad", "verdadera", "verdadero", "vez", "vosotras",
    "n", "s", "of", "c", "the", "m", "qu", "to", "as", "is",
    "asi", "via", "sera", "tambien", "vosotros", "voy", "y", "ya", "yo"]))

df = pd.read_csv(tuit_file)
words = ' '.join(df['tweet'])
words = unicode(words, 'UTF-8')
words = unicodedata.normalize('NFKD', words).encode('ascii', 'ignore')

no_urls_no_tags = " ".join([word for word in words.split()
                            if 'http' not in word and not word.startswith('@') and word != 'RT'
                            ])

wordcloud = WordCloud(
    font_path='./RobotoCondensed.ttf',
    stopwords=STOPWORDS,
    background_color='white',
    width=1800,
    height=1400,
    mask=twitter_mask
).generate(no_urls_no_tags)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./wordcloud.png', dpi=300)
plt.show()