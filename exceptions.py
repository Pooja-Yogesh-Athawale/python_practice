import requests

try:
    r = requests.get("https://www.udacity.com")
    print(r) # If you did print(r.status_code), that also works!
except requests.exceptions.ConnectionError:
    print("Could not connect to server.")