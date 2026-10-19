#This custom library created for the collect all products from the Delta Exchange API.
import json
import logging
from datetime import datetime

import requests

logger = logging.getLogger(__name__)


def get_products():

    url = "https://api.india.delta.exchange/v2/products"

    try:
        logger.info("Fetching products from Delta Exchange")
        response = requests.get(url)
        if response.status_code == 200:
            products = response.json()
            # filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_product.json")
            # with open(filename, "w", encoding="utf-8") as products_file:
            #     json.dump(products["result"], products_file, indent=2, ensure_ascii=False)
            # logger.info("Products saved to %s", filename)
            return products["result"]

        logger.warning(
            "Failed to fetch products: Delta Exchange returned status %s",
            response.status_code,
        )
        return {
            "error": "Failed to fetch products",
            "status_code": f"{response.status_code}",
        }
    except (requests.RequestException, ValueError, OSError):
        logger.exception("Error while fetching products from Delta Exchange")
        return {"error": "Failed to fetch products"}