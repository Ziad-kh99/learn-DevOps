FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port (Gunicorn will run here)
EXPOSE 8000

# Run with Gunicorn (production-ready WSGI server)
CMD ["gunicorn", "weather_app.wsgi:application", "--bind", "0.0.0.0:8000"]
