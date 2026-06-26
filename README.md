# WordPress на macOS: локально и в интернете

![macOS](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white)
![MAMP Free](https://img.shields.io/badge/MAMP-Free-3D8FC6?style=flat)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)

> Два пошаговых гайда: поднять WordPress на Mac через MAMP и перенести готовый сайт на хостинг.

---

## Часть 1: Локальная установка (MAMP)

Установите WordPress на Mac — без хостинга и домена. Всё работает через **MAMP Free**.

![WordPress установлен](assets/images/06-first-launch/wp-install-success.png)

| Шаг | Действие | Раздел |
|-----|----------|--------|
| 1 | Скачать MAMP и WordPress | [docs/01-prerequisites.md](docs/01-prerequisites.md) |
| 2 | Установить MAMP | [docs/02-install-mamp.md](docs/02-install-mamp.md) |
| 3 | Настроить MAMP (Apache, порты, htdocs) | [docs/03-configure-mamp.md](docs/03-configure-mamp.md) |
| 4 | Создать базу данных | [docs/04-create-database.md](docs/04-create-database.md) |
| 5 | Установить WordPress | [docs/05-install-wordpress.md](docs/05-install-wordpress.md) |
| 6 | Войти в админку | [docs/06-first-launch.md](docs/06-first-launch.md) |

**Проблемы с MAMP:** [docs/99-troubleshooting.md](docs/99-troubleshooting.md)

---

## Часть 2: Перенос на хостинг

Перенесите **уже готовый** локальный сайт в интернет — универсальный ручной алгоритм + альтернатива через плагин.

**[Начать часть 2 →](docs/deploy/README.md)**

| Шаг | Действие | Раздел |
|-----|----------|--------|
| 1 | Подготовка | [docs/deploy/01-prerequisites.md](docs/deploy/01-prerequisites.md) |
| 2 | Выбор хостинга | [docs/deploy/02-choose-hosting.md](docs/deploy/02-choose-hosting.md) |
| 3 | Бэкап локального сайта | [docs/deploy/03-backup-local.md](docs/deploy/03-backup-local.md) |
| 4 | Экспорт базы данных | [docs/deploy/04-export-database.md](docs/deploy/04-export-database.md) |
| 5 | Загрузка файлов | [docs/deploy/05-upload-files.md](docs/deploy/05-upload-files.md) |
| 6 | База на хостинге | [docs/deploy/06-create-remote-database.md](docs/deploy/06-create-remote-database.md) |
| 7 | Импорт SQL | [docs/deploy/07-import-database.md](docs/deploy/07-import-database.md) |
| 8 | wp-config и замена URL | [docs/deploy/08-wp-config-and-urls.md](docs/deploy/08-wp-config-and-urls.md) |
| 9 | Финальная проверка | [docs/deploy/09-final-check.md](docs/deploy/09-final-check.md) |

**Альтернатива (плагин):** [docs/deploy/10-alternative-plugin.md](docs/deploy/10-alternative-plugin.md)

**Проблемы при переносе:** [docs/deploy/99-troubleshooting.md](docs/deploy/99-troubleshooting.md)

---

## Часть 3 (планируется)

Установка WordPress **сразу на хостинге** без MAMP — отдельный гайд.

---

## Видеоматериал (часть 1)

**[Установка WordPress на MAMP (YouTube)](https://www.youtube.com/watch?v=OwnwrO6Ub28&t=1s)**

> В видео порты могут отличаться (`8888` / `8889`) — в части 1 используются **`80`** и **`3306`**.

---

## Параметры локальной установки (часть 1)

| Параметр | Значение |
|----------|----------|
| Сайт | `http://localhost/название-вашей-папки/` |
| Apache | порт `80` |
| MySQL | порт `3306` |
| phpMyAdmin | `http://localhost/phpMyAdmin/` |
| htdocs | `/Applications/MAMP/htdocs/` |
| MySQL | `root` / `root` |

---

## Лицензия

MIT — см. [LICENSE](LICENSE).
