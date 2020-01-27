# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    rating = scrapy.Field()
    
    total_reviews = scrapy.Field()
    walking_grade = scrapy.Field()
    restaurant = scrapy.Field()
    attraction = scrapy.Field()
    page_link = scrapy.Field()
    amenities = scrapy.Field()
    address = scrapy.Field()
    #display_price = scrapy.Field()

    num_excellent = scrapy.Field()
    num_good = scrapy.Field()
    num_avg = scrapy.Field()
    num_poor = scrapy.Field()
    num_bad = scrapy.Field()

