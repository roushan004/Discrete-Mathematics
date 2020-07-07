#!/usr/bin/env python3

def gcd(p, q):
    assert p >= 0 and q >= 0 and p+q > 0

    return gcd(q, p%q) if q>0 else p
def extended_gcd(a, b):
    #implementation of gcd check d = ax + by 
    assert a >= b and b >= 0 and a+b > 0

    if b == 0:
        d, x, y = a, 1, 0
        
    else:
        (d, p, q) = extended_gcd(b, a%b)
        x = q 
        y = p - q * (a // b)

    #sanity check
    assert a%d == 0 and b%d == 0
    assert d == a*x + b*y
    return (d, x, y)

def lcm(a, b):
    Gcd = gcd(a,b)
    return (a*b)/Gcd
#print(gcd(4,6))
#print(gcd(10,9))
#print(extended_gcd(10, 6))
if __name__ == '__main__':
     a = int(input("a:"))
     b = int(input("b:"))
     g = extended_gcd(a,b)
     print(f'gcd:{g}')
     l = lcm(a,b)
     print(f"lcm: {l}")
