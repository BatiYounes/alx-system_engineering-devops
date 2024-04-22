#!/usr/bin/python3
"""
Export all tasks that are owned by this
employee in the CSV format.
"""
import csv
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

    # Writing data to CSV file
    csv_file_name = "{}.csv".format(employee_id)
    with open(csv_file_name, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                             "TASK_TITLE"])
        
        # Fetching todos for the employee
        tasks_response = requests.get(fake_api + "todos",
                                      params={"userId": employee_id})
        if tasks_response.status_code != 200:
            print("Error: Unable to fetch tasks.")
            sys.exit(1)
        tasks = tasks_response.json()
        
        for task in tasks:
            csv_writer.writerow([employee_id, employee_username,
                                str(task.get("completed")), task.get("title")])

    print("Number of tasks in CSV: OK")
    print("Data exported to {} successfully.".format(csv_file_name))
