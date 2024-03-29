# Python practice field

<p align="left">
<a>
  <img src=https://img.shields.io/badge/python-~3.10-green>
</a>
<a>
  <img src=https://img.shields.io/badge/poetry-1.5.1-green>
</a>
<a>
  <img src=https://img.shields.io/badge/style-wemake-000000.svg>
</a>
<a>
  <img src=https://github.com/alexnazarv/training-project-api/actions/workflows/tests.yml/badge.svg>
</a>
<a>
  <img src=https://github.com/alexnazarv/training-project-api/actions/workflows/release.yml/badge.svg>
</a>
<a>
  <img src=https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit>
</a>
</p>

Just a practice field for making, linting, testing and describing python projects and setting CI/CD for it.

Here is a Docker image that runs FastAPI server with two simple get and post methods.

### TO DO:
#### CI:
Добавить правила для коммитов:
  * мануал шаг с деплоем на тест
  * мануал шаг с деплоем на прод

#### General:
* Добавить test coverage
* Описать все, что происходит в репо в шапке
***

## Requirements
* python ~3.10

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
docker run -d --rm --name apicontainer -p 8000:8000 apicontainer:test &&
docker rmi $(docker images -f "dangling=true" -q)
```

Clean up container and image:
```bash
docker rm -f apicontainer &&
docker rmi $(docker images apicontainer -q) -f
```

### Run tests
```bash
poetry run python3 -m pytest --cov=app
```

### Run linters
```bash
poetry run flake8 . && mypy . && isort .
```
