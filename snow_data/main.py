from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from config_setting import create_db, create_db_engine, config_info
from stnIds_api import data_from_api
from config_setting import SnowApiData, Base

def operation_db(engine, stn_ids):
    create_db(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    today = datetime.now()

    for stn_id in stn_ids.get('stnIds', []):
        for i in range(1, 8):
            date_to_collect = today - timedelta(days=i)
            date_str = date_to_collect.strftime('%Y-%m-%d')

            for item in stn_ids.get('data', []):
                if item.get('stnIds') == stn_id:
                    ddMes_str = item.get('ddMes')
                    ddMes = float(ddMes_str) if ddMes_str else 0.0

                    ddMefs_str = item.get('ddMefs')
                    ddMefs = float(ddMefs_str) if ddMefs_str else 0.0

                    res_data = {
                        'stnIds': stn_id,
                        'ddMes': ddMes,
                        'ddMefs': ddMefs,
                        'stnNm': item.get('stnNm'),
                        'date': date_str
                    }
                    session.add(SnowApiData(**res_data))
    session.commit()
    session.close()

def main():
    api_config = config_info()
    api_url = f"{api_config['api_end']}?serviceKey={api_config['serviceKey']}"

    stn_ids_from_api = data_from_api(api_url, [])

    init_stn_id = None

    if stn_ids_from_api:
        init_stn_id = stn_ids_from_api[0]

    engine = create_db_engine()

    if init_stn_id is not None:
        operation_db(engine, init_stn_id)


if __name__ == "__main__":
    main()