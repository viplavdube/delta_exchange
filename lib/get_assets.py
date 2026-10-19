import logging
import requests

logger = logging.getLogger(__name__)


def get_assets():

    url = "https://api.india.delta.exchange/v2/assets"

    payload={}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch asset", "status_code": f"{response.status_code}"}
    except requests.RequestException as e:
        logger.exception("Error while fetching assets from Delta Exchange")
        return {"error": "Failed to fetch assets"}