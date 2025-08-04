# Flask Blog API

## Запуск приложения

1. Создать виртуальное окружение:

```bash
python3 -m venv myenv
```

2. Активировать виртуальное окружение:

```bash
source myenv/bin/activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Запустить приложение:

```bash
python main.py
```

## Request Examples

GET: http://127.0.0.1:5000/ping (healthcheck, no request body)
GET: http://127.0.0.1:5000/blogpost (no request body)
POST: http://127.0.0.1:5000/blogpost

```json
{ "body": "hi", "author": "me" }
```

PUT: http://127.0.0.1:5000/blogpost/0

```json
{ "body": "updated post", "author": "new-me" }
```

DELETE: http://127.0.0.1:5000/blogpost/0 (no request body)

Если поста не существует (неверный `post_id`):

Ответ:

```json
{
  "error": "Blog post not found"
}
```

HTTP статус: 404
