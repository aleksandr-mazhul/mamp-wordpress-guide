# Приложение: загрузка через FTP (FileZilla)

**Альтернативная ветка** — вместо [шага 3](03-upload.md) (File Manager + ZIP).

[← Часть 2](README.md) · После загрузки → [шаг 4: база данных](04-database.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Сделайте

1. Скачайте [FileZilla Client](https://filezilla-project.org/) на Mac
2. Панель хостинга → **FTP Accounts** / **FTP-аккаунты** — запишите хост, логин, пароль, порт (обычно `21`)
3. Откройте FileZilla → вверху заполните поля → **Быстрое соединение**
4. **Слева:** найдите папку сайта в `/Applications/MAMP/htdocs/`
5. **Справа:** откройте `public_html` (или `htdocs` / `www`)
6. Выделите **все** файлы и папки слева → перетащите направо
7. Дождитесь окончания очереди (10–30 минут)

**Проверка:** на сервере в корне лежит `index.php`, папки `wp-admin`, `wp-content`, `wp-includes`.

---

## Пояснение

<details>
<summary>FTP vs ZIP</summary>

ZIP через File Manager обычно быстрее. FTP — запасной вариант.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Не подключается | [troubleshooting.md#ftp-filezilla](troubleshooting.md#ftp-filezilla) |

---

**[Далее: шаг 4 — база данных →](04-database.md)** · [← Часть 2](README.md)
