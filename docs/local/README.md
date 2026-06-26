# Часть 1: WordPress на Mac через MAMP

[← К оглавлению репозитория](../../README.md)

```mermaid
flowchart LR
    A[Скачать] --> B[MAMP]
    B --> C[База данных]
    C --> D[WordPress]
    D --> E[Админка]
```

---

## Чеклист за 10 минут

1. Скачать [MAMP Free](https://www.mamp.info/ru/downloads/) и [WordPress](https://ru.wordpress.org/download/) → [01-before.md](01-before.md)
2. Установить MAMP → [01-before.md](01-before.md)
3. Apache, порты `80` / `3306`, папка htdocs → [02-mamp.md](02-mamp.md)
4. Start в MAMP, создать базу в phpMyAdmin → [03-wordpress.md](03-wordpress.md)
5. Распаковать WordPress в htdocs → [03-wordpress.md](03-wordpress.md)
6. Подключить базу, запустить установку → [03-wordpress.md](03-wordpress.md)
7. Войти в админку → [03-wordpress.md](03-wordpress.md)

**Проблемы:** [troubleshooting.md](troubleshooting.md)

---

## Шаги

| Шаг | Файл | Содержание |
|-----|------|------------|
| 1 | [01-before.md](01-before.md) | Скачивание, требования |
| 2 | [02-mamp.md](02-mamp.md) | Установка и настройка MAMP |
| 3 | [03-wordpress.md](03-wordpress.md) | БД, установка WP, первый вход |

---

## Шпаргалка (вся часть 1)

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

Сайт готов локально → **[Часть 2: перенос на хостинг](../migrate/README.md)**

[Начать: Подготовка →](01-before.md)
