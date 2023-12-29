from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from config_setting import create_db, create_db_engine, config_info
from stnIds_api import data_from_api

def operation_db(engine, stn_ids):
    create_db(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    today = datetime.now()
    pre_day = today - timedelta(days=1)
    pre_day_str = pre_day.strftime('%Y-%m-%d')

    params = {'startDt': pre_day_str}

    for stn_id in stn_ids:
        if stn_id:
            for item in stn_id.get('data', []):
                ddMes_str = item.get('ddMes')
                ddMes = float(ddMes_str) if ddMes_str else 0.0

                ddMefs_str = item.get('ddMefs')
                ddMefs = float(ddMefs_str) if ddMefs_str else 0.0

                res_data = {
                    'stnIds': stn_id,
                    'ddMes': ddMes,
                    'ddMefs': ddMefs,
                    'stnNm': item.get('stnNm')
                }
                session.add(res_data)
    session.commit()
    session.close()

def main():
    api_config = config_info()
    api_url = f"{api_config['api_end']}?serviceKey={api_config['serviceKey']}"
    stn_ids = data_from_api(stn_ids)
    api_data = data_from_api(api_url, stn_ids)

    for item in api_data.get('data', []):
        ddMes_str = item.get('ddMes')
        ddMes = float(ddMes_str) if ddMes_str else 0.0

        ddMefs_str = item.get('ddMefs')
        ddMefs = float(ddMefs_str) if ddMefs_str else 0.0

        res_data = {
            'stnIds': api_data.get('stnIds'),
            'ddMes': ddMes,
            'ddMefs': ddMefs,
            'stnNm': item.get('stnNm')
        }
    engine = create_db_engine()
    operation_db(engine, [res_data])


if __name__ == "__main__":
    main()