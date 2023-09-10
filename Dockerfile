FROM python:3.10.11-alpine
COPY ./pyproject.toml ./poetry.lock* ./
RUN pip install poetry==1.5.1 && poetry install --only main --no-cache --no-root
COPY ./app /app
CMD ["poetry", "run", "python3", "-m", "app.main"]
