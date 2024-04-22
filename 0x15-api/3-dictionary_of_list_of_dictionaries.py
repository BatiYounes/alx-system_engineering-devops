#!/usr/bin/python3
"""
export all tasks that are owned by this employee in the JSON format.
"""
if __name__ == "__main__":
    import json
    import requests

    fake_api = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(fake_api + "users").json()
    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            user.get("id"): [{"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": user.get("username")
                              } for task in requests.get(fake_api + "todos",
                                       params={"userId": user.get("id")}
                                       ).json()]
            for user in users}, json_file)
