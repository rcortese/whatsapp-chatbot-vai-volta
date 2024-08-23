# Use uma imagem base do Python
FROM python:3.12.5-slim

# Copie o arquivo requirements.txt para o container
COPY requirements.txt /app/requirements.txt

# Instale as dependências necessárias
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copie o código e o arquivo .env para o container
COPY . /app
WORKDIR /app

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
