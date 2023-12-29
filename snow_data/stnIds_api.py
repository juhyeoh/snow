import requests

def data_from_api(api_url, stn_ids):
    url = f"{api_url}?stnIds={stn_ids}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        stn_ids = data.get('stnIds', [])
        return stn_ids