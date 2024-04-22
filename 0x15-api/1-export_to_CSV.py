#!/usr/bin/python3
"""
Export data in CSV format
"""
import csv
import json
import requests
from sys import argv


def export_to_csv(user_id):
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    user_data = [user for user in users if user.get('id') == int(user_id)]
    if not user_data:
        return "User not found"

    username = user_data[0].get('username')
    tasks = [
        (str(user_id), username, str(task.get('completed')), task.get('title'))
        for task in todos if task.get('userId') == int(user_id)
    ]

    if not tasks:
        return "No tasks found for this user"

    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(tasks)

    return f"CSV exported to {filename}"


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <user_id>")
    else:
        user_id = argv[1]
        print(export_to_csv(user_id))
