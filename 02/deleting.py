first_name = "Zaphod"


def hello(name):
    """Say hello"""
    print "Hello, {}".format(name)


def hello_multi(name, greeting_mult=1):
    """Say hello gratuitously"""
    greeting_count = 3 * greeting_mult
    for num in range(greeting_count):
        hello(name)
    return greeting_count

del(first_name)
try:
    hello(first_name)
except NameError as e:
    print e

del(hello)
try:
    hello_multi("Startibartfast")
except NameError as e:
    print e
