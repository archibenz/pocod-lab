# ПР3 — Работа с образами в Docker

Сборка собственного образа при помощи `Dockerfile`.

```bash
docker build -t pocod/alpineapache:1.0 .
docker run -d -p 8080:80 pocod/alpineapache:1.0
curl http://localhost:8080
```

Ожидаемый ответ: `HTTP/1.1 200 OK`, `Server: Apache/2.4.68 (Unix)`, тело — `Hello Docker Apache`.
