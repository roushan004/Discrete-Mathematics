#!/usr/bin/env python3
from Euclid_algo import extended_gcd,gcd
import itertools as it
# implementation of b/a congruent to x (mod n)   Returns: X

def mod_div(a, b, n):
    if a>=n:
        gcd, _, s = extended_gcd(a,n)
    else:
        gcd, _, s = extended_gcd(n,a)
    print(f"s: {s}       other one: {_}")
    
    if gcd == 1:
        #find the S in s congruent to S (mod n)
        S = s % n
        return (b*S) % n # this is congruent to b/a (mod n)
def ChiTh(n, r):
    assert all(gcd(a, b)==1 for (a,b) in it.combinations(n, 2))
    for n1 in n:
        if n1 == n[0]:
            # its the first one; leave it and default some of values for next level
            a = n1
            b = n[1]
            r1 = r[0]
            r2 = r[1]
            if a>=b:
                d, x, y = extended_gcd(a, b)
            else:
                d, x, y = extended_gcd(b, a)
            r1 = (r1*b*y + r2*a*x) % (a*b)
            a = a*b
            continue
        if n1 == n[1]:
            #already considered continue
            continue
        a, b = a, n1
        if a>=b:
            d, x, y = extended_gcd(a, b)
        else:
            d, x, y = extended_gcd(b, a)
        r2 = r[n.index(n1)]

        r1 = (r1*b*y + r2*a*x) % (a*b)
        a=a*b
    return r1

if __name__ == '__main__':
    print("Finds X in relation b/a congruent to X (mod n) or From a given array of numbers determines modulo product of all numbers")
    print("Selct 1 or 2")
    choice = input("Enter 1 or 2:")
    if choice == 1:
        a = int(input('a:'))
        b = int(input('b:'))
        n = int(input('n:'))
        print(mod_div(a, b, n))
    else:
        print("Try entering the parameters from the program itself")
