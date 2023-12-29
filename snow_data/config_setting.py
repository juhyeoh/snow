from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table, DateTime
from env import settings

def create_db(engine):
    metadata = MetaData()

    table_set = Table(
        'snowdata_table', metadata,
        Column('pageNo', Integer, primary_key=True),
        Column('stnIds', String(255)),
        Column('date', DateTime),
        Column('ddMefs', Float),
        Column('ddMes', Float),
        Column('stnNm', String(255))
    )
    metadata.create_all(engine)

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