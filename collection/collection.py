import os
from datetime import datetime
import logging
import json
from lib.get_products import get_products
from lib.get_assets import get_assets
from lib.get_indices import get_indices
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    logging.basicConfig(level=logging.INFO)
    products = get_products()
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    products_filename = os.path.join(DATA_DIR, f"{filename}_product.json")
    with open(products_filename, "w", encoding="utf-8") as products_file:
        json.dump(products, products_file, indent=2, ensure_ascii=False)
    logger.info("Products saved to %s", filename)
    assets = get_assets()
    assets_filename = os.path.join(DATA_DIR, f"{filename}_assets.json")
    with open(assets_filename, "w", encoding="utf-8") as assets_file:
        json.dump(assets, assets_file, indent=2, ensure_ascii=False)
    logger.info("Assets saved to %s", filename)
    indices = get_indices()
    indices_filename = os.path.join(DATA_DIR, f"{filename}_indices.json")
    with open(indices_filename, "w", encoding="utf-8") as indices_file:
        json.dump(indices, indices_file, indent=2, ensure_ascii=False)
    logger.info("Indices saved to %s", filename)