[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Добавить еще Build Status
### Запуск
Сборка и запуск контейнера:

    docker build . -t apicontainer -t apicontainer:0.1
    docker run -d --rm --name apicontainer -p 80:80 apicontainer:0.1

https://github.com/PyCQA/isort/blob/main/.flake8 -- длина 100, странно
