# WordPress на macOS: локально и в интернете

![macOS](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white)
![MAMP Free](https://img.shields.io/badge/MAMP-Free-3D8FC6?style=flat)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)

Пошаговый гид на русском: WordPress на Mac, перенос на хостинг или установка сразу в интернете.

![WordPress установлен](assets/images/local/06-first-launch/wp-install-success.png)

---

## С чего начать

```mermaid
flowchart TD
    root[Вы здесь]
    root --> q{Задача?}
    q -->|Учусь на Mac| L[Часть 1]
    q -->|Сайт на localhost| M[Часть 2]
    q -->|Сразу в интернет| H[Часть 3]
```

| Ситуация | Путь | Время |
|----------|------|-------|
| Нет сайта, Mac + MAMP | **[→ Часть 1](docs/local/README.md)** | ~30 мин |
| Сайт на `localhost` | **[→ Часть 2](docs/migrate/README.md)** | ~45 мин |
| Сразу на хостинг | **[→ Часть 3](docs/hosting/README.md)** | ~30 мин |

Внутри каждой части — шаги **1 → 2 → …** с кнопками «Далее». Развилки (FTP, плагин) — в [Части 2](docs/migrate/README.md).

---

## Структура

```
docs/local/     3 шага + troubleshooting
docs/migrate/   6 шагов + appendix + troubleshooting
docs/hosting/   4 шага + troubleshooting
```

[Полный указатель](docs/README.md) · [Как дополнять гайд](CONTRIBUTING.md) · [LICENSE](LICENSE)
