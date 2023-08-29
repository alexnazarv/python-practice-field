[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide) 
[![Build Status](https://travis-ci.org/tylerwince/flake8-bandit.svg?branch=master)](https://travis-ci.org/tylerwince/flake8-bandit)  
Отсюда забрать linkedIn https://github.com/vbriand/vbriand

TO DO:
1. Кеширование виртуального окружения
2. Кеширование Docker image
3. Красивое оформление README с HTML переносами как у автора fastapi (Просто посередине шапки воткнуть лейблы)
4. Добавить лейблы по тестам, билдам, линкедин


### Description
Just FastApi playground and part of a bigger one

### Run without Docker
```bash
poetry install && poetry run python3 -m app.main
```

### Run with Docker: 

#### Build image and run container
```bash
docker build . -t apicontainer -t apicontainer:0.1 && 
docker run -d --rm --name apicontainer -p 8000:8000 apicontainer:0.1
```
#### Clean up container and image:
```bash
docker rm -f apicontainer &&
docker rmi $(docker images apicontainer -q) -f &&
docker rmi $(docker images -f "dangling=true" -q)
```

### Run tests
```bash
poetry run python3 -m pytest
```
OR  
```bash
python3 -m pytest
```

### Run linters
```bash
poetry run flake8 . && mypy . && isort .
```
