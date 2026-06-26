# WordPress на macOS: локально и в интернете

![macOS](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white)
![MAMP Free](https://img.shields.io/badge/MAMP-Free-3D8FC6?style=flat)
![WordPress](https://img.shields.io/badge/WordPress-21759B?style=flat&logo=wordpress&logoColor=white)

Открытый пошаговый гид на русском: WordPress на Mac, перенос на хостинг или установка сразу в интернете.

![WordPress установлен](assets/images/local/06-first-launch/wp-install-success.png)

---

## С чего начать

Выберите **один** путь — дальше гайд ведёт по шагам, как по дереву:

```mermaid
flowchart TD
    root[Вы здесь]
    root --> q1{Что нужно?}
    q1 -->|Учусь на Mac| L[Часть 1 Local]
    q1 -->|Сайт на localhost| M[Часть 2 Migrate]
    q1 -->|Сразу в интернет| H[Часть 3 Hosting]
```

| Ваша ситуация | Куда | Время |
|---------------|------|-------|
| **Нет сайта, учусь на Mac** | **[→ Часть 1: Local](docs/local/README.md)** | ~30 мин |
| **Сайт на localhost, выкладываю** | **[→ Часть 2: Migrate](docs/migrate/README.md)** | ~45 мин |
| **Сразу на хостинг, без MAMP** | **[→ Часть 3: Hosting](docs/hosting/README.md)** | ~30 мин |

Полный указатель шагов: **[docs/README.md](docs/README.md)**

Ошибки и альтернативные способы (FTP, плагин) — в **README каждой части**.

---

## Что это

Документация с чеклистами и скриншотами — не код сайта.

| Часть | Суть |
|-------|------|
| **Local** | WordPress на Mac (MAMP) |
| **Migrate** | Перенос готового localhost-сайта на хостинг |
| **Hosting** | WordPress с нуля на хостинге |

---

## Кому подходит

Новички на **macOS**, русский язык, бесплатный стек (MAMP + учебный хостинг). Опыт кода не нужен.

---

## Структура репозитория

```
docs/local/     — 3 шага + troubleshooting
docs/migrate/   — 6 шагов + appendix (FTP, плагин) + troubleshooting
docs/hosting/   — 4 шага + troubleshooting
```

---

## Как устроен гайд

В каждом шаге: **Сделайте** → **Проверка** → пояснения в `<details>` → ссылка на troubleshooting.

В шапке: `Шаг N из M` и кнопки **← Назад** / **Далее →**.

---

## Участие

[CONTRIBUTING.md](CONTRIBUTING.md) · [LICENSE](LICENSE)
