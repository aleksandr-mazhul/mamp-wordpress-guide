# 03. Установка WordPress на хостинге

Вы здесь: [Часть 3](README.md) · **Шаг 3 из 4** · [← Назад](02-database.md) · [Далее →](04-launch.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

### Скачать и загрузить WordPress

1. На Mac скачайте WordPress: [ru.wordpress.org/download](https://ru.wordpress.org/download/)
2. Распакуйте ZIP — внутри папка `wordpress` с файлами
3. Снова **сожмите** содержимое `wordpress` в один ZIP (или сожмите саму папку)
4. Панель → **File Manager** → корень сайта (`public_html`)
5. **Upload** → выберите ZIP → дождитесь 100%
6. **Extract** / **Распаковать**
7. Убедитесь: в `public_html` лежит `index.php` (не вложенная `wordpress/wordpress/`)

### Мастер установки в браузере

8. Откройте **URL вашего сайта** (из [шага 1](01-account.md))
9. Выберите язык **Русский** → **Продолжить**
10. **Вперёд!** → форма базы данных:

| Поле | Значение |
|------|----------|
| Имя базы данных | DB_NAME из [шага 2](02-database.md) |
| Имя пользователя | DB_USER |
| Пароль | DB_PASSWORD |
| Сервер базы данных | DB_HOST |
| Префикс таблиц | `wp_` |

11. **Отправить** → **Запустить установку**
12. Заполните название сайта, **логин администратора**, пароль, email
13. **Установить WordPress**

<!-- TODO: скриншоты -->
<!-- ![Мастер установки](../../assets/images/hosting/03-wordpress/wp-install-wizard.png) -->

**Проверка:** экран «Поздравляем!» или кнопка **Войти**.

---

## Пояснение

<details>
<summary>Отличие от Части 1 (MAMP)</summary>

Тот же мастер WordPress, но файлы на **сервере хостинга**, а данные БД — из панели, не `root`/`root`.
</details>

<details>
<summary>Лишняя папка wordpress</summary>

Если URL стал `http://домен.com/wordpress/` — переместите файлы из `wordpress/` в `public_html/`.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Ошибка соединения с БД | [troubleshooting.md#db-connection](troubleshooting.md#db-connection) |
| 404 на сайте | [troubleshooting.md#page-404](troubleshooting.md#page-404) |

---

**[Далее: шаг 4 — первый запуск →](04-launch.md)**
