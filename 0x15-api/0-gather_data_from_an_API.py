#!/usr/bin/python3
"""
Python script that fetches info about an employees tasks
progress using REST API
"""
if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2 and sys.argv[1].isdigit():

        r1 = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
        r2 = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}")

        EMPLOYEE_NAME = r1.json()['name']
        NUMBER_OF_DONE_TASKS = 0
        TOTAL_NUMBER_OF_TASKS = len(r2.json())
        done_with = []

        for dict_ in r2.json():
            if dict_.get("completed"):
                NUMBER_OF_DONE_TASKS += 1
                done_with.append(dict_['title'])

        print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
        for task in done_with:
            print(f"\t {task}")
