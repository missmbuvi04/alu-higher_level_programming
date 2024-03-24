#!/usr/bin/python3
"""A script that
- fetches http://0.0.0.0:5050/status.
- uses urllib package
"""


if __name__ == '__main__':
    import urllib.request

    url = 'http://0.0.0.0:5050/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

