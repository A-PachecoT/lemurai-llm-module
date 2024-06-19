FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .

ENV GROQ_API_KEY "token"
RUN pip install --no-cache-dir -r requirements.txt


COPY lemur_core.py .
COPY lemur_service.py .

EXPOSE 8080

# Comando para ejecutar la aplicación FastAPI con Uvicorn
CMD ["uvicorn", "lemur_service:app", "--host", "0.0.0.0", "--port", "8080"]
