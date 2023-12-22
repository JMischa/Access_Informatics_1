__author__ = "Mischa Jampen"

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def get_average_grade(path):

    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        num = 0
        sum = 0
        for l in f.readlines():
            if l.startswith("#"):
                continue

            idx = l.find(":")
            if idx > 0:
                l2 = l[idx+1:]
                f = float(l2)
                sum += f
                num += 1

        if sum == 0:
            return 0.0
        else:
            return sum/num

# The following line calls the function and prints the return
# value to the console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("task/my_grades.txt"))

