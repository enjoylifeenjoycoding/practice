# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MailsItem(scrapy.Item):
    mail_id = scrapy.Field()
    mail_from = scrapy.Field()
    mail_to = scrapy.Field()
    mail_subject = scrapy.Field()
    mail_sentDate = scrapy.Field()
    mail_receivedDate = scrapy.Field()
    mail_priority = scrapy.Field()
    mail_backgroundColor = scrapy.Field()
