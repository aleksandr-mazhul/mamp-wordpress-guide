# 03. WordPress: база, установка, вход

[← MAMP](02-mamp.md) | [Часть 1](README.md)

---

## Сделайте

### База данных

1. В MAMP нажмите **Start** — Apache и MySQL зелёные
2. Откройте `http://localhost/MAMP/` → MySQL → **phpMyAdmin**

![WebStart — phpMyAdmin](../../assets/images/local/04-create-database/mamp-webstart-phpmyadmin.png)

3. Слева **New** → имя базы (например `wordpress`) → кодировка `utf8mb4_unicode_ci` → **Create**

![phpMyAdmin — New](../../assets/images/local/04-create-database/phpmyadmin-new.png)

![Создание базы](../../assets/images/local/04-create-database/create-database.png)

### Установка WordPress

4. Распакуйте `wordpress-x.x.x-ru_RU.zip`, переименуйте папку `wordpress` (латиница, без пробелов)
5. Переместите в `/Applications/MAMP/htdocs/название-вашей-папки/`
6. В браузере: `http://localhost/название-вашей-папки/` → язык **Русский**
7. **Вперёд!** → заполните БД: имя базы, пользователь `root`, пароль `root`, сервер `localhost`, префикс `wp_`
8. **Отправить** → **Запустить установку**
9. Заполните название сайта, логин, пароль, email → **Установить WordPress** → **Войти**

![Форма БД](../../assets/images/local/05-install-wordpress/wp-db-config.png)

![Запустить установку](../../assets/images/local/05-install-wordpress/wp-run-install.png)

![Данные сайта](../../assets/images/local/06-first-launch/wp-site-info.png)

![Установка завершена](../../assets/images/local/06-first-launch/wp-install-success.png)

**Проверка:** админка открывается по `http://localhost/название-вашей-папки/wp-admin/`.

```mermaid
flowchart TB
    H[htdocs/папка] --> U["http://localhost/папка/"]
    U --> WP[WordPress]
    DB[(MySQL база)] --> WP
    WP --> ADM["/wp-admin/"]
```

---

## Что записать

| Что | Ваше значение |
|-----|----------------|
| Папка | `/Applications/MAMP/htdocs/название-вашей-папки/` |
| URL сайта | `http://localhost/название-вашей-папки/` |
| Имя базы | *(как в phpMyAdmin)* |
| Логин WP | *(при установке)* |

> `root` / `root` — **только локально**. На хостинге будут другие данные.

### Полезно после установки

- **ЧПУ:** Настройки → Постоянные ссылки → «Название записи» → Сохранить
- **Следующий запуск:** MAMP → Start → открыть URL сайта

---

## Пояснение

<details>
<summary>Зачем utf8mb4</summary>

Кодировка `utf8mb4_unicode_ci` поддерживает все символы Unicode, включая эмодзи.
</details>

<details>
<summary>Имя папки = часть URL</summary>

Папка `my-blog` → адрес `http://localhost/my-blog/`. Внутри должны быть `index.php`, `wp-admin`, `wp-content`, `wp-includes`.
</details>

<details>
<summary>Про скриншот формы БД</summary>

На скриншоте в полях могут быть примеры `username` / `password` — **не копируйте**. Для MAMP: `root` / `root`.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Ошибка соединения с БД | [troubleshooting.md#db-connection](troubleshooting.md#db-connection) |
| 404 на сайте | [troubleshooting.md#page-404](troubleshooting.md#page-404) |
| phpMyAdmin не открывается | [troubleshooting.md#phpmyadmin](troubleshooting.md#phpmyadmin) |

---

## Дальше

**[Часть 2: перенос на хостинг →](../migrate/README.md)**

[← Часть 1](README.md)
