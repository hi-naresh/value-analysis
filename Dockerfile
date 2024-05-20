FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10.14

COPY src /app

RUN pip install --no-cache-dir -r /src/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
