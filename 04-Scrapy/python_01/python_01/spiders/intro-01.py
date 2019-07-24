import scrapy
import numpy as np
class IntroSpider(scrapy.Spider):


     name='introduccion_Spider'

     def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            #yield nos permite hacer sincrona para que se ejecute en secuencia y no en paralelo
            yield scrapy.Request(url=url)
   
     def parse(self, response):

        etiqueta_contenedor=response.css('article.product_pod')
        titulo=response.css('h3> a ::attr(title)').extract()
         
        stoks=titulo = etiqueta_contenedor.css('div.product_price>p.instock.availability::text').extract()
        precios=etiqueta_contenedor.css('div.prodcut_price>p.price_color').extract()
        diccionario=[titulo:'titulo',stoks:'stoks',precios:'precios']
        a= pd.DataFrame(diccionario)
        a.to_excel('example.xlsx', sheet_name='example')        
        print(titulo)
        print(a)
        print(stoks)
        print(precios)

