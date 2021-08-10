import sys

print(sys.version)
print(sys.executable)

jun_name = 'jun'

def greet(who_to_greet):
    greeting = f'Hello, {who_to_greet}'
    return greeting

print(greet('World'))
print(greet('Jun'))
