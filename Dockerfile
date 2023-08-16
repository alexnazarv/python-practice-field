FROM python:3.10.10 as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
FROM python:3.10.10
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip -r /code/requirements.txt
COPY ./training_api /code/training_api
CMD ["uvicorn", "training_api.main:app", "--host", "0.0.0.0", "--port", "80"]
