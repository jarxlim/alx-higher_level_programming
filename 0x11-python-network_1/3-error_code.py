#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""

from sys import argv
import urllib.request as request
import urllib.error as error

if __name__ == '__main__':

    try:
        with request.urlopen(argv[1]) as r:
            html = r.read()
            utf8 = html.decode('utf-8')
            print(utf8)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
