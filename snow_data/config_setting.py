import logging
import os

from dotenv import load_dotenv
from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

load_dotenv()
Base = declarative_base()


class SnowApiData(Base):
    __tablename__ = "snowdata_collector"

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
        "host": os.environ.get("DB_HOST"),
        "database": os.environ.get("DB_NAME"),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "port": os.environ.get("DB_PORT"),
        "serviceKey": os.environ.get("service_key"),
        "api_end": os.environ.get("api_url"),
    }


def create_db_engine():
    config = config_info()
    engine = create_engine(
        f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}",
        echo=True,
    )
    return engine


engine = create_db_engine()
create_db(engine)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
