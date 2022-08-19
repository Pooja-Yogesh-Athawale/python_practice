import requests

try:
    r = requests.get("https://www.udacity.com")
except NameError:
    print("Did you forget to import the requests module?")

try:
    print(r.text)
except NameError:
    print("There seems to be a NameError; r is not defined!")

string = 'short'
try:
    for letter in range(6):
        print(string[letter])
except IndexError:
    print("Did you try to index past the end of the string?")

print("Woohoo! You got them all!")