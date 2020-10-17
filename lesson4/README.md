## Тестирование API (requests + json schema)
### Цель: Тестирование API сервиса с помощью Python используя библиотеки pytest, requests, jsonschema
1. Тестирование сервиса jsonplaceholder.typicode.com
   
   Написать тесты для todos - https://jsonplaceholder.typicode.com/todos
  
   Документация - https://jsonplaceholder.typicode.com/guide
   
   Где есть возможность - нужно использовать параметризацию. 
  
   Список тестов:
    1. positive/negative тесты для Getting a resource
    2. тесты для Listing all resources
    3. positive/negative тесты для Creating a resource
    4. positive/negative тесты для Updating a resource with PUT
    5. тесты для Updating a resource with PATCH
    6. positive/negative тесты для Deleting a resource
    7. positive/negative тесты для Filtering resources
   Все тесты должны успешно проходить

2. Тестирование jsonsсhema сервиса jsonplaceholder.typicode.com
  Написать тесты для проверки структуры json (schema) todos - https://jsonplaceholder.typicode.com/todos
  Схемы должны быть оформлены в виде файлов и использоваться тестами
  Для теста Listing all resources нужно использовать файл со схемой из теста Getting a resource указав ссылку на него в схеме

    Список тестов:

    1. Getting a resource
    2. Listing all resources

    Все тесты должны успешно проходить
  
Критерии оценки: Репозиторий должен быть правильно оформлен: README, gitignore (никаких служебных или лишних файлов), requirements.txt, PEP8