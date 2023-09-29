#!/usr/bin/python3
""" script that fetches from a url using urllib package """

import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        html_body = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(html_body)))
        print("\t- content: {}".format(html_body))
        print("\t- utf8 content: {}".format(html_body.decode('utf-8')))
