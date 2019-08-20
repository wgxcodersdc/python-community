# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseDotGovRep(scrapy.Item):
    """
    Represents a HousseDotGov scraped item
    """
    name = scrapy.Field()
    website = scrapy.Field()
    party = scrapy.Field()
    zip = scrapy.Field()

    # update date in UTC
    scrape_date = scrapy.Field()
