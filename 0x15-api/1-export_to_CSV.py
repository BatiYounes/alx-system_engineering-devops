#!/usr/bin/python3
"""
Exports all tasks owned by a specific employee in CSV format.

This script takes an employee ID as a command-line
argument and retrieves all tasks
associated with that employee from a fake API
It then exports the tasks into a CSV file named after the employee ID.

Usage: python3 script_name.py employee_id
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    fake_api = 'https://jsonplaceholder.typicode.com/'
    _id = sys.argv[1]
    employee = requests.get(fake_api + "users/{}".format(_id)).json()
    tasks = requests.get(fake_api + "todos", params={"userId": _id}).json()
    employee_username = employee.get("username")
    with open("{}.csv".format(_id), "w", newline="") as csv_file:
        csv_w = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        [csv_w.writerow([_id, employee_username, task.get("completed"),
                         task.get("title")]) for task in tasks]
	
