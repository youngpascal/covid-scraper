import os

BOT_NAME = 'covid'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False



'''
DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'myPassword',
    'database': 'scrape'
}'''

ITEM_PIPELINES = {'scraper.pipelines.TutorialPipeline': 300}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


