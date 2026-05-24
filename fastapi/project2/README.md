1. Garanta que todas dependências necessárias estão instaladas
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

2. Baixe e execute o script de instalação
curl https://pyenv.run | bash

3. Adicione o seguinte script no arquivo ~/.bashrc
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

4. Restart shell
5. Valide a instalação
pyenv --version
Comandos básicos
# lista as versões de python disponíveis
pyenv install -l
# instala uma versão
pyenv install <version>
# mostra versão instalada
pyenv global
# define uma versão
pyenv global <version>

# lista versões instaladas
pyenv versions

Author: @Diogo Duarte
Github: @diogoduarte
Linkedin: https://www.linkedin.com/in/diogoduartec

poetry = pip + venv (gerenciador de pacotes e dependências e também de ambiente virtual
iniciar ambiente virtual:
#poetry env activate

Passo 1: Ativar de verdade
Para garantir que você está dentro do ambiente, copie e cole o comando que ele imprimiu
para você. No seu caso, deve ser exatamente este:
Bash
source
/home/zemarques/.cache/pypoetry/virtualenvs/introducao-phhdTEpc-py3.10/bin/activate


Inicia a migrations:

docker compose run --user 1000 app sh -c 'alembic init migrations'

Gera a migration:
docker compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "add categories table"'

Executa a migration no BD:

# 🚀 Project2 — FastAPI + PostgreSQL + Poetry + Docker

> **Checklist diário de início de trabalho.**  
> Siga este guia na ordem para levantar o ambiente do zero.

---

## Índice

1. [Pré-requisitos (instalar uma vez)](#1-pré-requisitos-instalar-uma-vez)
2. [Setup inicial do projeto (uma vez)](#2-setup-inicial-do-projeto-uma-vez)
3. [Checklist diário — mão na massa](#3-checklist-diário--mão-na-massa)
4. [Comandos úteis](#4-comandos-úteis)
5. [Estrutura do projeto](#5-estrutura-do-projeto)

---

## 1. Pré-requisitos (instalar uma vez)

Execute os passos abaixo **apenas na primeira vez** que for configurar a máquina.

### 1.1. Dependências do sistema (Ubuntu/Debian)

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

### 1.2. Pyenv (gerenciar versões do Python)

```bash
curl https://pyenv.run | bash
```

Adicione ao final do `~/.bashrc`:

```bash
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

Reinicie o shell ou execute:

```bash
source ~/.bashrc
```

Valide:

```bash
pyenv --version
```

### 1.3. Poetry (gerenciar pacotes e ambiente virtual)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Adicione ao `~/.bashrc` (se ainda não estiver):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Recarregue e valide:

```bash
source ~/.bashrc
poetry --version
```

### 1.4. Docker (PostgreSQL + serviços)

Instale o Docker e o Docker Compose conforme a [documentação oficial](https://docs.docker.com/engine/install/ubuntu/).

Após instalar, adicione seu usuário ao grupo docker (para não precisar de `sudo`):

```bash
sudo usermod -aG docker $USER
```

**Faça logout e login novamente** para o grupo fazer efeito.

---

## 2. Setup inicial do projeto (uma vez)

Execute **apenas na primeira vez** que for clonar/criar o projeto.

### 2.1. Clone o repositório e entre na pasta

```bash
cd /caminho/para/o/projeto
```

### 2.2. Configure a versão do Python com Pyenv

```bash
pyenv install 3.11   # se ainda não tiver instalado
pyenv local 3.11
```

### 2.3. Instale as dependências com Poetry

```bash
poetry install
```

Isso cria o ambiente virtual e instala todas as dependências listadas no `pyproject.toml`.

### 2.4. Crie o arquivo `.env`

Copie o exemplo e ajuste as variáveis:

```bash
# Crie o .env na raiz do projeto com:
DATABASE_URL=postgresql://admin:admin@db:5432/project2
POSTGRES_DB=project2
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin
```

> ⚠️ O `.env` **não** deve ser versionado (já está no `.gitignore`).

### 2.5. Suba o banco de dados com Docker

```bash
docker compose up -d db
```

Aguarde alguns segundos até o PostgreSQL estar pronto.

### 2.6. Execute as migrations iniciais

```bash
docker compose run --user 1000 app sh -c 'alembic upgrade head'
```

> Se o container `app` ainda não foi construído, rode `docker compose build app` antes.

---

## 3. Checklist diário — mão na massa

Sempre que **iniciar o dia de trabalho** ou **começar um novo projeto**, siga esta sequência.

### Passo 0 — Navegue até o projeto

```bash
cd /home/zemarques/curso-python/fastapi-bkp/project2
```

### Passo 1 — Ative o ambiente virtual do Poetry

```bash
poetry env activate
```

O Poetry imprimirá um comando como este abaixo — **copie e cole no terminal**:

```bash
source /home/zemarques/.cache/pypoetry/virtualenvs/project2-xxxxxx-py3.11/bin/activate
```

Para facilitar, crie um alias ou use diretamente:

```bash
eval $(poetry env activate)
```

> ⚠️ Você saberá que está dentro do ambiente quando o terminal mostrar algo como `(project2-xxxxxx-py3.11)` no prompt.

### Passo 2 — Suba os containers Docker

```bash
docker compose up -d
```

Isso inicia:
- **`app`** — aplicação FastAPI (:8000)
- **`db`** — PostgreSQL principal (:5432)
- **`db-teste`** — PostgreSQL de testes (:5433)
- **`pgadmin`** — Interface para o banco (:5050)

### Passo 3 — Verifique se os serviços estão rodando

```bash
docker compose ps
```

Todos devem estar com status `Up`.

### Passo 4 — Execute as migrations pendentes

```bash
docker compose run --user 1000 app sh -c 'alembic upgrade head'
```

> Use `--user 1000` para evitar problemas de permissão nos arquivos gerados.

### Passo 5 — Rode os testes (opcional, mas recomendado)

```bash
docker compose run --user 1000 app sh -c 'python -m pytest'
```

### Passo 6 — Acesse a aplicação

- **API**: http://localhost:8000  
- **Documentação (Swagger)**: http://localhost:8000/docs  
- **PGAdmin**: http://localhost:5050  
  - Email: `admin@admin.com`  
  - Senha: `admin`  

---

## 4. Comandos úteis

### 4.1. Poetry

| Comando | Descrição |
|---|---|
| `poetry env activate` | Mostra o comando para ativar o ambiente virtual |
| `poetry install` | Instala todas as dependências do `pyproject.toml` |
| `poetry add <pacote>` | Adiciona uma nova dependência |
| `poetry remove <pacote>` | Remove uma dependência |
| `poetry show` | Lista os pacotes instalados |
| `poetry env info` | Mostra informações do ambiente virtual |

### 4.2. Pyenv

| Comando | Descrição |
|---|---|
| `pyenv install --list` | Lista versões disponíveis do Python |
| `pyenv install <versão>` | Instala uma versão específica |
| `pyenv global` | Mostra a versão global atual |
| `pyenv global <versão>` | Define a versão global do Python |
| `pyenv local <versão>` | Define a versão Python para o diretório atual |
| `pyenv versions` | Lista todas as versões instaladas |

### 4.3. Docker

| Comando | Descrição |
|---|---|
| `docker compose up -d` | Sobe todos os serviços em background |
| `docker compose up -d db` | Sobe apenas o banco |
| `docker compose down` | Para e remove todos os containers |
| `docker compose ps` | Status dos serviços |
| `docker compose logs -f` | Logs em tempo real de todos os serviços |
| `docker compose logs -f app` | Logs apenas da aplicação |
| `docker compose exec app sh` | Abre um shell dentro do container `app` |
| `docker compose build app` | Reconstrói a imagem da aplicação |

### 4.4. Alembic (migrations)

| Comando | Descrição |
|---|---|
| `docker compose run --user 1000 app sh -c 'alembic init migrations'` | Inicializa o diretório de migrations **(uma vez)** |
| `docker compose run --user 1000 app sh -c 'alembic revision --autogenerate -m "descrição da mudança"'` | Gera uma nova migration automaticamente |
| `docker compose run --user 1000 app sh -c 'alembic upgrade head'` | Aplica todas as migrations pendentes |
| `docker compose run --user 1000 app sh -c 'alembic downgrade -1'` | Reverte a última migration |
| `docker compose run --user 1000 app sh -c 'alembic current'` | Mostra a migration atual |
| `docker compose run --user 1000 app sh -c 'alembic history'` | Histórico de todas as migrations |

### 4.5. Testes

```bash
# Rodar todos os testes
docker compose run --user 1000 app sh -c 'python -m pytest'

# Rodar com verbose
docker compose run --user 1000 app sh -c 'python -m pytest -v'

# Rodar testes de um arquivo específico
docker compose run --user 1000 app sh -c 'python -m pytest tests/use_cases/test_category_use_cases.py -v'
```

### 4.6. Acessar o banco via terminal

```bash
docker exec -it postgresql psql -U admin -d project2
```

---

## 5. Estrutura do projeto

```
project2/
├── .env                       # Variáveis de ambiente (não versionar)
├── .gitignore
├── Dockerfile                 # Imagem da aplicação
├── docker-compose.yml         # Orquestração dos serviços
├── pyproject.toml             # Dependências (Poetry)
├── poetry.lock                # Lock das dependências
├── README.md                  # 👈 você está aqui
│
├── app/                       # Código principal
│   ├── main.py                # Ponto de entrada (FastAPI app)
│   │
│   ├── db/                    # Conexão e modelos do banco
│   │   ├── base.py            # Base declarativa do SQLAlchemy
│   │   ├── connection.py      # Engine e sessão
│   │   └── models.py          # Modelos ORM
│   │
│   ├── schemas/               # Schemas Pydantic
│   │   ├── base.py            # Schema base
│   │   └── category.py        # Schema de categorias
│   │
│   ├── routes/                # Endpoints (FastAPI routers)
│   │
│   ├── use_cases/             # Regras de negócio / Casos de uso
│   │
│   ├── test/                  # Testes automatizados
│   │   ├── conftest.py        # Fixtures do Pytest
│   │   ├── schemas/
│   │   └── use_cases/
│   │
│   ├── migrations/            # Migrations do Alembic
│   │   ├── versions/          # Arquivos de migração
│   │   ├── env.py             # Configuração do Alembic
│   │   ├── script.py.mako     # Template para novas migrations
│   │   └── README
│   │
│   └── alembic.ini            # Configuração do Alembic
```

---

## 🧠 Solução de problemas

| Problema | Solução |
|---|---|
| `Permission denied` ao gerar migration | Use `--user 1000` no `docker compose run` |
| Porta 8000 já em uso | Mude a porta no `docker-compose.yml` ou pare o outro processo |
| Banco não conecta | Verifique se o container `db` está rodando: `docker compose ps` |
| Dependência nova não encontrada | Rode `poetry install` e depois `docker compose build app` |
| `alembic upgrade head` não encontra tabelas | Verifique se o modelo foi importado no `env.py` do Alembic |
| Poetry não ativa o ambiente | Use `eval $(poetry env activate)` |

---

> **Autor:** @Jose Marques  
> *Checklist diário — para não esquecer nenhum passo no início do dia.*

























meu_projeto/
├── .venv/                   # Ambiente virtual
├── app/                     # Código principal da aplicação
│   ├── core/                # Configurações globais e segurança
│   │   ├── config.py        # Configurações (ex: Pydantic BaseSettings)
│   │   └── security.py      # Autenticação, hash de senhas, JWT
│   ├── db/                  # Conexão com banco de dados
│   │   ├── session.py       # Engine e Session do SQLAlchemy
│   │   └── base.py          # Base dos modelos
│   ├── models/              # Modelos do Banco de Dados (ORM)
│   │   └── usuario.py
│   ├── schemas/             # Schemas Pydantic (validação e serialização)
│   │   └── usuario.py
│   ├── routers/             # Endpoints da API (Controllers)
│   │   ├── usuario.py
│   │   └── auth.py
│   ├── services/            # Regras de negócio / Lógica da aplicação
│   │   └── usuario.py
│   └── main.py              # Ponto de entrada da aplicação
├── tests/                   # Testes automatizados
├── .gitignore
├── pyproject.toml           # Dependências (Poetry) ou requirements.txt
└── README.md


Detalhamento dos Diretórioscore/: Guarda a infraestrutura e configurações essenciais. Em config.py, use o BaseSettings do Pydantic para ler variáveis de ambiente (arquivo .env).db/: Centraliza a conexão com o banco de dados. Facilmente integrado com ORMs como SQLAlchemy ou Tortoise ORM.models/: Onde ficam as tabelas do seu banco de dados.schemas/: Objetos Pydantic responsáveis por definir o formato de entrada e saída dos dados na sua API (Request/Response bodies).routers/: Concentra os endpoints (rotas) da API. Evite colocar regras de negócio complexas diretamente aqui.services/: Camada intermediária que executa a lógica de negócios (chamada pelo router e utilizando as interações com o db).main.py: Arquivo raiz onde a instância do FastAPI() é criada, middlewares são adicionados e os routers são incluídos.Arquivos de Configuração de DependênciasPara gerenciar os pacotes do seu projeto, utilize gerenciadores como o Poetry (recomendado) ou um simples requirements.txt utilizando pip.Exemplo de estrutura mínima para um pyproject.toml usando o Poetry:toml[tool.poetry]
name = "meu_projeto"
version = "0.1.0"
description = "API FastAPI"
authors = ["Seu Nome <seu.email@exemplo.com>"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.110.0"
uvicorn = "^0.28.0"
sqlalchemy = "^2.0.0"
pydantic-settings = "^2.2.0"
Use o código com cuidado.Melhores Práticas de ModularizaçãoSe o seu projeto for muito grande, a estrutura modular pode ser mais eficiente. Em vez de separar por tipo de arquivo (tudo junto em schemas/), você agrupa por domínio, ficando com pastas como app/usuarios/ e app/produtos/, onde cada uma contém seu próprio models.py, schemas.py, router.py, e services.py.