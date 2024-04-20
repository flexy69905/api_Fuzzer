import requests
import sys

user_url = input("Enter your url or ip: ")

print(f"starting fuzz for url {user_url}")

def loop():
    for word in sys.stdin:
        res = requests.get(url=f"{user_url}/{word}")
        if res.status_code == 404:
            loop()
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

loop()