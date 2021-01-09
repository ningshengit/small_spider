# -*- coding: utf-8 -*-
# @Date    : 2020-12-09 22:12:43
# @Author  : autohe (${email})
# @知乎    : https://www.zhihu.com/people/kuanye
# @微信    : xdxh-1
# @funtion : 
# @Version : $Id$

from  scrapy import Selector
import os
import time
import re
import jieba

with open('exam.html', 'r', encoding='utf-8') as fp:
    res = fp.read()

select = Selector(text=res)

# title = select.xpath('//title/text()').extract()
# print(title)

# href = select.xpath('//div[@class="article-intro"]/ul/li/a/@href').extract()

# for url in href:
#     print(url)

#title = select.xpath('//div[@class="article-intro"]/p/text()').extract_first()

#print(title)
example_code = select.xpath('//div[@class="example"]//text()').extract()


print(example_code)
with open('ex.py', 'w', encoding='utf-8')as f:
    for ex in example_code:
        ex_ = ex.replace('\xa0', ' ')    
        f.write(ex)