#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST reques
"""

from sys import argv
import urllib.request as request
import urllib.parse as parse

if __name__ == '__main__':
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        html = r.read()
        utf8 = html.decode('utf-8')
        print(utf8)
