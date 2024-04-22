#!/usr/bin/python3
"""
Export data in the JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    all_data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = [
            {"username": username, "task": task.get('title'),
             "completed": task.get('completed')}
            for task in todos if task.get('userId') == user_id
        ]
        all_data[str(user_id)] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_data, json_file)
