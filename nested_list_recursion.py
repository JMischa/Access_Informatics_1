#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def analyze(item):

    if isinstance(item, (float, int)):
        return (item, [item])
    elif isinstance(item, str):
        return (0, [3 * len(item)])
    elif not isinstance(item, list):
        return (0, [item])
    elif isinstance(item, list) and len(item) == 0:
        return (0, item)
    sum_num = 0
    list_items = []
    if isinstance(item[0], (int,float)):
        sum_num += item[0]
        list_items.append(item[0])
    elif isinstance(item[0], str):
        list_items.append(3 * len(item[0]))
    elif isinstance(item[0], list):

        nested_res = analyze(item[0])
        sum_num += nested_res[0]
        list_items.append(nested_res[1])
    else:
        list_items.append(item[0])
    
    rest_res = analyze(item[1:])
    sum_num += rest_res[0]
    list_items.extend(rest_res[1])
    
    return(sum_num, list_items)
# The following line calls the function and prints the return
# value to the Console only, if this file is run as the main file.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
if __name__ == "__main__": # Do not change this line, it could affect the grading
    #item = [1, [6, 1, {}], 2, "s"]
    #print(analyze(item))
    print(analyze([1, [{}, 2], print, "hi"]))  # mixed with other types
    # (3, [1, [{}, 2], <built-in function print>, 6])


