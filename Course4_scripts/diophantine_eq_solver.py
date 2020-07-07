#!/usr/bin/env python3
# solutions for ax + by = c     Returns: Values of x and y
from Euclid_algo import extended_gcd, gcd

def deqs(a, b, c):
    if c/gcd(a,b) == c//gcd(a,b):
        #so solutions are possible
        #extract values of x' and y' from extended_gcd(a,b)
        if a>=b and b>=0:
            (d, x, y) = extended_gcd(a,b)
        else:
            (d, y, x) = extended_gcd(b, a)
        print(f"d: {d} x:{x}  y: {y}")
        # X and Y are values of X,Y in the diophantine equation
        t = c/d
        X = x*t
        Y = y*t
    else:
        return 
    return (X, Y)

if __name__ == '__main__':
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    print(deqs(a, b, c))
