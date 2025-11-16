# Usa imagem oficial do Python 3.10
FROM python:3.10-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta que o Render usa
EXPOSE 10000

# Comando para iniciar a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
