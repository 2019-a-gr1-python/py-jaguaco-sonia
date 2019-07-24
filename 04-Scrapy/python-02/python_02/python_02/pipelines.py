# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
'''Python02Pipeline'''
class FiltrarSoloTabletas(object):
    def process_item(self, item, spider):
     titulo = item['titulo']
     print(titulo)
     if('capsula' not in titulo):
         raise DropItem('No tiene capsula en el titulo')
     else:
            return item
class TituloMinusculas(object):
    def process_item(self, item, spider):
        print(item['titulo'])
        item['titulo'] = item['titulo'].lower()
        return item
from scrapy.exceptions import DropItem

class FiltrarMayoresPromedio(object):
    def process_item(self,item,spider):
        mean = 12.339
        if(item['precio']>mean):
            return item
        else:
            raise DropItem('No es mayor al promedio')