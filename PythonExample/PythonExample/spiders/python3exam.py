# -*- coding: utf-8 -*-
import scrapy
import re
from PythonExample.items import PythonexampleItem


class Python3examSpider(scrapy.Spider):
    name = 'python3exam'
    allowed_domains = ['www.runoob.com']
    start_urls = ['https://www.runoob.com/python3/python3-examples.html']


    def match(self, url):

        result = re.match('^/p', url)
        if result:
            url_ = 'https://www.runoob.com' + url
            return url_
        else:
            url_ = 'https://www.runoob.com/python3/' + url
            return url_
        if 'www.runoob.com' in url:
            url_ = 'https:' + url
            return url_


    def parse(self, response):
        href = response.xpath('//div[@class="article-intro"]/ul/li/a/@href').extract()
        if href:
            for url in href:
                url_ = self.match(url)
                yield scrapy.Request(url=url_, callback=self.detial, dont_filter=True)
 
    def detial(self, response):
        if response.status == 200:
            title = response.xpath('//div[@class="article-intro"]/h1/text()').extract_first()
            example_code = response.xpath('//div[@class="example"]//text()').extract()
            item = PythonexampleItem(title=title,
                                    content=example_code)
            yield item
