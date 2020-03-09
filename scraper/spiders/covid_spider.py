
import scrapy
from scraper.items import CountryTest, TotalData
from scrapy.spiders import Spider
from scrapy.selector import Selector
import re 
import json



class CovidSpider(Spider):

    name = "covid"
    start_urls = [ 'https://www.worldometers.info/coronavirus/' ]

  
    def parse(self, response):
        date = response.xpath("//div[contains(text(), 'Last update')]/text()").getall()
        total_numbers = response.xpath("//div[@class='maincounter-number']/span/text()").getall()
        totals = TotalData()
        totals['total_covid_cases'] = total_numbers[0]
        totals['total_covid_deaths'] = total_numbers[1]
        totals['total_covid_recovered'] = total_numbers[2]
        #yield totals
        tbody = response.css('tbody') #get the table row
        country_rows = tbody.css('tr') #get the table row
        for country in country_rows: 
            c = country.css('td::text').getall() # dump the row text into a list
            
            # parse data and add it to CountryTest
            data = CountryTest()
            data['name'] = c[0].strip()
            data['total_cases'] = int(''.join(re.findall("[0-9]", c[1]))) if c[1].strip() else 0
            data['new_cases'] = int(''.join(re.findall("[0-9]", c[2]))) if c[2].strip() else 0
            data['total_deaths'] = int(''.join(re.findall("[0-9]", c[3]))) if c[3].strip() else 0
            data['new_deaths'] = int(''.join(re.findall("[0-9]", c[4]))) if c[4].strip() else 0
            data['active_cases'] = int(''.join(re.findall("[0-9]", c[5]))) if c[5].strip() else 0
            data['total_recovered'] = int(''.join(re.findall("[0-9]", c[6]))) if c[6].strip() else 0
            data['condition'] = int(''.join(re.findall("[0-9]", c[7]))) if c[7].strip() else 0
            data['percentage_changed_cases'] = (data['new_cases'] / (data['total_cases'] - data['new_cases'])) * 100 if data['total_cases'] != data['new_cases'] else 0
            data['percentage_changed_deaths'] = (data['new_deaths'] / (data['total_deaths'] - data['new_deaths'])) * 100 if data['total_deaths'] != data['new_deaths'] else 0
            data['date_updated'] = ''.join(date)
            yield data
