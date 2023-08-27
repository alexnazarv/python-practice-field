"""Data types for application."""
from enum import Enum
from typing import Annotated, Optional

from fastapi import Body, Query
from pydantic import BaseModel, ConfigDict, Field, PositiveFloat, field_validator

DEFAULT_PRODUCTS_SUBSTRS = ("mac", "iphone", "ipad", "watch", "keyboard", "pencil", "airpods", "home")

Charity = Optional[
    Annotated[
        int,
        Query(
            title="Optional money for charity",
            description="Money for charity",
            ge=1,
            include_in_schema=True,
            deprecated=False,
        )]]


class Stores(Enum):
    """Valid stores names."""

    apple = "apple"


class ProductsInfo(BaseModel):
    """Check for custom product's info passed to post request."""

    product_name: str = Field(max_length=20)
    price: PositiveFloat = Field(gt=0)

    @classmethod
    def validation_func(cls, product_name: str) -> bool:
        """
        Check if information about a product contains default substrings.

        :param product_name: checked param
        :returns: bool
        """
        return any(substring in product_name.lower() for substring in DEFAULT_PRODUCTS_SUBSTRS)

    @field_validator("product_name", mode="before")
    def product_should_contain_mac(cls, product_name: str) -> str:
        """
        Apply validation_func to product_name param.

        :param product_name: checked param
        :raises ValueError: if product_name doesn't contain mac substr
        :returns: product_name without changes if condition is passed
        """
        if not ProductsInfo.validation_func(product_name):
            raise ValueError(
                "Product_name should involve default_products_substrs: {default_products_substrs}".format(
                    default_products_substrs=DEFAULT_PRODUCTS_SUBSTRS,
                ),
            )
        return product_name

    model_config = ConfigDict(extra="allow")


class StorePositions(BaseModel):
    """Request body data type."""

    products_info: list[ProductsInfo] = Field(
        title="List of products names with corresponding prices",
    )


class RequestBody(BaseModel):
    """Data type for RequestBody passed to post request."""

    requestbody: Annotated[
        StorePositions,
        Body(
            title="Request body",
            description="Dict to generate random data from",
            examples=[
                {"products_info": [
                    {"product_name": "MacBook Pro", "price": 1999.99},
                    {"product_name": "iPad Air", "price": 899.99},
                ]}],
            embed=False,
        )]
