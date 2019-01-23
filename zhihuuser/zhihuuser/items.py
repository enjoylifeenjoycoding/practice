# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    name = scrapy.Field()
    profession = scrapy.Field()
    img_head_url = scrapy.Field()
    attention = scrapy.Field()