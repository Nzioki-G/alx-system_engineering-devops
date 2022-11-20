#!/usr/bin/python3
"""given an employees id, return info about their task progress"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    users_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'{users_url}/todos'

    # get the user details to fetch name
    r1 = requests.get(users_url)
    # get user's todo LIST to fetch completed and not-completed tasks
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
