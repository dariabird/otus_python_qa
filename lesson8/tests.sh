#!/bin/bash

# Собираем image с тегом my_tests
docker build -t my_tests .

# Запускаем контейнер под именем my_run из image my_tests
docker run --name my_run my_tests --browser chrome --is_remote

# Копируем из контейнера созданный allure-report
docker cp my_run:/app/allure-report .

# Запускаем хост для отчёта аллюр (утилита лежит локально)
# Хост отчёта нужно будет остановить руками
allure serve allure-report

# Удаляем из системы созданный контейнер
docker system prune -f