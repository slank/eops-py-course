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

# call with a positional argument. Specifies no return value
return_value = hello(first_name)
print "Return value: {}".format(return_value)

# call with a positional argument. Omit keyword argument
return_value = hello_multi(first_name)
print "Return value: {}".format(return_value)

# call with a positional argument. Specify keyword argument positionally
return_value = hello_multi(first_name, 2)
print "Return value: {}".format(return_value)

# call with a positional argument. Specify keyword argument by name
return_value = hello_multi(first_name, greeting_mult=2)
print "Return value: {}".format(return_value)
