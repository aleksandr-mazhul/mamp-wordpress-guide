# Приложение: загрузка через FTP (FileZilla)

[← Часть 2](README.md)

Основной путь — **File Manager + ZIP** ([02-upload-and-db.md](02-upload-and-db.md)). FTP — если файловый менеджер неудобен или ZIP не принимают.

---

## Сделайте

1. Скачайте [FileZilla Client](https://filezilla-project.org/)
2. В панели хостинга найдите FTP-данные: хост, логин, пароль, порт (обычно `21`)
3. FileZilla → заполните поля → **Быстрое соединение**
4. **Слева** — Mac, папка сайта в `htdocs`
5. **Справа** — сервер, `public_html` (или аналог)
6. Выделите все файлы слева → перетащите направо
7. Дождитесь окончания очереди (10–30 минут)

**Проверка:** на сервере в корне сайта лежит `index.php`, папки `wp-admin`, `wp-content`, `wp-includes`.

---

## Пояснение

<details>
<summary>FTP vs ZIP</summary>

ZIP через File Manager обычно быстрее — одна загрузка вместо тысяч мелких файлов.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Connection timeout | Проверьте хост, порт, файрвол |
| Login incorrect | Логин/пароль из раздела FTP, не от панели |
| Пассивный режим | FileZilla: Правка → Настройки → FTP → Passive |

Подробнее: [troubleshooting.md#ftp-filezilla](troubleshooting.md#ftp-filezilla)

---

[← Часть 2](README.md)
