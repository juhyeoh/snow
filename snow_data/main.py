import json
import requests
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from config_setting import create_db_engine
from make_list import merged_data
from config_setting import config_info, SnowApiData, Base

def operation_db(session):
    api_config = config_info()
    url = api_config['api_end']

    fir_date = (datetime.now() - timedelta(days=7)).strftime('%Y%m%d')
    sec_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

    for stn_id, stn_nm in merged_data:
        try:
            params = {
                'serviceKey': api_config['serviceKey'],
                'pageNo': 1,
                'numOfRows': 7,
                'dataType': 'JSON',
                'dataCd': 'ASOS',
                'dateCd': 'DAY',
                'startDt': fir_date,
                'endDt': sec_date,
                'stnIds': stn_id
            }
            response = requests.get(url, params=params)
            data = response.json().get('response')

            if data and 'body' in data:
                items = data['body'].get('items')
                for item in items:
                    try:
                        if not isinstance(item, dict):
                            item = dict(item)
                        tm = item.get('tm')
                        stn_nm = item.get('stnNm')

                        ddMes_str = item.get('ddMes')
                        ddMes = float(ddMes_str) if ddMes_str else 0.0

                        ddMefs_str = item.get('ddMefs')
                        ddMefs = float(ddMefs_str) if ddMefs_str else 0.0

                        res_data = {
                            'date': datetime.strptime(tm, '%Y-%m-%d').date(),
                            'stnIds': stn_id,
                            'ddMefs': ddMefs,
                            'ddMes': ddMes,
                            'stnNm': stn_nm
                        }
                        session.add(SnowApiData(**res_data))
                    except Exception as e:
                        print(f"An error occurred: {e}")
        except requests.exceptions.RequestException as e:
            print(f"{e}")
    session.commit()
    

def main():
    engine = create_db_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    operation_db(session)

    session.close()

if __name__ == "__main__":
    main()
