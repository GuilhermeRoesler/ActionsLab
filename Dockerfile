# Imagem mínima usada no job de build do CI (demonstração pedagógica).
# Não é o alvo de deploy — o CD publica o site estático em GitHub Pages.
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY calculadora.py pyproject.toml ./
COPY tests/ ./tests/

CMD ["pytest", "--verbose"]
