<p align="center">
<a>
  <img src=https://img.shields.io/badge/python-~3.10-green>
</a>
<a>
  <img src=https://img.shields.io/badge/poetry-1.5.1-green>
</a>
<a>
  <img src=https://img.shields.io/badge/style-wemake-000000.svg
</a>
<a>
  <img src=https://github.com/alexnazarv/training-project-api/actions/workflows/ci.yml/badge.svg>
</a>
</p>

### TO DO:

#### CI
1. Оптимизация, посмотреть есть ли лишние actions (поетри, например)
2. Кеширование виртуального окружения для прогона линтеров и тестов
3. Использовать semantic release (и convential commit). Сделать пуш в регистри мануальным
4. Тест для докер имеджа -- сборка и запуск -> гет запрос. @moneretin, надо ли если есть тесты приложения и билд в ci?
***

## Description
Just FastApi playground

### Requirements
* python ~3.10
* poetry

## Debug

Clone repo first:
```bash
git clone git@github.com:alexnazarv/training-project-api.git
```

### Run without Docker

Install poetry:
```bash
pip install poetry==1.5.1
```

Move to project directory and make a venv:
```bash
cd training-project-api && poetry shell
```

Install dependencies and run the app:
```bash
poetry install && poetry run python3 -m app.main
```

### Run with Docker

Build image and run container:
```bash
docker build . -t apicontainer -t apicontainer:test &&
docker rmi $(docker images -f "dangling=true" -q) &&
docker run -d --rm --name apicontainer -p 8000:8000 apicontainer:test
```

Clean up container and image:
```bash
docker rm -f apicontainer &&
docker rmi $(docker images apicontainer -q) -f
```

### Run tests
```bash
poetry run python3 pytest
```

### Run linters
```bash
poetry run flake8 . && mypy . && isort .
```
