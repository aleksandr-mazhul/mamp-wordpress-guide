# 01. Подготовка

[← Часть 1](README.md) | [Далее: MAMP →](02-mamp.md)

---

## Сделайте

1. Проверьте систему: macOS 12+, ~500 МБ свободного места, интернет для скачивания
2. Скачайте **MAMP Free**: [mamp.info/ru/downloads](https://www.mamp.info/ru/downloads/) (блок **MAMP**, не PRO)
3. Скачайте **WordPress** на русском: [ru.wordpress.org/download](https://ru.wordpress.org/download/) — сохраните `wordpress-x.x.x-ru_RU.zip`
4. (Опционально) Посмотрите видео: [YouTube](https://www.youtube.com/watch?v=OwnwrO6Ub28&t=1s)

**Проверка:** на диске два файла — установщик MAMP (`.pkg`) и архив WordPress (`.zip`).

---

## Пояснение

<details>
<summary>Зачем это нужно</summary>

**MAMP** (Mac, Apache, MySQL, PHP) превращает Mac в локальный веб-сервер. WordPress — файлы сайта + база данных MySQL. Скачиваем оба компонента заранее, чтобы дальше не отвлекаться.

Скачивайте только с официальных сайтов — сторонние «сборки» могут быть опасны.
</details>

<details>
<summary>Локально vs хостинг</summary>

| | Локально (MAMP) | На хостинге |
|---|-----------------|-------------|
| Доступ | Только с вашего Mac | Из интернета |
| Стоимость | Бесплатно | Обычно платно |
| Для чего | Обучение, разработка | Публичный сайт |
</details>

<details>
<summary>Про видео и порты</summary>

В видео могут быть порты `8888` / `8889`. В этом гайде — **`80`** и **`3306`**. При расхождении ориентируйтесь на текст.
</details>

---

## Если ошибка

| Симптом | Куда |
|---------|------|
| macOS блокирует MAMP | [troubleshooting.md#apache-wont-start](troubleshooting.md#apache-wont-start) |

---

[Далее: MAMP →](02-mamp.md)
