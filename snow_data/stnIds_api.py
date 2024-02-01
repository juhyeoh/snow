from datetime import datetime, timedelta
import requests
from config_setting import config_info

api_config = config_info()
url = api_config['api_end']

fir_date = (datetime.now() - timedelta(days=8)).strftime('%Y%m%d')
sec_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')

def stnid_data():
    try:
        params = {'serviceKey': api_config['serviceKey']}
        response = requests.get(url, params=params)
        stnIds = response.json().get('stnIds', [])
        return stnIds
    except requests.exceptions.RequestException as e:
        print(f"{e}")
        return []

def data_from_api(stnIds):
    try:
        params = {'serviceKey': api_config['serviceKey'], 'pageNo': 1, 'numOfRows': 7, 'dataType': 'JSON', 'dataCd': 'ASOS', 'dateCd': 'DAY', 'startDt': fir_date, 'endDt': sec_date, 'stnIds': ','.join(stnIds)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{e}")
        return []

stnIds = stnid_data()

if stnIds:
    stn_ids_list = stnIds
    stn_ids_from_api = data_from_api(stnIds)
    
    if stn_ids_from_api:
        init_stn_id = stn_ids_from_api[0]