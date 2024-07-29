#!/usr/bin/python3
"""
This module exports all tasks owned by this employee in JSON format.

The JSON file format:
{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ...] }

Usage:
    python3 2-export_to_JSON.py <USER_ID>
"""

import json
import requests
import sys


def fetch_user_tasks(user_id):
    """
    Fetches tasks for a given user_id from the JSONPlaceholder API.

    Args:
        user_id (str): The ID of the user.

    Returns:
        tuple: A tuple containing the user data and the user's tasks (list).
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None, None

    user = user_response.json()
    todos = todos_response.json()

    return user, todos


def export_to_json(user, todos):
    """
    Exports tasks to a JSON file in the specified format.

    Args:
        user (dict): The user data.
        todos (list): The list of tasks.

    File format:
        {"USER_ID":[{"task": "TASK_TITLE","completed": TASK_COMPLETED_STATUS,
        "username": "USERNAME"}, ...] }
    """
    user_id = user.get('id')
    username = user.get('username')
    tasks = [{"task": todo.get('title'),
              "completed": todo.get('completed'),
              "username": username} for todo in todos]

    data = {str(user_id): tasks}

    filename = f"{user_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    user, todos = fetch_user_tasks(user_id)

    if user is None or todos is None:
        print(f"Failed to fetch data for user ID {user_id}")
        sys.exit(1)

    export_to_json(user, todos)
    print(f"Data exported to {user_id}.json")
