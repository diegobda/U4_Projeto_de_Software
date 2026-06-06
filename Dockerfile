FROM python:3.12-slim

WORKDIR /app

COPY calculadora_gui.py .

CMD ["python", "calculadora_gui.py"]
