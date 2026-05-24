import pytest
from alembic import command
from alembic.config import Config
from app.db.connection import Session

# 1. Nova fixture que cria as tabelas automaticamente
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Caminho para o seu arquivo alembic.ini (ajuste se estiver em outra pasta)
    alembic_cfg = Config("alembic.ini")
    
    # Roda as migrações (cria as tabelas)
    command.upgrade(alembic_cfg, "head")
    
    yield  # Aqui o Pytest roda todos os seus testes
    
    # Limpa o banco de dados desfazendo as migrações após os testes
    command.downgrade(alembic_cfg, "base")

# 2. A sua fixture original continua igualzinha
@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()