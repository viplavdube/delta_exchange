#This custom library created for the collect all products from the Delta Exchange API.
import requests


def get_indices():

    url = "https://api.india.delta.exchange/v2/indices"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch indices", "status_code": f"{response.status_code}"}