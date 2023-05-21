from flask import Flask
from flask import request
app = Flask(__name__)
version_path = '/v1'


@app.post(f'{version_path}/todos')
def create_todo():
    return "created"


@app.get(f'{version_path}/todos')
def fetch_todos():
    return []


@app.get(f'{version_path}/todos/<int:todo_id>')
def fetch_todo(todo_id):
    return f'Todo: {todo_id}'


@app.patch(f'{version_path}/todos/<int:todo_id>')
def update_todo(todo_id):
    return f'update Todo: {todo_id}'


@app.delete(f'{version_path}/todos/<int:todo_id>')
def delete_todo(todo_id):
    return f'delete Todo: {todo_id}'


if __name__ == "__main__":
    app.run(debug=True)
