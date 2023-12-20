#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes(n):
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.
     
    primes_up_to_n = [True] * (n+1)
    primes_up_to_n[0] = primes_up_to_n[1] = False

    for p in range(2, math.ceil(math.sqrt(n)) + 1):
        if primes_up_to_n[p]:
            for i in range(p * p, n + 1, p):
                primes_up_to_n[i] = False

    primes = [i for i in range(2, n + 1) if primes_up_to_n[i]]
    return primes
    
    



    # You don't need to change the following line.
    # It simply returns the list created above.
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes(100))
