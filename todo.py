import click
import json
import os

TODO_FILE = 'todos.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Ajoute une nouvelle tâche."""
    todos = load_todos()
    todos.append({'task': task, 'done': False})
    save_todos(todos)
    click.echo(f'Tâche ajoutée : {task}')

@cli.command()
def list():
    """Liste toutes les tâches."""
    todos = load_todos()
    if not todos:
        click.echo('Aucune tâche.')
        return
    for i, todo in enumerate(todos, 1):
        status = '✔' if todo['done'] else ' '
        click.echo(f'{i}. [{status}] {todo["task"]}')

@cli.command()
@click.argument('index', type=int)
def done(index):
    """Marque une tâche comme complétée."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index-1]['done'] = True
        save_todos(todos)
        click.echo(f'Tâche {index} marquée comme complétée.')
    else:
        click.echo('Index invalide.')

@cli.command()
@click.argument('index', type=int)
def remove(index):
    """Supprime une tâche."""
    todos = load_todos()
    if 1 <= index <= len(todos):
        removed = todos.pop(index-1)
        save_todos(todos)
        click.echo(f'Tâche supprimée : {removed["task"]}')
    else:
        click.echo('Index invalide.')

if __name__ == '__main__':
    cli()
