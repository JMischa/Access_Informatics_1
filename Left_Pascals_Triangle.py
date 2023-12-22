__author__ = "Mischa Jampen"

# build a string 
def build_string_pyramid(h):

    # One idea is to start with an empty string and append individual lines
    s = ""

    for i in range(1, h + 1):
        line = ''
        for j in range(1, i + 1):
            line += str(j)
            if j < i:
                line += '*'
        s += line + '\n'

    
    for i in range(h-1, 0, -1):
        line = ''
        for j in range(1, i + 1):
            line += str(j)
            if j < i:
                line += '*'
        s += line + '\n'
    # You may want to use nested loops and the range() function

    # Don't forget to return the result
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid(5))

