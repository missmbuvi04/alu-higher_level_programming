#!/usr/bin/python3
# python script that fetches 'https://alu-intranet.hbtn.io/status

import urllib.request
import urllib.error

def fetch_status(url):
    """
    Fetches and prints the status from the given URL
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
    except urllib.error.URLError as e:
        print("Error:", e.reason)

if __name__ == "__main__":
    fetch_status("https://alu-intranet.hbtn.io/status")
