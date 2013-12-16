first_name = "Zaphod"


def hello():
    """Say hello"""
    print "Hello, {}".format(first_name)


def reverse_name():
    # try removing or commenting-out the next line
    global first_name
    first_name = first_name[::-1]

hello()
reverse_name()
hello()
