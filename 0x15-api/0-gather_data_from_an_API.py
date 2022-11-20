#!/usr/bin/python3
"""fetch info about an employees tasks' progress using REST API"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    users_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'{users_url}/todos'

    r1 = requests.get(users_url)
    r2 = requests.get(todos_url)

    name = r1.json().get("name")
    completed = 0
    total = 0
    done_with = []

    for dict in r2.json():
        if dict.get("completed"):
            completed += 1
            done_with.append(dict.get("title"))
        total += 1

    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for task in done_with:
        print(f"\t {task}")
