from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, PositiveFloat, field_validator


class Stores(str, Enum):
    apple = "apple"
    xiaomi = "xiaomi"


class ProductsInfo(BaseModel):
    product_name: str = Field(max_length=20)
    price: PositiveFloat = Field(gt=0)

    @field_validator("product_name")
    def product_should_contain_mac(cls, product_name: str) -> str: # noqa N805
        if "mac" not in product_name.lower():
            raise ValueError("Product_name should involve 'mac'")
        return product_name

    model_config = ConfigDict(extra="allow")


class PostReadItemsRequestBody(BaseModel):
    products_info: list[ProductsInfo] = Field(
        title="List of products names with corresponding prices")
