#!/usr/bin/python3
""" Gather data from an API """
import json
import sys
import urllib.request


def emp(id):
    usr = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url1 = 'https://jsonplaceholder.typicode.com/todos'
    request_url = urllib.request.urlopen(usr)
    data = request_url.read()
    request_url1 = urllib.request.urlopen(url1)
    todos1 = request_url1.read()
    todos = json.loads(todos1)
    jdata = json.loads(data)
    com = 0
    tks = 0
    emp_task = []
    emp_name = jdata.get("name")

    for j in todos:
        """ stor the title name of the  completed task """
        if j["userId"] == id:
            if j["completed"]:
                emp_task.append(j["title"])
                com = com + 1
            tks = tks + 1

    print("Employee {} is done with tasks({}/{}):".format(emp_name, com, tks))
    for i in emp_task:
        print("\t", end="")
        print(i)


if __name__ == "__main__":
    emp(int(sys.argv[1]))
