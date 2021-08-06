import sys
import requests


print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = f'Hello, {who_to_greet}'
    return greeting

print(greet('World'))
print(greet('Jun'))

r = requests.get('https://wsp.co.uk')
print(r.status_code)
