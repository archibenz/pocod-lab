# ПР4 — Docker Compose

Два варианта связки «веб-сервер + веб-клиент»:

- `docker-compose.yml` — веб-сервер на Python (`http.server`), порт 8000
- `docker-compose-apache.yml` — веб-сервер Apache из образа ПР3, порт 8081

Клиент обращается к серверу **по имени сервиса** (`http://webserver:8000/`),
а не по IP-адресу: Compose создаёт общую сеть со встроенным разрешением имён.

Запуск с именем проекта `pocod`, чтобы контейнеры группировались отдельно:

```bash
docker compose -p pocod up -d --build
docker compose -p pocod down
```
