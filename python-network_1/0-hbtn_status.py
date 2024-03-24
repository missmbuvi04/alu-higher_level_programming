#!/usr/bin/python3
"""Documented by Lsblack"""
import urllib.request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content.decode("utf-8"))

