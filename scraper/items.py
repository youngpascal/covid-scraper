# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryTest(scrapy.Item):
    name = scrapy.Field()
    total_cases = scrapy.Field()
    new_cases = scrapy.Field()
    total_deaths = scrapy.Field()
    new_deaths = scrapy.Field()
    active_cases = scrapy.Field()
    total_recovered = scrapy.Field()
    condition = scrapy.Field()
    percentage_changed_cases = scrapy.Field()
    percentage_changed_deaths = scrapy.Field()
    date_updated = scrapy.Field()

class TotalData(scrapy.Item):
    total_covid_cases = scrapy.Field()
    total_covid_deaths = scrapy.Field()
    total_covid_recovered = scrapy.Field()