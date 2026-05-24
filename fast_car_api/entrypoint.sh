#!/bin/bash
set -e

echo "=== Fast Car API - Entrypoint ==="

# Aguarda o PostgreSQL ficar disponível
echo "Aguardando PostgreSQL..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "PostgreSQL disponível!"

# Executa as migrações do Alembic
echo "Executando migrações do banco de dados..."
alembic upgrade head

# Inicia a aplicação
echo "Iniciando servidor FastAPI..."
exec uvicorn fast_car_api.app:app --host 0.0.0.0 --port 8000
