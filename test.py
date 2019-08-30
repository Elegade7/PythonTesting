import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# testing a change

print(greet("world"))
print(greet("Zach"))
