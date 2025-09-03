FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install typing-extensions==4.12.2 && pip install --no-cache-dir torch==2.7.1+cpu --index-url https://download.pytorch.org/whl/cpu && pip install --no-cache-dir -r requirements.txt && python -m spacy download ru_core_news_sm

RUN mkdir -p /app/e5smallv2
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/e5-small-v2').save('/app/e5smallv2')"

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]