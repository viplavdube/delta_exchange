import requests


def get_assets():

    url = "https://api.india.delta.exchange/v2/assets"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch asset", "status_code": f"{response.status_code}"}