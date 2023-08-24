"""Functions used to make responses."""
import random

from src.data_types import PostReadItemsRequestBody

apple_store_positions = {
    "iPhone 13 Pro": 1099.99,
    "iPad Air": 699.99,
    "MacBook Pro": 1999.99,
    "AirPods Pro": 249.99,
    "Apple Watch Series 7": 399.99,
    "iMac": 1299.99,
    "HomePod Mini": 99.99,
    "Apple Pencil": 129.99,
    "Mac Mini": 699.99,
    "Magic Keyboard": 199.99,
}


def generate_random_order(products_info: PostReadItemsRequestBody = apple_store_positions) -> dict:
    """
    Parse dictionary and generate new one with random quantities and total price.

    :param products_info: dictionary that contains store positions
    :returns: random basket generated from products_info
    """
    if products_info != apple_store_positions:
        products_info = products_info.model_dump()
        store_positions = {}
        for dict_element in products_info["products_info"]:
            store_positions.update({dict_element["product_name"]: dict_element["price"]})
    elif products_info == apple_store_positions:
        store_positions = products_info

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
