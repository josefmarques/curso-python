FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema para compilar o psycopg2 e netcat (healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Dá permissão de execução ao entrypoint
RUN chmod +x entrypoint.sh

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando de entrada que executa migrações e inicia o servidor
CMD ["/bin/bash", "entrypoint.sh"]
