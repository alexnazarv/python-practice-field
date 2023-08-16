"""
DESCRIPTION:
* Get для получения рандомных данных
* Post для передачи словаря из которого будут генериться рандомные данные

QUESTIONS:
charity -- в каждом методе описывать или есть вариант вынести отдельно часто повторяющийся параметр?
Поему мы пишем async def? https://fastapi.tiangolo.com/async/

TO DO на будущее:
1. Добавить обработку ошибок (передать exceptionhandler в app, чтобы доставать красивые ошибки
   пайдентика)
   Дока: https://fastapi.tiangolo.com/tutorial/handling-errors/
2. Навесть секурность из доки (засунуть в кубер с терминейтед прокси (nginx))
3. Ознакомиться с вебсокетами https://fastapi.tiangolo.com/advanced/websockets/
4. Ознакомиться с куками
5. https://docs.github.com/en/actions/automating-builds-and-tests/
   building-and-testing-python#starting-with-the-python-workflow-template
"""
from typing import Annotated

from fastapi import Body, FastAPI, Query

from .api_data_types import PostReadItemsRequestBody, Stores
from .api_functions import generate_random_order

app = FastAPI()


@app.get("/orders/{store}")
async def read_items(store: Stores,
                     charity: Annotated[int | None,
                                        Query(title="Optional money for charity",
                                              description="Money for charity",
                                              alias="clean-sea-charity",
                                              ge=0,
                                              include_in_schema=True,
                                              deprecated=False)] = None) -> dict:
    if store is Stores.apple:
        results = generate_random_order()

    if charity:
        results.update({"charity": charity})

    return results


@app.post("/orders/{store}")
async def read_custom_items(store: Stores,
                            requestbody: Annotated[PostReadItemsRequestBody,
                                                   Body(title="Request body",
                                                        description="Dict to generate \
                                                                     random data from",
                                                        examples=[{"products_info": [
                                                            {"product_name": "mac2", "price": 11},
                                                            {"product_name": "mac3", "price": 22}
                                                        ]}],
                                                        embed=False)],
                            charity: Annotated[int | None,
                                               Query(title="Optional money for charity",
                                                     description="Money for charity",
                                                     alias="clean-sea-charity",
                                                     ge=1,
                                                     include_in_schema=True,
                                                     deprecated=False)] = None):
    if store is Stores.apple:
        results = generate_random_order(requestbody)

    if charity:
        results.update({"charity": charity})

    return results
