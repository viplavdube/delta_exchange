#This custom library created for the collect all products from the Delta Exchange API.
import logging
import requests

logger = logging.getLogger(__name__)


def get_indices():

    url = "https://api.india.delta.exchange/v2/indices"

    payload={}
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            indices = response.json()
            return indices["result"]
        else:
            return {"error": "Failed to fetch indices", "status_code": f"{response.status_code}"}
    except requests.RequestException as e:
        logger.exception("Error while fetching indices from Delta Exchange")
        return {
            "error": "Failed to fetch indices",
        }