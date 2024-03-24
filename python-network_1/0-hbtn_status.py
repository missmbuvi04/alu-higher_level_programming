#!/usr/bin/python3

"""Script that fetches status from a URL using urllib."""

import urllib.request

def getStatus():
    """
    Fetches the status from 'https://intranet.hbtn.io/status'
    and prints out the response body.
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        type_content = type(content)
        print("Body response:")
        print("\t- type: {}".format(type_content))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))

if __name__ == "__main__":
    getStatus()

