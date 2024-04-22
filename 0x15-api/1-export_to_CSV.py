#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data
in CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    fake_api = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]

    # Fetching employee information
    employee = requests.get(fake_api + "users/{}".format(employee_id)).json()
    employee_name = employee.get("username")

    # Fetching todos for the employee
    todos = requests.get(fake_api + "todos", params={"userId": employee_id}).json()

    # Filtering completed tasks and preparing data for CSV
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for todo in todos:
        task_completed = "True" if todo.get("completed") else "False"
        task_title = todo.get("title")
        csv_data.append([employee_id, employee_name, task_completed, task_title])

    # Writing data to CSV file
    csv_file_name = "{}.csv".format(employee_id)
    with open(csv_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print("Data exported to {} successfully.".format(csv_file_name))
