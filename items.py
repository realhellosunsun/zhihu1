# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    answer_count=Field()
    articles_count = Field()
    follower_count =Field()
    following_count = Field()
    gender = Field()
    name= Field()
    question_count = Field()
    url_token = Field()



