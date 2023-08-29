"""Main module tests."""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestGet:
    """Class for testing get functions."""

    def test_read_items(self):
        """Tests read_items get request with optional charity param that has alias clean-sea-charity."""
        response = client.get("/orders/apple?clean-sea-charity=5")
        assert response.status_code == 200


class TestPost:
    """Class for testing post functions."""

    def test_read_custom_items_to_success(self):
        """Tests read_items post request with passed requstbody (json arg)."""
        response = client.post("/orders/apple",
                               json={"products_info": [{"product_name": "mac2", "price": 11.0123},
                                                       {"product_name": "mac3", "price": 22}]})
        assert response.status_code == 200, response.json()["detail"][0]["msg"]

    def test_read_custom_items_to_success_with_charity(self):
        """
        Tests read_items post request with passed requstbody (json arg) and
        optional charity param that has alias clean-sea-charity.
        """
        response = client.post("/orders/apple?clean-sea-charity=5",
                               json={"products_info": [{"product_name": "mac2", "price": 11.0123},
                                                       {"product_name": "mac3", "price": 22}]})
        assert response.status_code == 200, response.json()["detail"][0]["msg"]

    def test_read_custom_items_to_fail(self):
        response = client.post("/orders/apple",
                               json={"products_info": [{"product_name": "map2", "price": 11},
                                                       {"product_name": "mac3", "price": 22}]})
        assert response.status_code == 422

    def test_read_custom_items_to_fail_with_charity(self):
        response = client.post("/orders/apple?clean-sea-charity=-1",
                               json={"products_info": [{"product_name": "mac2", "price": 11.0123},
                                                       {"product_name": "mac3", "price": 22}]})
        assert response.status_code == 422, response.json()["detail"][0]["msg"]
