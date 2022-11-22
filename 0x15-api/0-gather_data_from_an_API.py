#!/usr/bin/python3
"""
Python script that fetches info about an employees tasks
progress using REST API
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2 and sys.argv[i].isdigit():
        user_id = sys.argv[1]

        r1 = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        r2 = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")

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
