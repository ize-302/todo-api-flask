import json
from flask import Flask, jsonify, request
import uuid
import os
app = Flask(__name__)
app.debug = True
version_path = '/v1'


# write data to file
def write_to_file(data):
    with open('todos.json', 'w') as file:
        json.dump(data, file)


# read external json file
def read_file():
    # create todos.json if not exist
    json_file_exists = os.path.exists('todos.json')
    if json_file_exists == False:
        write_to_file([])
    with open('todos.json') as f:
        return json.load(f)


# generate random uuid.
def generate_id():
    return str(uuid.uuid4())


existing_todos = read_file()


# API ROUTES
# create todo
@app.post(f'{version_path}/todos')
def create_todo():
    data = {
        "id": generate_id(),
        "note": request.json['note']
    }
    existing_todos.append(data)
    write_to_file(existing_todos)
    return jsonify({"message": 'Note created', "todo": data}), 201


# fetch todos
@app.get(f'{version_path}/todos')
def fetch_todos():
    return jsonify({"todos": existing_todos}), 200


# fetch a todo
@app.get(f'{version_path}/todos/<todo_id>')
def fetch_todo(todo_id):
    result = None
    for todo in existing_todos:
        if todo['id'] == todo_id:
            result = todo
            break
    if result == None:
        return jsonify({"error": 'Resource not found'}), 404
    else:
        return jsonify({"todo": result}), 200


# update a todo
@app.patch(f'{version_path}/todos/<todo_id>')
def update_todo(todo_id):
    updated_note = request.json['note']
    result = None
    for todo in existing_todos:
        if todo['id'] == todo_id:
            todo['note'] = updated_note
            result = todo
            break
    if result == None:
        return jsonify({"error": 'Resource not found'}), 404
    else:
        write_to_file(existing_todos)
        return jsonify({"todo": result, "success": 'Resource updated'}), 200


# delete a todo
@app.delete(f'{version_path}/todos/<todo_id>')
def delete_todo(todo_id):
    result = []
    for todo in existing_todos:
        if todo['id'] != todo_id:
            result.append(todo)
    write_to_file(result)
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
