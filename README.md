### Запуск
Сборка и запуск контейнера:

    docker build . -t apicontainer -t apicontainer:0.1
    docker run -d --rm --name apicontainer -p 80:80 apicontainer:0.1
