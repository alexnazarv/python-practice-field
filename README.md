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
* Использовать semantic release (и convential commit). Сделать пуш в регистри мануальным
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
