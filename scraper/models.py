from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import scraper.settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**scraper.settings.DATABASE))

def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Data(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    total_cases = Column('total_cases', Integer, nullable=True)
    new_cases = Column('new_cases', Integer, nullable=True)
    total_deaths = Column('total_deaths', Integer, nullable=True)
    new_deaths = Column('new_deaths', Integer, nullable=True)
    active_cases = Column('active_cases', Integer, nullable=True)
    total_recovered = Column('total_recovered', Integer)
    condition = Column('condition', Integer, nullable=True)
    percentage_changed_cases = Column('percentage_changed_cases', Integer, nullable=True)
    percentage_changed_deaths = Column('percentage_changed_deaths', Integer, nullable=True)
    date_updated = Column('date_updated', String, nullable=True)

class JsonData(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "json_data"

    id = Column(Integer, primary_key=True)
    jsond = Column('json_data', JSON, nullable=True)