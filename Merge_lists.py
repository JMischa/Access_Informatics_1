#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    
    if a == [] or b == []:
        return []
    if len(a) == len(b):
        ans = list(zip(a,b))
    elif len(a) > len(b):
        ans = []
        for i in range(0, len(b)):
            ans.append((a[i], b[i]))
        for j in range(len(b), len(a)):
            ans.append((a[j], b[-1]))
        return ans
    else:
        res = []
        for i in range(0, len(a)):
            res.append((a[i], b[i]))
        for j in range(len(a), len(b)):
            res.append((a[-1], b[j]))
        return res    
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0,3], [5, 6, 1,2,3,4]))