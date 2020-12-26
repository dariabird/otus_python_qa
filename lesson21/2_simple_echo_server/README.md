## Simple echo-server
Простой echo-сервер:
- принимает HTTP-запрос,
- парсит заголовки,
- возвращает их обратно клиенту в формает json.

##Как проверить работу
Запускаем сервер:
```bash
python simple_server.py
```
В терминале выполняем команду:
```bash
curl -v 'http://127.0.0.1:14985' \
  -H 'authority: yandex.ru' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'device-memory: 8' \
  -H 'dpr: 1' \
  -H 'viewport-width: 1280' \
  -H 'rtt: 50' \
  -H 'downlink: 10' \
  -H 'ect: 4g' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
```

И получим ответ:
```bash
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
   "authority":"yandex.ru",
   "pragma":"no-cache",
   "cache-control":"no-cache",
   "device-memory":"8",
   "dpr":"1",
   "viewport-width":"1280",
   "rtt":"50",
   "downlink":"10",
   "ect":"4g",
   "upgrade-insecure-requests":"1",
   "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
   "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
   "sec-fetch-site":"none",
   "sec-fetch-mode":"navigate",
   "sec-fetch-user":"?1",
   "sec-fetch-dest":"document",
   "accept-language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}
```
