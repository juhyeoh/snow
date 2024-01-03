from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from env import settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SnowApiData(Base):
    __tablename__ = 'snowdata_table'

    pageNo = Column(Integer, primary_key=True)
    date = Column(DateTime)
    stnIds = Column(String(255))
    ddMefs = Column(Float)
    ddMes = Column(Float)

def create_db(engine):
    Base.metadata.create_all(engine)

def config_info():
    return {
        'host': settings.DATABASE_CONFIG['host'],
        'database': settings.DATABASE_CONFIG['database'],
        'user': settings.DATABASE_CONFIG['user'],
        'password': settings.DATABASE_CONFIG['password'],
        'port': settings.DATABASE_CONFIG['port'],
        'serviceKey': settings.DATABASE_CONFIG['serviceKey'],
        'api_end': settings.DATABASE_CONFIG['api_end'],
    }

def create_db_engine():
    config = config_info()
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(config['user'], config['password'], config['host'], config['port'], config['database']), echo=True)
    return engine