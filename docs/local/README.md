# Часть 1: WordPress на Mac через MAMP

[← К оглавлению репозитория](../../README.md)

```mermaid
flowchart LR
    A[Шаг 1: Скачать] --> B[Шаг 2: MAMP]
    B --> C[Шаг 3: WordPress]
    C --> D[Админка]
```

---

## Маршрут

| Шаг | Файл | Содержание |
|-----|------|------------|
| 1 | [01-before.md](01-before.md) | Скачивание MAMP и WordPress |
| 2 | [02-mamp.md](02-mamp.md) | Установка и настройка MAMP |
| 3 | [03-wordpress.md](03-wordpress.md) | БД, установка WP, первый вход |
| — | [troubleshooting.md](troubleshooting.md) | Ошибки MAMP и WordPress |

**[Начать шаг 1 →](01-before.md)**

---

## Чеклист за 10 минут

1. Скачать MAMP и WordPress → [01-before.md](01-before.md)
2. Установить и настроить MAMP → [02-mamp.md](02-mamp.md)
3. База, установка, вход в админку → [03-wordpress.md](03-wordpress.md)

**Проблемы:** [troubleshooting.md](troubleshooting.md)

---

## Шпаргалка

| Параметр | Значение |
|----------|----------|
| Сайт | `http://localhost/название-вашей-папки/` |
| Админка | `http://localhost/название-вашей-папки/wp-admin/` |
| Apache | порт `80` |
| MySQL | порт `3306` |
| phpMyAdmin | `http://localhost/phpMyAdmin/` |
| htdocs | `/Applications/MAMP/htdocs/` |
| MySQL | `root` / `root` |

---

## Видео

**[Установка WordPress на MAMP (YouTube)](https://www.youtube.com/watch?v=OwnwrO6Ub28&t=1s)**

> В видео порты могут быть `8888` / `8889` — в этом гайде **`80`** и **`3306`**.

---

## Дальше

- Сайт на localhost готов → **[Часть 2: перенос](../migrate/README.md)**
- Сразу в интернет без Mac → **[Часть 3: hosting](../hosting/README.md)**
