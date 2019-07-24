    
import scrapy 
from python_02.items  import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'
     # 1 generar una funcion que gener url
     # 2 anadir el recio (clase inut, outut)
     #3 transformar el recio a numero (float)
     #4 exortar a csv
     # anadir un pipeline para seleccionar los productos mayores al precio promediop
    def start_requests(self):
    
     urls=[    #Heredado conservar nombre de atributo
        'https://www.fybeca.com/FybecaWeb'
      ]
    allowed_domains = [     #Heredado conservar nombre de atributo
        'fybeca.com'
    ]
    url_segmentos_permitidos=(
        'pages/search-results.jsf?cat=238&s=0&pp=25',
        'pages/search-results.jsf?s=25&pp=25&cat=238&b=-1&ot=0',
        'pages/search-results.jsf?s=25&pp=50&cat=238&b=-1&ot=0',
        'pages/search-results.jsf?s=25&pp=75&cat=238&b=-1&ot=0',
        'pages/search-results.jsf?s=25&pp=100&cat=238&b=-1&ot=0',
        'pages/search-results.jsf?s=25&pp=125&cat=238&b=-1&ot=0',
        'pages/search-results.jsf?s=25&pp=150&cat=238&b=-1&ot=0'
    )
        
    rules=(
        Rule(LinkExtractor(
            allow_domains=allowed_domains,
            allow=url_segmentos_permitidos
        ),callback='parse_page'),
    )
   
            
    def parse(self, response):

        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len( producto.css('div.detail'))
            if(existe_producto > 0):
                # titulo = producto.css('a.name::text')
                # url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                
                producto_loader.default_output_processor = TakeFirst()

                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                    )
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )

                #producto_imprimir = producto_loader.load_item()
                #print(producto_imprimir)
                yield producto_loader.load_item()









"""
url = response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
contenedor = response.css('div.product-tile-inner')
titulo = contenedor.css('a.name::text')
def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    print('ASDASDAS') 
    return texto.replace(cadena_a_reemplazar,url)
class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen)
    )
    titulo = scrapy.Field()
from scrapy.loader import ItemLoader
il = ItemLoader(item=ProductoFybecaDos())
il.add_value('imagen',url.extract_first())
il.add_value('titulo', titulo.extract_first())
il.load_item()
"""