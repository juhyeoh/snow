import requests
from config_setting import config_info

global_stn_ids = []

def data_from_api(api_url, init_stn_id):
    url = f"{api_url}?stnIds={init_stn_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        stn_ids = data.get('stnIds', [])
        return stn_ids
    
api_config = config_info()
api_url = f"{api_config['api_end']}?serviceKey={api_config['serviceKey']}"

stn_ids_from_api = data_from_api(api_url, [])

if stn_ids_from_api:
    init_stn_id = stn_ids_from_api[0]