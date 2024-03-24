#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status and prints the response.
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"

    # Create a request object
    with urllib.request.urlopen(url) as response:
        # Read the response content
        content = response.read()

        # Decode the content to UTF-8
        utf8_content = content.decode('utf-8')
