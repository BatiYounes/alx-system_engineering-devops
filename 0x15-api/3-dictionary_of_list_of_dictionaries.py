import json
import requests

def fetch_data():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    return users, todos

def process_data(users, todos):
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []
        for todo in todos:
            if todo['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks.append(task_info)
        data[user_id] = user_tasks
    return data

def export_to_json(data):
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    users, todos = fetch_data()
    data = process_data(users, todos)
    export_to_json(data)
