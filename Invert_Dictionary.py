__author__ = "Mischa Jampen"

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    # implement this function
    invert_dict = {}
    for key in d:
        value = d[key]
        if not(value in invert_dict):
            invert_dict[value] = [key]
        else:
            invert_dict[value].append(key)

    for value in invert_dict:
        invert_dict[value] = sorted(invert_dict[value])

    return invert_dict
# The following line callsv the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3}))
