Это LLM + RAG чат-бот с интерфейсом на чистом HTML
Его суть в том, что этот бот отвечает про мои проекты, навыки и
что применялось для конкретного проекта. Данные были написаны мной
вручную, не очень подробно, к сожалению.

### Для запуска необходимо:

1. прописать HF_TOKEN в .env файле

2. установить зависимости 

```python
pip install -r requirements.txt
```

3. В папке src/build_data необходимо поместить файл data.txt , который будет содержать данные. !!! Необходимо предварительно разбить данные на чанки !!!

- [ПРОЕКТ]
- [НАВЫКИ]
- [УСЛОВИЯ РАБОТЫ]
- [КОНТАКТЫ]
- [ОПЫТ РАБОТЫ]

Пример заполнения:
```
[НАВЫКИ]
Языки: Python (Asyncio)
Web/Backend: FastAPI, aiohttp, aiogram
Базы данных: ...

[УСЛОВИЯ]
График работы: ...
Тип занятости: ...
Командировки: ...

[ПРОЕКТ]
Название: Universal Telegram Bot Platform
Технологии: aiogram, SQLite, Alembic, Requests
Описание: ...
Роль: ...
```

А после запустить *build_vector_db.py*, чтобы появилась chromaDB

4. Собрать образ Docker

Для VPS-сервера
```
docker buildx build --platform linux/amd64 -t ddrxgd/llm-app-ddrxg:amd64 .
```

```
docker buildx build -t ddrxgd/llm-app-ddrxg:latest .
```

Для запуска:
```
docker run -d --name llm-app -p 8000:8000 ddrxgd/llm-app-ddrxg:amd64
```

Готово! Проект запущен на 0.0.0.0:8000
Я использую VPS-сервер + маршрутизатор от CloudPub, он создает туннель
с публичного HTTPS урла на 0.0.0.0:8000

Сервис https://cloudpub.ru/ , он абсолютно бесплатный, есть докер образ.
Установить в докер на сервер
```
docker pull cloudpub/cloudpub:latest-arm64
```
Установить в докер локально
```
docker pull cloudpub/cloudpub
```