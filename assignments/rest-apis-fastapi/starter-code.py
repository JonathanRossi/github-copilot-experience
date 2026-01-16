from fastapi import FastAPI
from pydantic import BaseModel

# Inicialize a aplicação FastAPI
app = FastAPI()

# TODO: Defina modelos Pydantic para a tarefa
# Exemplo:
# class Task(BaseModel):
#     id: int
#     title: str
#     description: str
#     completed: bool = False

# Armazene tarefas em memória (lista)
tasks = []

# TODO: Implemente os endpoints da API
# GET /tasks - Listar todas as tarefas
# POST /tasks - Criar uma nova tarefa
# GET /tasks/{task_id} - Obter uma tarefa específica
# PUT /tasks/{task_id} - Atualizar uma tarefa
# DELETE /tasks/{task_id} - Deletar uma tarefa

# Exemplo de endpoint básico:
# @app.get("/")
# def read_root():
#     return {"message": "Bem-vindo à API de Tarefas!"}

if __name__ == "__main__":
    import uvicorn
    # Para rodar a API, execute: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
