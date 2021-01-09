# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class PythonexamplePipeline(object):

    def __init__(self):
        self.path = os.getcwd()

    def process_item(self, item, spider):
        
        with open(self.path+'/PythonExample/py/'+item['title']+'.py', 'w', encoding='utf-8') as f:
            for ex in item['content']:
                ex_ = ex.replace('\xa0', ' ')    
                f.write(ex_)
        return item
