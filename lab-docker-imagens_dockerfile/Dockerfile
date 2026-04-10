FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 5000

# comando que liga a aplicação quando o container inicia
CMD ["python", "app.py"]