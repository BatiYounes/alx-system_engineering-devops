#!/usr/bin/python3
"""
This module exports all tasks owned by this employee in CSV format.
"""

import csv
import requests
import sys


def fetch_user_tasks(user_id):
    """
    Fetches tasks for a given user_id from the JSONPlaceholder API.
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


def export_to_csv(user, todos):
    """
    Exports tasks to a CSV file in the format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    The file name must be: USER_ID.csv
    """
    user_id = user.get('id')
    username = user.get('username')
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csvwriter.writerow([user_id, username, todo.get('completed'), todo.get('title')])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    user, todos = fetch_user_tasks(user_id)

    if user is None or todos is None:
        print(f"Failed to fetch data for user ID {user_id}")
        sys.exit(1)

    export_to_csv(user, todos)
    print(f"Data exported to {user_id}.csv")
