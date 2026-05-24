from fastapi import FastAPI

def create_app():
    # A criação do app agora fica protegida dentro desta função
    app = FastAPI(title="Sistema Financeiro e PDV")

    # Suas rotas iniciais
    @app.get("/")
    def read_root():
        return {"status": "Servidor rodando perfeitamente!"}

    # Retorna a aplicação pronta
    return app