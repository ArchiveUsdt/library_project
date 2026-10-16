# Читальня — онлайн-библиотека (учебный проект)

Каталог книг на Django: список, детальная страница, добавление/изменение/удаление, поиск, фильтры, загрузка обложек, админ-панель и JSON API.
**Стек:** Python 3.10+, Django 4.2+, SQLite, Pillow, HTML/CSS/JavaScript без фреймворков.

## Структура и модули курса
| Модуль | Где в проекте |
|---|---|
| 1. Frontend-прототип | `prototype/` — 4 связанные страницы, `css/`, `js/`, `images/`. Открыть `prototype/index.html` в браузере |
| 2. Django + шаблоны | `config/`, `library/urls.py`, `templates/base.html` (extends/block), `templates/includes/` (header, footer, карточка), `static/` |
| 3. ORM, формы, admin, media | `library/models.py`, `forms.py`, `admin.py`, `migrations/`, `media/covers/` |
| 4. Итог + API | поиск/фильтр/сортировка в `views.filter_books`, API в `views.api_*` |

## Установка и запуск
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed           # тестовые данные
python manage.py createsuperuser
python manage.py runserver
```
Если `migrate` сообщает об изменениях в моделях — выполните `python manage.py makemigrations` и повторите `migrate`.

## Основные URL
`/` главная · `/books/` каталог (`?q=`, `?category=<id>`, `?sort=new|title|year`) · `/books/<id>/` книга · `/books/add/` · `/books/<id>/edit/` · `/contacts/` · `/admin/` · `/api/books/`

## Схема моделей
`Author 1—N Book N—1 Category`. Book: title, author (FK, CASCADE), category (FK, SET_NULL), year, description, cover (ImageField), created_at.

## API (только GET, JSON)
- `GET /api/books/` → `{"count": 6, "results": [{"id":1,"title":"…","author":"…","category":"Роман","year":1869,"description":"…","cover":null}]}`. Параметры `q`, `category`, `sort`.
- `GET /api/books/1/` → объект книги.
- Ошибки: `400` (неверный `category` или `sort`), `404` (нет книги), `405` (не GET), тело `{"error": "…"}`.
```bash
curl "http://127.0.0.1:8000/api/books/?q=война&sort=year"
curl -i http://127.0.0.1:8000/api/books/999/
```

