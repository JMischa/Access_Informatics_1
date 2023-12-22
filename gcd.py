__author__ = "Mischa Jampen"
######################
# Author: Mischa Jampen
######################

def gcd(a, b):
    # implement this function
    if a == 0 and b == 0:
        raise ValueError
    if a == 0 and b != 0:
        return abs(b)
    if a != 0 and b == 0:
        return abs(a)
    if abs(a) > abs(b):
        return gcd(abs(b), abs(a) % abs(b))
    else:
        return gcd(abs(a), abs(b) % abs(a))


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 116
b = 1926
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

