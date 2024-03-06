from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date
from env import settings
from sqlalchemy.orm import declarative_base
import logging

Base = declarative_base()

class SnowApiData(Base):
    __tablename__ = 'snowdata_collector'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    stnIds = Column(String(255))
    stnNm = Column(String(12))
    date = Column(Date)
    ddMes = Column(Float)
    ddMefs = Column(Float)

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
    engine = create_engine(
        f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}",
        echo=True
    )
    return engine

engine = create_db_engine()
create_db(engine)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
