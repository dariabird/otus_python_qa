# Устанавливаю базовый образ
FROM python:3.6

# Устанавливаю рабочую директорию внутри контейнера
# Диретокрия будет создана если её не было
# Будет в дальнешйем использовать как базовая
WORKDIR /app

# Копирую сначала зависимости
# Для того чтобы не пересобирать их каждый раз при сборке
COPY requirements.txt .

# Выполняю необходимые команды
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирую остальные файлы проекта
COPY . .

# Предустанавливаем команду pytest и отчёт
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
# Можно использовать так `docker run --rm my_tests --browser firefox`
# --is_remote показывает, что тесты будут запускаться в selenoid
CMD ["--browser", "chrome", "--is_remote"]