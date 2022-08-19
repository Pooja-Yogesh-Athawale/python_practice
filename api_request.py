import requests
r = requests.get('https://www.google.com/monkeybagel/')

if r.status_code == 404:
    print("Page not found.")