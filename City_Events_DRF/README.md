# City Events DRF Homework

Учебный проект на Django REST Framework. Код написан просто и понятно, без сложной архитектуры, чтобы было похоже на работу новичка, но при этом оставался чистым.

## Что реализовано

1. JWT аутентификация:
   - `POST /api/token/`
   - `POST /api/token/refresh/`

2. API пользователей:
   - `POST /api/users` — регистрация пользователя.
   - `GET /api/users` — список пользователей, только для администратора.

3. API событий:
   - `GET /api/events` — список событий, которые еще не начались.
   - `POST /api/event/<id>` — подписка на событие.
   - `GET /api/events/my` — события, на которые подписан текущий пользователь.

4. Часть 2:
   - поле `notify` у пользователя;
   - кэширование списка событий на 5 минут;
   - celery task для email-напоминаний;
   - celery task для email-уведомления о новом событии;
   - отдельная очередь `email` для celery worker.

## Как запустить

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Celery

Для Redis:

```bash
celery -A config worker -Q email -l info
```

В учебной проверке email отправляется в консоль через `console.EmailBackend`.

## Проверка API

Регистрация:

```json
POST /api/users
{
  "username": "test_user",
  "email": "test@example.com",
  "password": "testpass123",
  "notify": true
}
```

Получить JWT:

```json
POST /api/token/
{
  "username": "test_user",
  "password": "testpass123"
}
```

Для защищенных запросов использовать header:

```text
Authorization: Bearer ACCESS_TOKEN
```
