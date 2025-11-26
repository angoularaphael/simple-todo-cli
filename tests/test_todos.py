import os
import json
from todo import load_todos, save_todos, TODO_FILE

def setup_module():
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)

def test_save_and_load():
    todos = [{'task': 'Test', 'done': False}]
    save_todos(todos)
    loaded = load_todos()
    assert loaded == todos
    os.remove(TODO_FILE)
