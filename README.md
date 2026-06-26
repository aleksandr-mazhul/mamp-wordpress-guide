# Локальный WordPress на macOS через MAMP

![macOS](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white)
![MAMP Free](https://img.shields.io/badge/MAMP-Free-3D8FC6?style=flat)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)

> Пошаговый гайд: от установки MAMP до первого работающего сайта на WordPress.

Этот репозиторий — подробная инструкция для запуска WordPress локально на Mac. Никакого хостинга и домена не нужно: всё работает прямо на вашем компьютере через **MAMP Free**.

<!-- TODO: заменить placeholder на реальный скриншот -->
![Работающий WordPress-сайт](assets/images/06-first-launch/site-running.png)

*Рис. 1 — Итоговый результат: WordPress-сайт открыт в браузере*

---

## Быстрый старт

| Шаг | Действие | Раздел |
|-----|----------|--------|
| 1 | Установить MAMP | [docs/02-install-mamp.md](docs/02-install-mamp.md) |
| 2 | Запустить серверы | [docs/03-configure-mamp.md](docs/03-configure-mamp.md) |
| 3 | Создать базу данных | [docs/04-create-database.md](docs/04-create-database.md) |
| 4 | Установить WordPress | [docs/05-install-wordpress.md](docs/05-install-wordpress.md) |
| 5 | Открыть сайт | [docs/06-first-launch.md](docs/06-first-launch.md) |

Перед началом рекомендуем прочитать раздел [Подготовка](docs/01-prerequisites.md) — там системные требования и полезные ссылки.

---

## Что понадобится

- **macOS** 12 Monterey или новее (Apple Silicon или Intel)
- **~500 МБ** свободного места на диске
- **Браузер** (Safari, Chrome, Firefox — любой)
- **Интернет** — только для скачивания MAMP и WordPress

---

## Как устроен процесс

```mermaid
flowchart LR
    subgraph prep [Подготовка]
        A[Скачать MAMP]
        B[Скачать WordPress]
    end
    subgraph mamp [MAMP]
        C[Установить MAMP]
        D[Запустить Apache + MySQL]
    end
    subgraph db [База данных]
        E[phpMyAdmin]
        F[Создать БД]
    end
    subgraph wp [WordPress]
        G[Распаковать в htdocs]
        H[wp-config.php]
        I[Мастер установки]
    end
    A --> C --> D
    D --> E --> F
    B --> G --> H --> I
    F --> H
    I --> J[Сайт работает]
```

---

## Оглавление

| № | Раздел | Описание |
|---|--------|----------|
| 01 | [Подготовка](docs/01-prerequisites.md) | Системные требования, что такое MAMP и WordPress |
| 02 | [Установка MAMP](docs/02-install-mamp.md) | Скачивание и установка MAMP Free |
| 03 | [Настройка MAMP](docs/03-configure-mamp.md) | Запуск серверов, порты, папка htdocs |
| 04 | [База данных](docs/04-create-database.md) | Создание БД через phpMyAdmin |
| 05 | [Установка WordPress](docs/05-install-wordpress.md) | Распаковка файлов, wp-config, мастер установки |
| 06 | [Первый запуск](docs/06-first-launch.md) | Открытие сайта и вход в админку |
| 99 | [Решение проблем](docs/99-troubleshooting.md) | Частые ошибки и их исправление |

---

## Важные параметры MAMP

Эти значения используются на протяжении всего гайда — сохраните их под рукой:

| Параметр | Значение |
|----------|----------|
| Apache (веб-сервер) | `http://localhost:8888` |
| MySQL (база данных) | порт `8889` |
| phpMyAdmin | `http://localhost:8888/phpMyAdmin/` |
| Папка сайтов (htdocs) | `/Applications/MAMP/htdocs/` |
| Логин MySQL | `root` |
| Пароль MySQL | `root` |
| Database Host в WordPress | `localhost:8889` |

> **Важно:** в WordPress указывайте `localhost:8889`, а не просто `localhost` — иначе подключение к базе не сработает.

---

## Частые проблемы

Столкнулись с ошибкой? Загляните в [docs/99-troubleshooting.md](docs/99-troubleshooting.md) — там собраны типичные ситуации и их решения.

---

## Лицензия

MIT — см. [LICENSE](LICENSE).
