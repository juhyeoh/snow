from datetime import datetime, timedelta
import json
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
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{e}")
        return []

def data_from_api(list_data):
    try:
        params = {'serviceKey': api_config['serviceKey'], 'pageNo': 1, 'numOfRows': 7, 'dataType': 'JSON', 'dataCd': 'ASOS', 'dateCd': 'DAY', 'startDt': fir_date, 'endDt': sec_date, 'stnIds': list_data}
        response = requests.get(url, params=params)
        print(response.url)
        response.raise_for_status()

        if response.text:
            data = response.json()
            if 'response' in data and 'body' in data['response'] and 'items' in data['response']['body'] and 'item' in data['response']['body']['items']:
                stn_ids_list = [item.get('stnIds') for item in data['response']['body']['items']['item']]
                stn_ids_list = [stn_id for stn_id in stn_ids_list if stn_id is not None]
                return stn_ids_list
    except requests.exceptions.RequestException as e:
        print(f"{e}")
        return []
    
stn_ids_list = stnid_data()
stn_ids_from_api = data_from_api(stn_ids_list)

if stn_ids_from_api:
    init_stn_id = stn_ids_from_api[0]