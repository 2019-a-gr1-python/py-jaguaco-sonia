import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu'  # Heredado (conservar nombre)
    
    allowed_domains = [  # Heredado (conservar nombre)
        'un.org'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]
    # Heredado (conservar nombre)

    regla_uno = (
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=('funds-programmes-specialized-agencies-and-others')
            ), callback='parse_page')
        ,
    )

    rules = regla_dos


    def parse_page(self, response):
        lista_programas = response.css('div.field-items > div.field-item > h4::text').extract()

        for agencia in lista_programas:
            with open('onu_agencias.txt', 'a+') as archivo:
                archivo.write(agencia + '\n')