# 03. Загрузка файлов на сервер

Вы здесь: [Часть 2](README.md) · **Шаг 3 из 6** · [← Назад](02-hosting.md) · [Далее →](04-database.md)  
Если ошибка → [troubleshooting.md](troubleshooting.md)

---

## Выбор способа загрузки

| Способ | Когда |
|--------|-------|
| **File Manager + ZIP** (ниже) | Рекомендуем — проще для первого раза |
| **FTP (FileZilla)** | [appendix-ftp.md](appendix-ftp.md) — если менеджер неудобен или ZIP не принимают |

Дальше — **основной путь** через File Manager.

---

## Сделайте

### Подготовка ZIP на Mac

1. Откройте `/Applications/MAMP/htdocs/`
2. Правый клик по **папке вашего сайта** → **Сжать «…»**
3. Появится `название-папки.zip` — запомните, где лежит (обычно рядом с папкой)

### Загрузка в панели хостинга

4. Войдите в **панель хостинга** (как на [шаге 2](02-hosting.md))
5. Откройте **File Manager** / **Файловый менеджер**
6. Слева перейдите в корень сайта:
   - чаще всего `public_html`
   - или `htdocs`, `www`, `domains/ваш-домен/public_html`
7. Нажмите **Upload** / **Загрузить**
8. Выберите ZIP с Mac → дождитесь **100%**
9. В списке файлов найдите ZIP → правый клик → **Extract** / **Распаковать** / **Unzip**
10. Убедитесь: в корне лежит **`index.php`**, папки `wp-admin`, `wp-content`, `wp-includes`
11. (Опционально) Удалите ZIP с сервера

<!-- TODO: скриншот -->
<!-- ![File Manager — загрузка ZIP](../../assets/images/migrate/03-upload/file-manager-upload.png) -->

**Проверка:** в `public_html` (или аналоге) есть `index.php` **напрямую**, не в `public_html/wordpress/wordpress/`.

---

## Пояснение

<details>
<summary>Частая ошибка — лишняя вложенность</summary>

Если распаковали так, что сайт открывается только как `http://домен.com/wordpress/` — переместите **содержимое** папки `wordpress` на уровень выше в `public_html`.
</details>

<details>
<summary>ZIP быстрее FTP</summary>

Одна загрузка архива обычно быстрее, чем тысячи мелких файлов по FTP.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Сайт в подпапке `/wordpress/` | Переместите файлы на уровень выше |
| Upload обрывается | Меньший ZIP или [appendix-ftp](appendix-ftp.md) |
| Не вижу File Manager | [troubleshooting.md#panel-sections](troubleshooting.md#panel-sections) |

---

**[Далее: шаг 4 — база данных и импорт SQL →](04-database.md)**
