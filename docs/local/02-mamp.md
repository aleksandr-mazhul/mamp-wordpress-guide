# 02. MAMP: установка и настройка

[← Подготовка](01-before.md) | [Часть 1](README.md) | [Далее: WordPress →](03-wordpress.md)

---

## Сделайте

### Установка

1. Откройте `MAMP_*.pkg` → **Продолжить** → **Принимаю** → **Установить** → введите пароль Mac
2. Запустите **MAMP** из Программ (не MAMP PRO)
3. Если macOS блокирует: **Системные настройки** → **Конфиденциальность и безопасность** → **Всё равно открыть**

### Настройка

4. В главном окне выберите **Apache** (не Nginx)
5. **Preferences** → **Ports** → Apache `80`, MySQL `3306` (или кнопка **80 & 3306**) → **OK**
6. **Preferences** → **Server** → MySQL 8.0 → **Open in Finder** → запомните путь `/Applications/MAMP/htdocs/`

![Главное окно MAMP](../../assets/images/local/03-configure-mamp/mamp-main-window.png)

![Настройка портов](../../assets/images/local/03-configure-mamp/mamp-ports-settings.png)

![Папка htdocs](../../assets/images/local/03-configure-mamp/mamp-server-htdocs.png)

**Проверка:** окно MAMP открыто, Apache выбран, порты `80` / `3306`, папка htdocs найдена. **Start пока не нажимайте** — это в следующем шаге.

```mermaid
flowchart LR
    subgraph before [Было по умолчанию]
        A1[Apache 8888]
        M1[MySQL 8889]
    end
    subgraph after [Наши порты]
        A2[Apache 80]
        M2[MySQL 3306]
    end
    before --> after
```

---

## Пояснение

<details>
<summary>Зачем Apache, а не Nginx</summary>

WordPress использует `.htaccess` для красивых ссылок (ЧПУ). Apache понимает его без дополнительной настройки. Nginx для локальной разработки WP не используем.
</details>

<details>
<summary>Зачем порт 80</summary>

С портом `80` адрес чистый: `http://localhost/папка/` вместо `http://localhost:8888/папка/`. Порт 80 может запросить пароль администратора Mac — это нормально для портов ниже 1024.
</details>

<details>
<summary>Версия PHP</summary>

Оставьте PHP по умолчанию в MAMP — она совместима с WordPress. Менять без причины не нужно.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| Порт 80 занят | [troubleshooting.md#port-80-занят](troubleshooting.md#port-80-занят) |
| Порт 3306 занят | [troubleshooting.md#порт-3306-занят](troubleshooting.md#порт-3306-занят) |
| Apache не стартует | [troubleshooting.md#apache-не-стартует](troubleshooting.md#apache-не-стартует) |

---

[Далее: WordPress →](03-wordpress.md)
