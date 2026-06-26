# 02. База данных на хостинге

Вы здесь: [Часть 3](README.md) · **Шаг 2 из 4** · [← Назад](01-account.md) · [Далее →](03-wordpress.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

> Здесь создаём **пустую** базу. Импорт SQL с Mac **не нужен** — это не перенос ([Часть 2](../migrate/README.md)).

1. Панель → **MySQL Databases** / **Базы данных**
2. **Create Database** → имя латиницей (например `my_wp_db`) → **Create**
3. **Скопируйте полное имя** базы из панели
4. **Create User** → логин + пароль → **Create** → **запишите**
5. **Add User to Database** → все привилегии (**ALL PRIVILEGES**) → **Save**
6. Найдите **DB_HOST** в блоке Database details / Сведения о БД

| Поле | Ваше значение |
|------|----------------|
| DB_NAME | |
| DB_USER | |
| DB_PASSWORD | |
| DB_HOST | |

<!-- TODO: скриншот -->
<!-- ![Создание базы](../../assets/images/hosting/02-database/create-database.png) -->

**Проверка:** база создана, таблиц `wp_*` **ещё нет** (пустая) — их создаст мастер WordPress на следующем шаге.

---

## Пояснение

<details>
<summary>DB_HOST не всегда localhost</summary>

Копируйте значение из панели хостинга, не из памяти про MAMP.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Не создаётся база | [troubleshooting.md#db-connection](troubleshooting.md#db-connection) |

---

**[Далее: шаг 3 — установка WordPress →](03-wordpress.md)**
