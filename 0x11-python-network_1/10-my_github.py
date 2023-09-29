#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
"""

from sys import argv
import requests

if __name__ == '__main__':
    r = requests.get("https://api.github.com/user",
                     auth=(argv[1], argv[2]))
    data = r.json()
    id = data.get('id')
    print(id)
