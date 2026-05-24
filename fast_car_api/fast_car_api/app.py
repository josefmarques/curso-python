from fastapi import FastAPI

from fast_car_api.database import Base, engine
from fast_car_api.routers import router as car_router

# Cria as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Fast Car API',
    description='JMarques modern Car API',
    version='0.1.0',
)

app.include_router(car_router)


@app.get('/')
def read_root():
    return {'status': 'ok'}
