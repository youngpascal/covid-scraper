import scrapy
from scrapy.crawler import CrawlerProcess
from scraper.spiders.covid_spider import CovidSpider
from scrapy.utils.project import get_project_settings

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(CovidSpider)
    process.start()

