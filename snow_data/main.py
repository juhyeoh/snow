from datetime import datetime, timedelta
import requests
from sqlalchemy.orm import sessionmaker
from config_setting import create_db_engine
from make_list import merged_values
from config_setting import config_info, SnowApiData, Base

def operation_db(session):
    merged_data = merged_values
    api_config = config_info()
    url = api_config['api_end']

    fir_date = (datetime.now() - timedelta(days=8)).strftime('%Y%m%d')
    sec_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

    try:
        stn_ids = ','.join(merged_data)

        params = {
            'serviceKey': api_config['serviceKey'],
            'pageNo': 1,
            'numOfRows': 7,
            'dataType': 'JSON',
            'dataCd': 'ASOS',
            'dateCd': 'DAY',
            'startDt': fir_date,
            'endDt': sec_date,
            'stnIds': stn_ids
        }
        response = requests.get(url, params=params)
        data = response.json()

        for item in data:
            stn_id = item.get('stnIds')

            ddMes_str = item.get('ddMes')
            ddMes = float(ddMes_str) if ddMes_str else 0.0

            ddMefs_str = item.get('ddMefs')
            ddMefs = float(ddMefs_str) if ddMefs_str else 0.0

            tm = item.get('tm')

            res_data = {
                'date': tm,
                'stnIds': stn_id,
                'ddMefs': ddMefs,
                'ddMes': ddMes,
                'stnNm': item.get('stnNm')
            }
            session.add(SnowApiData(**res_data))

        session.commit()

    except requests.exceptions.RequestException as e:
        print(f"{e}")

def main():
    engine = create_db_engine()
    Session = sessionmaker(bind=engine)

    with Session() as session:
        Base.metadata.create_all(engine)
        operation_db(session)

if __name__ == "__main__":
    main()
