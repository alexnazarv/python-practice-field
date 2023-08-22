"""
Main module.

DESCRIPTION:
* Get для получения рандомных данных
* Post для передачи словаря из которого будут генериться рандомные данные

TO DO на будущее:
1.Добавить обработку ошибок (передать exceptionhandler в app, чтобы доставать красивые ошибки пайдентика)
  Дока: https://fastapi.tiangolo.com/tutorial/handling-errors/  # noqa: RST301,RST201
2.Навесть секурность из доки (засунуть в кубер с терминейтед прокси (nginx))
3.Ознакомиться с куками
4.https://docs.github.com/en/actions/automating-builds-and-tests/
  building-and-testing-python#starting-with-the-python-workflow-template # noqa: RST301
"""
from fastapi import FastAPI
import uvicorn

from src.data_types import Charity
from src.data_types import RequestBody
from src.data_types import Stores
from src.functions import generate_random_order

app = FastAPI()


@app.get("/orders/{store}")
async def read_items(store: Stores, charity: Charity = None) -> dict:
    """Get request returning random busket."""
    if store is Stores.apple:
        response = generate_random_order()

    if charity:
        response.update({"charity": charity})

    return response


@app.post("/orders/{store}")
async def read_custom_items(store: Stores, requestbody: RequestBody, charity: Charity):
    """Get request returning random busket from data sent by user."""
    if store is Stores.apple:
        response = generate_random_order(requestbody)

    if charity:
        response.update({"charity": charity})

    return response


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)  # noqa: S104, WPS432
