# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from scraper.models import Data, db_connect, create_deals_table, JsonData
import json



class TutorialPipeline(object):
        
    def __init__(self):
            """
            Initializes database connection and sessionmaker.
            Creates deals table.
            """
            engine = db_connect()
            create_deals_table(engine)
            self.Session = sessionmaker(bind=engine)
            
            #clear data from table
            try:
                session = self.Session()
                session.query(Data).delete()
                session.commit()
                session.query(JsonData).delete()
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """

        session = self.Session()
        data = Data(**item)
        jsond = JsonData(jsond=json.dumps(dict(item)))
        
        try:
            session.add(data)
            session.commit()
            session.add(jsond)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
