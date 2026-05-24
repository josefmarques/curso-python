# Fast Car API

API REST moderna para gerenciamento de veículos, construída com **FastAPI**, **SQLAlchemy** e **Pydantic**.

---

## Índice

- [Visão Geral](#vis%C3%A3o-geral)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pr%C3%A9-requisitos)
- [Como Executar](#como-executar)
  - [Com Docker](#%EF%B8%8F-opção-1--com-docker-recomendado)
  - [Local (sem Docker)](#-opção-2--local-sem-docker)
  - [MkDocs (documentação)](#-opção-3--servir-a-documentação-com-mkdocs)
- [Comandos disponíveis](#comandos-disponíveis)
- [Modelo de Dados](#modelo-de-dados)
- [Schemas (Pydantic)](#schemas-pydantic)
- [Endpoints](#endpoints)
- [Banco de Dados](#banco-de-dados)
- [Tratamento de Erros](#tratamento-de-erros)
- [Docker](#docker)
- [Documentação Interativa](#documenta%C3%A7%C3%A3o-interativa)
- [Autor](#autor)

---

## Visão Geral

A **Fast Car API** fornece uma interface REST completa para operações CRUD de veículos. O projeto foi desenvolvido com foco em boas práticas modernas, incluindo:

- Validação automática de dados com **Pydantic**
- Documentação interativa gerada automaticamente (Swagger / ReDoc)
- ORM com **SQLAlchemy** para abstração do banco de dados
- Tipagem forte em todo o código
- Formatação e lint padronizados com **Ruff**

---

## Tecnologias

| Tecnologia | Função |
|---|---|
| [Python 3.12+](https://python.org) | Linguagem de programação |
| [FastAPI](https://fastapi.tiangolo.com) | Framework web |
| [SQLAlchemy](https://www.sqlalchemy.org) | ORM (Object-Relational Mapping) |
| [Pydantic](https://docs.pydantic.dev) | Validação de dados via modelos |
| [PostgreSQL](https://postgresql.org) | Banco de dados relacional |
| [Docker](https://docker.com) | Containerização da aplicação |
| [Ruff](https://astral.sh/ruff) | Linter e formatador de código |
| [Taskipy](https://github.com/taskipy/taskipy) | Automação de tarefas |
| [Uvicorn](https://www.uvicorn.org) | Servidor ASGI |

---

## Estrutura do Projeto

```text
.
├── .dockerignore           # Arquivos ignorados pelo Docker
├── Dockerfile               # Imagem Docker da aplicação
├── entrypoint.sh            # Script de inicialização (migrações + servidor)
├── docker-compose.yaml      # Orquestração dos serviços (app + postgres + pgadmin)
├── pyproject.toml           # Configuração do projeto e ferramentas
├── requirements.txt         # Dependências Python
├── alembic.ini              # Configuração do Alembic
├── mkdocs.yml               # Configuração do MkDocs (documentação)
│
├── fast_car_api/
│   ├── __init__.py          # Torna o diretório um pacote Python
│   ├── app.py               # Ponto de entrada da aplicação FastAPI
│   ├── database.py          # Configuração da engine e sessão do SQLAlchemy
│   ├── models.py            # Modelo ORM da tabela 'cars'
│   ├── routers.py           # Definição de todas as rotas/endpoints
│   └── schemas.py           # Schemas Pydantic para validação de dados
│
├── docs/
│   └── index.md             # Documentação do projeto (este arquivo)
│
├── migrations/              # Scripts de migração do banco (Alembic)
│   ├── env.py
│   └── versions/
│
└── tests/                   # Testes automatizados
```

---

## Pré-requisitos

### Para todas as formas de execução

- Python 3.12 ou superior
- [Docker](https://docker.com) e [Docker Compose](https://docs.docker.com/compose/) (recomendado)
- [PDM](https://pdm.fming.dev) ou [pip](https://pip.pypa.io) (alternativo, sem Docker)

---

## Como Executar

### 🔵 Opção 1 — Com Docker (recomendado)

A aplicação está completamente containerizada com **Docker Compose**, orquestrando 3 serviços:

| Serviço | Imagem | Função | Porta |
|---|---|---|---|
| `app` | `fast_car_api-app` | API FastAPI | `8000` |
| `postgres` | `postgres:16` | Banco de dados relacional | `5432` |
| `pgadmin` | `dpage/pgadmin4` | Interface web para gerenciar o PostgreSQL | `5050` |

**Passos:**

```bash
# Construir a imagem e iniciar todos os serviços
docker compose up -d --build

# Verificar o status dos containers
docker compose ps

# Acompanhar os logs da aplicação
docker compose logs -f app
```

Acesse a API em: [http://localhost:8000](http://localhost:8000)

> **Nota:** O `entrypoint.sh` aguarda o PostgreSQL ficar disponível, executa as migrações do Alembic automaticamente e só então inicia o servidor.

---

### 🟢 Opção 2 — Local (sem Docker)

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/fast_car_api.git
   cd fast_car_api
   ```

2. **Crie um ambiente virtual e instale as dependências**

   Com PDM:
   ```bash
   pdm install
   ```

   Com pip:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados PostgreSQL**

   Certifique-se de ter um PostgreSQL rodando e configure a variável de ambiente:

   ```bash
   export DATABASE_URL=postgresql://zemarques:mrq831028@localhost:5432/fin-pdv
   ```

4. **Execute as migrações**

   ```bash
   alembic upgrade head
   ```

5. **Inicie o servidor de desenvolvimento**

   Com PDM:
   ```bash
   pdm run
   ```

   Ou manualmente:
   ```bash
   fastapi dev fast_car_api/app.py
   ```

   Acesse em: [http://localhost:8000](http://localhost:8000)

---

### 📘 Opção 3 — Servir a documentação com MkDocs

A documentação pode ser visualizada localmente via **MkDocs**:

```bash
mkdocs serve -a 127.0.0.1:8001
```

Acesse em: [http://127.0.0.1:8001](http://127.0.0.1:8001)

---

## Comandos disponíveis

Gerenciados via `taskipy` no `pyproject.toml`:

| Comando | Ação |
|---|---|
| `pdm run lint` | Executa o Ruff como linter |
| `pdm run lint_fix` | Executa o Ruff e aplica correções automáticas |
| `pdm run format` | Formata o código com Ruff |
| `pdm run` | Inicia o servidor FastAPI em modo dev |

---

## pyproject.toml

```toml
[project]
name = "Fast Car API"
version = "0.1.0"
description = "API moderna com FastAPI"
authors = [
  {name = "Jose Marques", email = "josemarques.moc@gmail.com"}
]
```

---

## Modelo de Dados

A tabela `cars` no banco **PostgreSQL** é definida pelo modelo ORM abaixo:

**Arquivo:** `fast_car_api/models.py`

```python
class Car(Base):
    __tablename__ = 'cars'

    id            = Column(Integer, primary_key=True, index=True)
    brand         = Column(String, nullable=False)
    model         = Column(String, nullable=False)
    color         = Column(String, nullable=True)
    factory_year  = Column(Integer, nullable=True)
    model_year    = Column(Integer, nullable=True)
    description   = Column(Text, nullable=True)
```

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id` | `Integer` (PK) | Sim | Identificador único (auto-incremento) |
| `brand` | `String` | Sim | Marca do veículo (ex.: Toyota, Ford) |
| `model` | `String` | Sim | Modelo do veículo (ex.: Corolla, Mustang) |
| `color` | `String` | Não | Cor predominante |
| `factory_year` | `Integer` | Não | Ano de fabricação |
| `model_year` | `Integer` | Não | Ano do modelo |
| `description` | `Text` | Não | Descrição adicional |

---

## Schemas (Pydantic)

**Arquivo:** `fast_car_api/schemas.py`

| Schema | Uso | Campos |
|---|---|---|
| **`CarSchema`** | Criação (`POST`) e atualização total (`PUT`) | `brand`, `model` (obrigatórios); `color`, `factory_year`, `model_year`, `description` (opcionais) |
| **`CarPartialUpdate`** | Atualização parcial (`PATCH`) | Todos os campos opcionais |
| **`CarPublic`** | Resposta da API (leitura) | `id` + todos os campos de `CarSchema` |
| **`CarList`** | Listagem de veículos | `cars: list[CarPublic]` |

---

## Endpoints

Todos os endpoints de veículos estão sob o prefixo `/api/v1/cars`.

---

### GET / - Health Check

Retorna o status da aplicação.

**Exemplo de requisição:**

```http
GET /
```

**Exemplo de resposta** (`200 OK`):

```json
{
  "status": "ok"
}
```

---

### POST /api/v1/cars/ - Criar veículo

Cria um novo veículo no banco de dados.

**Exemplo de requisição:**

```http
POST /api/v1/cars/
Content-Type: application/json

{
  "brand": "Toyota",
  "model": "Corolla",
  "color": "Prata",
  "factory_year": 2024,
  "model_year": 2025,
  "description": "Veículo zero quilômetro"
}
```

**Campos obrigatórios:** `brand`, `model`

**Exemplo de resposta** (`201 Created`):

```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Corolla",
  "color": "Prata",
  "factory_year": 2024,
  "model_year": 2025,
  "description": "Veículo zero quilômetro"
}
```

---

### GET /api/v1/cars/ - Listar veículos

Retorna uma lista paginada de veículos.

**Parâmetros de consulta (query params):**

| Parâmetro | Tipo | Padrão | Descrição |
|---|---|---|---|
| `offset` | `int` | `0` | Número de registros a pular (para paginação) |
| `limit` | `int` | `100` | Número máximo de registros por página |

**Exemplo de requisição:**

```http
GET /api/v1/cars/?offset=0&limit=10
```

**Exemplo de resposta** (`200 OK`):

```json
{
  "cars": [
    {
      "id": 1,
      "brand": "Toyota",
      "model": "Corolla",
      "color": "Prata",
      "factory_year": 2024,
      "model_year": 2025,
      "description": "Veículo zero quilômetro"
    }
  ]
}
```

---

### GET /api/v1/cars/{car_id} - Buscar veículo

Retorna os detalhes de um veículo específico pelo seu ID.

**Exemplo de requisição:**

```http
GET /api/v1/cars/1
```

**Exemplo de resposta** (`200 OK`):

```json
{
  "id": 1,
  "brand": "Toyota",
  "model": "Corolla",
  "color": "Prata",
  "factory_year": 2024,
  "model_year": 2025,
  "description": "Veículo zero quilômetro"
}
```

**Possíveis erros:**

| Código | Motivo |
|---|---|
| `404 Not Found` | Nenhum veículo encontrado com o ID informado |

---

### PUT /api/v1/cars/{car_id} - Atualizar veículo

Substitui **todos** os dados de um veículo existente.

> **Atenção:** Diferente do `PATCH`, o `PUT` exige o envio de **todos os campos obrigatórios** (`brand`, `model`). Campos não enviados serão definidos como `null`.

**Exemplo de requisição:**

```http
PUT /api/v1/cars/1
Content-Type: application/json

{
  "brand": "Honda",
  "model": "Civic",
  "color": "Preto",
  "factory_year": 2023,
  "model_year": 2024,
  "description": "Atualizado via PUT"
}
```

**Exemplo de resposta** (`201 Created`):

```json
{
  "id": 1,
  "brand": "Honda",
  "model": "Civic",
  "color": "Preto",
  "factory_year": 2023,
  "model_year": 2024,
  "description": "Atualizado via PUT"
}
```

---

### PATCH /api/v1/cars/{car_id} - Atualização parcial

Atualiza **apenas os campos enviados** de um veículo existente.

**Exemplo de requisição:**

```http
PATCH /api/v1/cars/1
Content-Type: application/json

{
  "color": "Azul",
  "description": "Cor alterada via PATCH"
}
```

**Exemplo de resposta** (`201 Created`):

```json
{
  "id": 1,
  "brand": "Honda",
  "model": "Civic",
  "color": "Azul",
  "factory_year": 2023,
  "model_year": 2024,
  "description": "Cor alterada via PATCH"
}
```

> **Nota:** O `PATCH` utiliza `exclude_unset=True` no Pydantic, garantindo que apenas os campos enviados no corpo da requisição sejam alterados.

---

### DELETE /api/v1/cars/{car_id} - Remover veículo

Remove um veículo do banco de dados.

**Exemplo de requisição:**

```http
DELETE /api/v1/cars/1
```

**Exemplo de resposta** (`204 No Content`):

```text
(Resposta vazia - sem corpo)
```

---

## Banco de Dados

**Arquivo:** `fast_car_api/database.py`

A aplicação utiliza **PostgreSQL** como banco de dados relacional, com o SQLAlchemy como ORM.

### Configuração

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://zemarques:mrq831028@postgres:5432/fin-pdv',
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

A URL de conexão é definida pela variável de ambiente `DATABASE_URL`. O valor padrão (`default`) aponta para o serviço `postgres` do Docker Compose.

### Criação automática das tabelas

No `app.py`, as tabelas são criadas automaticamente na inicialização:

```python
from fast_car_api.database import Base, engine

Base.metadata.create_all(bind=engine)
```

Além disso, o **Alembic** gerencia as migrações de forma versionada.

### Sessão (Dependência)

A função `get_session()` é utilizada como dependência nas rotas para injetar a sessão do banco:

```python
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
```

---

## Tratamento de Erros

Todas as rotas que buscam um veículo por ID retornam `404 Not Found` caso o recurso não exista:

```python
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Car not found',
)
```

### Códigos de status utilizados

| Código | Descrição | Endpoints |
|---|---|---|
| `200 OK` | Requisição bem-sucedida | `GET /`, `GET /cars/`, `GET /cars/{id}` |
| `201 Created` | Recurso criado/atualizado com sucesso | `POST /cars/`, `PUT /cars/{id}`, `PATCH /cars/{id}` |
| `204 No Content` | Recurso removido (sem corpo na resposta) | `DELETE /cars/{id}` |
| `404 Not Found` | Recurso não encontrado | `GET /cars/{id}`, `PUT /cars/{id}`, `PATCH /cars/{id}`, `DELETE /cars/{id}` |
| `422 Unprocessable Entity` | Erro de validação dos dados enviados | Todos os endpoints com corpo |

---

## Documentação Interativa

Com o servidor em execução, acesse:

| Ferramenta | URL | Descrição |
|---|---|---|
| **Swagger UI** | [http://localhost:8000/docs](http://localhost:8000/docs) | Interface interativa para testar os endpoints |
| **ReDoc** | [http://localhost:8000/redoc](http://localhost:8000/redoc) | Documentação alternativa em formato de página única |
| **OpenAPI JSON** | [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) | Esquema OpenAPI no formato JSON |

---

## Docker

O projeto possui suporte completo a containers com os seguintes arquivos:

### `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/bin/bash", "entrypoint.sh"]
```

### `entrypoint.sh`

Script que aguarda o PostgreSQL, executa as migrações e inicia o servidor:

```bash
#!/bin/bash
set -e

# Aguarda o PostgreSQL ficar disponível
while ! nc -z postgres 5432; do
  sleep 1
done

# Executa as migrações
alembic upgrade head

# Inicia o servidor
exec uvicorn fast_car_api.app:app --host 0.0.0.0 --port 8000
```

### `docker-compose.yaml`

Orquestra três serviços:

| Serviço | Container | Porta | Depende de |
|---|---|---|---|
| `app` | `fast_car_api` | `8000` | `postgres` |
| `postgres` | `postgres_db` | `5432` | — |
| `pgadmin` | `pgadmin_client` | `5050` | `postgres` |

### `.dockerignore`

Impede que arquivos desnecessários sejam copiados para a imagem Docker:

```text
.venv/
.ruff_cache/
__pycache__/
*.pyc
*.db
.git/
docs/
tests/
```

---

## Autor

**Jose Marques**

- Email: [josemarques.moc@gmail.com](mailto:josemarques.moc@gmail.com)

---

<div align="center">
  <sub>Fast Car API v0.1.0 — Documentação gerada em 2025</sub>
</div>
