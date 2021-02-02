# -*- coding: utf-8 -*-
import scrapy
from bci_project.items import BciProjectItem
from scrapy.http import Request




class TaylorandfrancisSpider(scrapy.Spider):
    name = 'taylorandfrancis'
    allowed_domains = ['tandfonline.com']
    start_urls = ['https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1263916',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.944469',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.979727',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2013.869003',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1100366',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1307625',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1169723',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1193458',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.979728',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1338010',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1530010',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1252621',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1303253',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1552357',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1493073',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1060819',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1138056',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1246328',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1203629',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1330611',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1252143',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1104613',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1275488',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.912885',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.954183',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1100048',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1132080',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1297192',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1254403',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2013.877210',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1338008',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1440781',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2019.1614770',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1101922',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1149360',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1213603',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1207127',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1063363',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1292721',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1080961',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2019.1571356',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2019.1568821',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1100038',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1103155',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1415496',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1433776',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1103591',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1504662',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1207494',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.912884',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1266725',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1505191',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2018.1550710',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1338013',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.996066',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1114978',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1207497',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1207496',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2014.912881',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1100037',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1134958',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1210989',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1100514',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1304020',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1253524',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1338011',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2015.1101656',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1338012',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2013.867652',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1381829',
    'https://www.tandfonline.com/doi/full/10.1080/2326263X.2016.1207495',
    'https://www.tandfonline.com/doi/full/10.1080/21688370.2016.1142493']




    def parse(self, response):

        title = response.xpath('//meta[@name="dc.Title"]/@content').extract_first()
        abstract = response.xpath('//div[@class="abstractSection abstractInFull"]/p/text()').extract_first()
        authors = response.xpath('//meta[@name="dc.Creator"]/@content').extract()
        publisher = response.xpath('//meta[@name="dc.Publisher"]/@content').extract_first()
        journal = response.xpath('//meta[@name="citation_journal_title"]/@content').extract_first()
        datepublished = response.xpath('//meta[@name="dc.Date"]/@content').extract_first()
        source_link = response.xpath('//meta[@name="dc.Source"]/@content').extract_first()
        checkopenaccess = response.xpath('//a[@class="grant-access"]')


        if checkopenaccess == []:
            isopenaccess = True
        else:
            isopenaccess = False

        load_item = BciProjectItem()

        load_item['title'] = title
        load_item['abstract'] = abstract
        load_item['authors'] = authors
        load_item['publisher'] = publisher
        load_item['journal'] = journal
        load_item['datepublished'] = datepublished
        load_item['source_link'] = source_link
        load_item['isopenaccess'] = isopenaccess
        yield load_item
