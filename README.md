# Todo-api-flask
Simple CRUD api built using python and flask. Data are retrieved from and written into a JSON file which serves as a local DB

### Setup
- Clone repo
- Activate packages: `source .venv/bin/Activate`
- Install environment: `python3 -m venv .venv`
- Run application `flask --app server run --debug`

### API routes

- Create todo:
  `url_path: /v1/todos`
  `method = POST`
  `body:`
  ```
  {
    "note": "Note here
  }
- Fetch todos
`url_path: /v1/todos`
`method = GET`
- Fetch a todo item
`url_path: /v1/todos/todo_id`
`method = GET`

- Update a todo item
`url_path: /v1/todos/todo_id`
`method = PATCH`
  `body:`
  ```
  {
    "note": "Note here
  }
- Delete a todo item
`method = DELETE`
`url_path: /v1/todos/todo_id`