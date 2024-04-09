import requests
from datetime import datetime, timedelta
from make_list import merged_data
from config_setting import config_info, SnowApiData


def oper_db(session):
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
                for item in items['item']:
                    tm = item['tm']
                    format_date = datetime.strptime(tm, '%Y-%m-%d')
                    date = format_date.strftime('%Y-%m-%d')
                    
                    ddMes_str = item['ddMes']
                    ddMes = float(ddMes_str) if ddMes_str else 0.0
                    ddMefs_str = item['ddMefs']
                    ddMefs = float(ddMefs_str) if ddMefs_str else 0.0
                                        
                    res_data = {
                        'stnIds': stn_id,
                        'stnNm': stn_nm,
                        'date': date,
                        'ddMes': ddMes,
                        'ddMefs': ddMefs
                    }
                    session.add(SnowApiData(**res_data))
                
        except requests.exceptions.RequestException as e:
            print(f"{e}")
    session.commit()