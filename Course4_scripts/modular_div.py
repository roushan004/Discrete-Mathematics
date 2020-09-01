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

if __name__ == '__main__':
    print("Finds X in relation b/a congruent to X (mod n) ")
    a = int(input('a:'))
    b = int(input('b:'))
    n = int(input('n:'))
    print(mod_div(a, b, n)
