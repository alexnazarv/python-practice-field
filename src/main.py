"""
Main module.

DESCRIPTION:
* Get для получения рандомных данных
* Post для передачи словаря из которого будут генериться рандомные данные

TO DO на будущее:
1. Добавить обработку ошибок (передать exceptionhandler в app, чтобы доставать красивые ошибки пайдентика)
   Дока: https://fastapi.tiangolo.com/tutorial/handling-errors/
2. Навесть секурность из доки (засунуть в кубер с терминейтед прокси (nginx))
3. Ознакомиться с куками
4. https://docs.github.com/en/actions/automating-builds-and-tests/
   building-and-testing-python#starting-with-the-python-workflow-template
"""


from fastapi import FastAPI

from data_types import Charity
from data_types import RequestBody
from data_types import Stores
from functions import generate_random_order

app = FastAPI()


@app.get("/orders/{store}")
async def read_items(store: Stores,
                     charity: Charity = None) -> dict:
    """Get request returning random busket."""
    if store is Stores.apple:
        results = generate_random_order()

    if charity:
        results.update({"charity": charity})

    return results


@app.post("/orders/{store}")
async def read_custom_items(store: Stores,
                            requestbody: RequestBody,
                            charity: Charity):
    """Post request returning random busket based on passed to "requestbody" argument positions."""
    if store is Stores.apple:
        results = generate_random_order(requestbody)

    if charity:
        results.update({"charity": charity})

    return results
