"""Data types for application."""
from enum import Enum
from typing import Annotated

from fastapi import Body
from fastapi import Query
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator
from pydantic import PositiveFloat


class Stores(str, Enum):
    """Valid stores names."""

    apple = "apple"
    xiaomi = "xiaomi"


class ProductsInfo(BaseModel):
    """Check for custom product's info passed to post request."""

    product_name: str = Field(max_length=20)
    price: PositiveFloat = Field(gt=0)

    @field_validator("product_name", mode="before")
    def product_should_contain_mac(cls, product_name: str) -> str:  # noqa N805
        if "mac" not in product_name.lower():
            raise ValueError("Product_name should involve 'mac'")
        return product_name

    model_config = ConfigDict(extra="allow")


class PostReadItemsRequestBody(BaseModel):
    """Request body data type."""

    products_info: list[ProductsInfo] = Field(
        title="List of products names with corresponding prices")


class Charity(BaseModel):
    """Data type for optional argument "charity" passed to request."""

    charity: Annotated[int | None,
                       Query(title="Optional money for charity",
                             description="Money for charity",
                             alias="clean-sea-charity",
                             ge=1,
                             include_in_schema=True,
                             deprecated=False)]


class RequestBody(BaseModel):
    """Data type for RequestBody passed to post request."""

    requestbody: Annotated[PostReadItemsRequestBody,
                           Body(title="Request body",
                                description="Dict to generate \
                                             random data from",
                                examples=[{"products_info": [
                                    {"product_name": "mac2", "price": 11},
                                    {"product_name": "mac3", "price": 22}
                                         ]}],
                                embed=False)]
