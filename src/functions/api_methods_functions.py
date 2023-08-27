"""Functions used to make responses."""
import random

from src.data_types import StorePositions
from src.functions.common import read_default_positions

DEFAULT_APPLE_STORE_POSITIONS = read_default_positions()


def generate_random_order(products_info: StorePositions = DEFAULT_APPLE_STORE_POSITIONS) -> dict:
    """
    Parse dictionary and generate new one with random quantities and total price.

    :param products_info: dictionary that contains store positions
    :returns: random basket generated from products_info
    """
    products_info_dumped = products_info.model_dump()
    store_positions = {}

    for dict_element in products_info_dumped["products_info"]:
        store_positions.update({dict_element["product_name"]: dict_element["price"]})

    product_name = random.choice(list(store_positions.keys()))
    price_per_item = store_positions[product_name]
    quantity = random.randint(1, 100)
    total_product_price = quantity * price_per_item

    return {
        "product_name": product_name,
        "price_per_item": price_per_item,
        "quantity": quantity,
        "total_price": total_product_price,
    }


if __name__ == "__main__":
    generate_random_order()
