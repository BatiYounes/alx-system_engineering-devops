#!/usr/bin/python3
"""
Export all tasks that are owned by this
employee in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    fake_api = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]

    # Fetching employee information
    employee_response = requests.get(fake_api + "users/{}".format(employee_id))
    employee = employee_response.json()
    if employee_response.status_code != 200:
        print("Error: Employee not found.")
        sys.exit(1)

    employee_username = employee.get("username")

    # Fetching todos for the employee
    tasks_response = requests.get(fake_api + "todos",
                                  params={"userId": employee_id})
    if tasks_response.status_code != 200:
        print("Error: Unable to fetch tasks.")
        sys.exit(1)
    tasks = tasks_response.json()

    # Creating JSON data
    json_data = {employee_id: []}
    for task in tasks:
        json_data[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        })

    # Writing data to JSON file
    json_file_name = "{}.json".format(employee_id)
    with open(json_file_name, "w") as json_file:
        json.dump(json_data, json_file)

    print("Data exported to {} successfully.".format(json_file_name))
