#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
if __name__ == "__main__":
    import requests
    import sys

    fake_api = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(fake_api + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(fake_api + "todos",
                         params={"userId": sys.argv[1]}).json()
    tasks = [ts.get("title") for ts in todos if ts.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
          employee.get("name"), len(tasks), len(todos)))
    [print("\t {}".format(task)) for task in tasks]
