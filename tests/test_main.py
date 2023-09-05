"""Main module tests."""
from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestGet:
    """Class for testing get functions."""

    @pytest.mark.parametrize('url, expected', [
        ('/orders/apple?charity=5', HTTPStatus.OK),
        ('/orders/apple', HTTPStatus.OK),
        ('/orders/apple?charity=w', HTTPStatus.UNPROCESSABLE_ENTITY),
        ('/orders/xiaomi?charity=2', HTTPStatus.UNPROCESSABLE_ENTITY),
        ('/baskets/apple', HTTPStatus.NOT_FOUND),
    ])
    def test_read_items(self, url: str, expected: HTTPStatus) -> None:
        """Tests read_items get request with optional charity param that has alias clean-sea-charity."""
        response = client.get(url)
        assert response.status_code == expected


class TestPost:
    """Class for testing post functions."""

    @pytest.mark.parametrize('url, json_body, expected', [
        (
            '/orders/apple',
            {'products_info': [
                {'product_name': 'iMac', 'price': 1199.99},
                {'product_name': 'HomePod Mini', 'price': 99.99},
            ]},
            HTTPStatus.OK,
        ),
        (
            '/orders/apple?charity=5',
            {'products_info': [
                {'product_name': 'MacBook Pro 15', 'price': 1399.99},
                {'product_name': 'Apple Watch Series 7', 'price': 499.99},
            ]},
            HTTPStatus.OK,
        ),
        (
            '/orders/apple',
            {'products_info': [
                {'product_name': 'MacBook Pro 15', 'price': 1399.99},
                {'product_name': 'GALAXY ULTRA', 'price': 799.99},
            ]},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        ),
        (
            '/orders/xiaomi',
            {'products_info': [
                {'product_name': 'MacBook Pro 15', 'price': 1399.99},
                {'product_name': 'Apple Watch Series 7', 'price': 449},
            ]},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        ),
        (
            '/basket/apple',
            {'products_info': [
                {'product_name': 'MacBook Pro 15', 'price': 1399.99},
                {'product_name': 'Apple Watch Series 7', 'price': 449},
            ]},
            HTTPStatus.NOT_FOUND,
        ),
    ])
    def test_read_custom_items_to_success(self, url: str, json_body: dict, expected: HTTPStatus) -> None:
        """Tests read_items post request with passed requstbody (json arg)."""
        response = client.post(url, json=json_body)
        assert response.status_code == expected, response.json()['detail'][0]['msg']
