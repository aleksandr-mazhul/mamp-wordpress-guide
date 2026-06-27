# 03. Установка WordPress на хостинге

Вы здесь: [Часть 3](README.md) · **Шаг 3 из 4** · [← Назад](02-database.md) · [Далее →](04-launch.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

### Файлы на сервер

1. Скачайте [WordPress на русском](https://ru.wordpress.org/download/) — архив `wordpress-x.x.x-ru_RU.zip`
2. Панель → **File Manager** → `public_html`
3. **Upload** → выберите ZIP → **Extract** / **Распаковать**
4. Если файлы оказались в `public_html/wordpress/` — **переместите содержимое** в `public_html/` (должен лежать `index.php` в корне)

### Мастер установки

5. Браузер → **URL сайта** ([шаг 1](01-account.md))
6. Язык **Русский** → **Продолжить** → **Вперёд!**
7. База данных — значения из [шага 2](02-database.md):

| Поле | Значение |
|------|----------|
| Имя базы | DB_NAME |
| Пользователь | DB_USER |
| Пароль | DB_PASSWORD |
| Сервер | DB_HOST |
| Префикс | `wp_` |

8. **Отправить** → **Запустить установку**
9. Название сайта, логин, пароль, email → **Установить WordPress**

<!-- TODO: скрин wp-install-wizard.png в assets/images/hosting/03-wordpress/ -->

**Проверка:** экран «Поздравляем!» или кнопка **Войти**.

---

## Пояснение

<details>
<summary>Отличие от Части 1</summary>

Тот же мастер WordPress, но файлы на сервере хостинга, а БД — из панели (не `root`/`root` с MAMP).
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Ошибка БД | [migrate/troubleshooting.md#db-connection](../migrate/troubleshooting.md#db-connection) |
| 404 | [migrate/troubleshooting.md#permalinks-404](../migrate/troubleshooting.md#permalinks-404) |

---

**[Далее: шаг 4 →](04-launch.md)**
