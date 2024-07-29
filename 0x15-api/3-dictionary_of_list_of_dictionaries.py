#!/usr/bin/python3
"""
This module fetches and exports to-do list data in JSON format
for all users from a REST API.
"""

import json
import requests


def fetch_data():
    """Fetch data from the API and return it as JSON."""
    base_url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(f'{base_url}/users').json()
    todos = requests.get(f'{base_url}/todos').json()

    return users, todos


def create_user_tasks(users, todos):
    """Create a dictionary of user tasks."""
    user_tasks = {user['id']: [] for user in users}
    for task in todos:
        username = next(user['username'] for user in users 
                        if user['id'] == task['userId'])
        task_data = {
            'username': username,
            'task': task['title'],
            'completed': task['completed']
        }
        user_tasks[task['userId']].append(task_data)

    return user_tasks


def export_to_json(user_tasks):
    """Export user tasks to a JSON file."""
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == '__main__':
    users, todos = fetch_data()
    user_tasks = create_user_tasks(users, todos)
    export_to_json(user_tasks)
