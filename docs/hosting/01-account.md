# 01. Аккаунт и панель хостинга

Вы здесь: [Часть 3](README.md) · **Шаг 1 из 4** · [Далее →](02-database.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

> Подробная версия тех же шагов — в [migrate/02-hosting](../migrate/02-hosting.md). Ниже — краткий путь для установки с нуля.

### Регистрация

1. Откройте сайт хостинга: [InfinityFree](https://www.infinityfree.com/) или [AwardSpace](https://www.awardspace.com/)
2. **Sign Up** / **Регистрация** → email, пароль → подтвердите email (если просят)
3. **Login** / **Вход** → панель управления (vPanel, cPanel и т.д.)
4. Создайте сайт, если панель просит: выберите субдомен (например `mysite.infinityfreeapp.com`)

### Запишите и найдите разделы

5. Запишите **URL сайта** (домен / субдомен)
6. Найдите в панели (пока не создавайте БД):
   - **MySQL Databases**
   - **File Manager**
   - **phpMyAdmin**

| Поле | Ваше значение |
|------|----------------|
| URL сайта | |
| Логин панели | |
| Пароль панели | |

<!-- TODO: скриншот -->
<!-- ![Панель хостинга](../../assets/images/hosting/01-account/panel-overview.png) -->

**Проверка:** вы в панели, знаете адрес сайта и где MySQL / File Manager.

---

## Пояснение

<details>
<summary>Зачем бесплатный хостинг для учёбы</summary>

Подходит для тестов. Для серьёзного проекта позже выберете платный тариф — алгоритм установки тот же.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Не вижу разделов | [migrate/troubleshooting.md#panel-sections](../migrate/troubleshooting.md#panel-sections) |

---

**[Далее: шаг 2 — база данных →](02-database.md)**
