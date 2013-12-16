first_name = "Zaphod"


def hello(name):
    """Say hello"""
    print "Hello, {}".format(name)


def hello_multi(name, greeting_mult=1):
    """Say hello gratuitously"""
    greeting_count = 3 * greeting_mult
    for num in range(greeting_count):
        hello(name)

hello(first_name)
hello_multi(first_name, 2)
