# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo


class BciProjectPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017 )
        db = self.client['bci_data']
        self.collection = db['articles']


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
