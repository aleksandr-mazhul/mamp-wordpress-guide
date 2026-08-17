# Решение проблем (хостинг)

[← Часть 3](README.md)

Типовые проблемы при установке WordPress на хостинге. Перенос с Mac — см. [Часть 2](../migrate/troubleshooting.md).

---

<a id="panel-sections"></a>

## Не нахожу раздел в панели хостинга

**Симптом:** нет MySQL Databases, File Manager или phpMyAdmin.

**Решение:**

1. Ищите похожие названия на русском и английском
2. Раздел может называться **Databases**, **Files**, **Website** → **Manage**
3. На бесплатных хостингах phpMyAdmin — кнопка рядом с созданной базой
4. Поиск по панели (иконка лупы): `mysql`, `file`, `phpmyadmin`

---

<a id="db-connection"></a>

## Error establishing a database connection

Проверьте `wp-config.php` на сервере:

| Поле | Частая ошибка |
|------|----------------|
| DB_NAME | Не полное имя из панели |
| DB_USER | Не тот пользователь |
| DB_PASSWORD | Опечатка |
| DB_HOST | `localhost` по привычке с MAMP — **возьмите из панели** |

---

<a id="permalinks-404"></a>

## 404 на всех страницах кроме главной

1. Настройки → Постоянные ссылки → **Сохранить**
2. Проверьте `.htaccess` в корне сайта

---

<a id="white-screen"></a>

## Белый экран

1. `WP_DEBUG` и `WP_DEBUG_DISPLAY` в `wp-config.php`
2. Переименуйте папку плагина в `wp-content/plugins/`
3. Логи в панели хостинга (Error Log)

---

<a id="error-500"></a>

## 500 Internal Server Error

- Переименуйте `.htaccess` → `.htaccess.bak` → Постоянные ссылки → Сохранить
- PHP 8.0+ в панели хостинга
- Права: папки `755`, файлы `644`

---

[← Часть 3](README.md)
