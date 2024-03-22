#!/usr/bin/python3
"""
Fetches status from either https://intranet.hbtn.io/status
or http://0.0.0.0:5050/status using urllib.
"""

import urllib.request
import urllib.error


def fetch_status(url):
    """
    Fetches and prints the status from the given URL.

    Args:
        url (str): The URL to fetch the status from.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error:", e.reason)


if __name__ == "__main__":
    fetch_status("https://intranet.hbtn.io/status")

