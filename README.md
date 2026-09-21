# ПО ЦОД — лабораторные и практические работы

Учебный репозиторий по дисциплине **«Программное обеспечение центров обработки данных»**.

**Студент:** Коломиец Александр Романович
**Группа:** ИКПИ-33
**Год:** 2026

---

## Лабораторные работы

| № | Тема | Содержимое |
|---|------|-----------|
| 1 | Система управления версиями Git. Сервис GitHub | [`lab1-git/`](lab1-git/) — журнал работы с локальным репозиторием |
| 2 | Совместная работа в GitHub | [`lab2-github/`](lab2-github/) — ветка, коммиты, pull request |
| 4 | Автоматизация тестирования Apache JMeter | [`lab4-jmeter/`](lab4-jmeter/) — тест-план `.jmx` |
| 5 | Apache JMeter, часть 2 | [`lab5-jmeter/`](lab5-jmeter/) — тест-план `.jmx` и `urls.csv` |

## Практические работы

| № | Тема | Содержимое |
|---|------|-----------|
| 1 | Установка Docker | [`pr1-docker-install/`](pr1-docker-install/) |
| 2 | Знакомство с Docker | [`pr2-docker-basics/`](pr2-docker-basics/) — журнал команд |
| 3 | Работа с образами: Dockerfile | [`pr3-dockerfile/`](pr3-dockerfile/) — `Dockerfile`, `index.html` |
| 4 | Docker Compose | [`pr4-compose/`](pr4-compose/) — два проекта Compose |

---

## Как воспроизвести

### Практическая №3 — собрать образ и запустить веб-сервер

```bash
cd pr3-dockerfile
docker build -t pocod/alpineapache:1.0 .
docker run -d -p 8080:80 --name pocod-web pocod/alpineapache:1.0
curl http://localhost:8080          # ожидается: Hello Docker Apache
```

### Практическая №4 — связка веб-сервера и веб-клиента

```bash
cd pr4-compose
docker compose -p pocod up -d --build
docker compose -p pocod logs webclient    # ожидается: HTTP 200
docker compose -p pocod down
```

Вариант с веб-сервером Apache вместо Python:

```bash
docker compose -p pocod -f docker-compose-apache.yml up -d
docker compose -p pocod -f docker-compose-apache.yml logs webclient
docker compose -p pocod -f docker-compose-apache.yml down
```

### Лабораторные №4 и №5 — тест-планы JMeter

Открыть `.jmx` в Apache JMeter через **File → Open**.
Для ЛР5 файл `urls.csv` должен лежать рядом с тест-планом.

---

## Отчёты

Отчёты по ГОСТ 7.32-2017 (PDF и DOCX) в репозиторий не включены — сдаются отдельно.
