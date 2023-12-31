__author__ = "Mischa Jampen"

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []

    for i in range(2,len(n) + 1):
        for digit in range(10):
            nr = n[:2] + n[2:i] + str(digit) + n[i:]
            possible_nrs_for_juliet.append(nr)

    return (list(set(possible_nrs_for_juliet) & set(wa_nrs)))
    # Don't forget to return your result

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
