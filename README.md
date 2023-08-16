### Запуск
Сборка и запуск контейнера: (добавить удаление промежуточного контейнера после сборки)

    docker build . -t apicontainer -t apicontainer:0.1
    docker run -d --rm --name apicontainer -p 80:80 apicontainer:0.1

### TO DO:  
GitHub actions -- сборка и пуш контейнера в докерхаб
