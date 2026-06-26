# 05. wp-config и замена URL

Вы здесь: [Часть 2](README.md) · **Шаг 5 из 6** · [← Назад](04-database.md) · [Далее →](06-check.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

### Часть A. wp-config.php на сервере

1. Панель → **File Manager** → корень сайта (`public_html`)
2. Найдите файл **`wp-config.php`**
3. Правый клик → **Edit** / **Редактировать** / **Code Editor**
4. Найдите строки `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`
5. Замените значения на данные из [шага 4](04-database.md):

```php
define( 'DB_NAME', 'имя_базы_на_хостинге' );
define( 'DB_USER', 'пользователь_базы' );
define( 'DB_PASSWORD', 'пароль_базы' );
define( 'DB_HOST', 'значение_из_панели' );
```

6. **Save** / **Сохранить**
7. Откройте в браузере адрес сайта с [шага 2](02-hosting.md)

<!-- TODO: скриншот -->
<!-- ![Редактирование wp-config](../../assets/images/migrate/05-configure/edit-wp-config.png) -->

### Часть B. Замена URL (localhost → домен)

8. Снова откройте `wp-config.php` на сервере
9. **Перед** строкой `/* That's all, stop editing! Happy publishing. */` добавьте (ваш домен):

```php
define( 'WP_HOME', 'http://ваш-домен-хостинга.com' );
define( 'WP_SITEURL', 'http://ваш-домен-хостинга.com' );
```

10. Сохраните файл
11. Браузер → `http://ваш-домен-хостинга.com/wp-admin/`
12. Войдите — **логин и пароль те же**, что задавали на Mac при установке WordPress
13. В админке: **Плагины** → **Добавить новый**
14. В поиске: **Better Search Replace** → **Установить** → **Активировать**
15. Слева: **Инструменты** → **Better Search Replace**
16. Заполните:
    - **Search for:** `http://localhost/название-вашей-папки` (как записали в [шаге 1](01-prepare.md))
    - **Replace with:** `http://ваш-домен-хостинга.com`
    - Отметьте **все таблицы**
    - **Run Search/Replace**
17. Вернитесь в `wp-config.php` → **удалите** строки `WP_HOME` и `WP_SITEURL` → сохраните
18. **Настройки** → **Постоянные ссылки** → **Сохранить изменения** (ничего не меняя)

**Проверка:** сайт открывается по домену хостинга, не уводит на `localhost`.

```mermaid
flowchart LR
    OLD["localhost/папка"] -->|Better Search Replace| NEW["домен хостинга"]
```

---

## Пояснение

<details>
<summary>Зачем Better Search Replace</summary>

В базе «зашит» старый адрес. Грубая замена текста в `.sql` может сломать данные — плагин делает это безопасно.
</details>

<details>
<summary>HTTPS</summary>

Если сайт с SSL — везде `https://` вместо `http://`, включая Search Replace и **Настройки** → **Общие**.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Ошибка соединения с БД | [troubleshooting.md#db-connection](troubleshooting.md#db-connection) |
| Редирект на localhost | [troubleshooting.md#localhost-redirect](troubleshooting.md#localhost-redirect) |
| Битые картинки | Повторите Search Replace; проверьте `wp-content/uploads` |

---

**[Далее: шаг 6 — финальная проверка →](06-check.md)**
