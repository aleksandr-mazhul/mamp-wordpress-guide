# Часть 1: WordPress на Mac через MAMP

[← К оглавлению репозитория](../../README.md)

Установка WordPress **локально** — без хостинга. Дальше: [перенос](../migrate/README.md) или [сразу на хостинг](../hosting/README.md).

```mermaid
flowchart LR
    A[1 Скачать] --> B[2 MAMP]
    B --> C[3 WordPress]
    C --> D[Админка]
```

---

## Шаги

| Шаг | Файл | Содержание |
|-----|------|------------|
| 1 | [01-before.md](01-before.md) | Скачать MAMP и WordPress |
| 2 | [02-mamp.md](02-mamp.md) | Установка, порты 80/3306, htdocs |
| 3 | [03-wordpress.md](03-wordpress.md) | База, установка, вход в админку |
| — | [troubleshooting.md](troubleshooting.md) | Если что-то сломалось |

---

## Шпаргалка

| Параметр | Значение |
|----------|----------|
| Сайт | `http://localhost/название-вашей-папки/` |
| Админка | `.../wp-admin/` |
| htdocs | `/Applications/MAMP/htdocs/` |
| MySQL | `root` / `root`, порт `3306` |
| phpMyAdmin | `http://localhost/phpMyAdmin/` |

Видео (порты в ролике могут отличаться): [YouTube](https://www.youtube.com/watch?v=OwnwrO6Ub28&t=1s)

---

**[Начать шаг 1 →](01-before.md)**
