import uvicorn
from app import create_app

# Cria a instância da aplicação, igual ao curso
app = create_app()

if __name__ == '__main__':
    # O Uvicorn substitui o app.run() do Flask
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)