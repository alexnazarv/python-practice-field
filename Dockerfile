FROM python:3.10.10-alpine
COPY ./pyproject.toml ./poetry.lock* ./
RUN pip install poetry==1.5.1 && poetry install --only main --no-cache
COPY ./app /app
CMD ["poetry", "run", "python3", "-m", "app.main"]