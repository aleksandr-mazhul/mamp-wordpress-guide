# 04. Первый запуск и настройка

Вы здесь: [Часть 3](README.md) · **Шаг 4 из 4** · [← Назад](03-wordpress.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

1. Откройте `http://ваш-домен-хостинга.com/wp-admin/`
2. Войдите логином и паролем с [шага 3](03-wordpress.md)
3. **Настройки** → **Постоянные ссылки** → «Название записи» → **Сохранить**
4. Запишите данные сайта:

| Что | Ваше значение |
|-----|----------------|
| URL сайта | |
| URL админки | `.../wp-admin/` |
| DB_NAME, DB_USER, DB_HOST | из шага 2 |
| Логин WordPress | |

**Проверка:** главная открывается, админка работает, ссылки на записи красивые (не `?p=123`).

---

## Пояснение

<details>
<summary>HTTPS</summary>

Если хостинг выдал SSL — в **Настройки** → **Общие** оба адреса с `https://`.
</details>

<details>
<summary>Что дальше</summary>

Темы, страницы, плагины — как в обычном WordPress. Локальную копию на Mac для этого пути не нужно.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| 404 на страницах | [migrate/troubleshooting.md#permalinks-404](../migrate/troubleshooting.md#permalinks-404) |
| Белый экран | [migrate/troubleshooting.md#white-screen](../migrate/troubleshooting.md#white-screen) |

---

## Готово

Сайт в интернете с нуля.

- Перенос с Mac → [Часть 2: Migrate](../migrate/README.md)
- [← Часть 3](README.md) · [← К оглавлению репозитория](../../README.md)
