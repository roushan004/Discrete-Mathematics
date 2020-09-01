#!/usr/bin/env python3

import itertools as it
from Euclid_algo import extended_gcd, gcd


def ChiRTh(n1, n2, r1, r2):
    if n1>=n2:
        _, x, y = extended_gcd(n1,n2)
    else: 
        _, y, x = extended_gcd(n2, n1)
    
    x = (r1*n2*y + r2*n1*x) % (n1*n2)
    return x

def adv_CRT(n, r):
    assert all (gcd(a, b)==1 for (a,b) in it.combinations(n, 2))
    n1, r1 = n[0], r[0]
    i = 1
    for n2 in n[1::]:
        
        if i <= len(r):
            r2 = r[i]
        print("BEFORE ACTION:", " n1: ",n1," n2: ",n2," r1 ",r1," r2 ", r2)
        if n1>=n2:
            _, x, y = extended_gcd(n1, n2)
        else:
            _, y, x = extended_gcd(n2, n1)
            
        r1 = ChiRTh(n1, n2, r1, r2)
        n1 = n1*n2
        i+=1        
        print("After ACTION:", " n1: ",n1," n2: ",n2," r1 ",r1," r2 ", r2)
    return r1

n = [3, 5, 7]
r = [2, 4, 5]
print(adv_CRT(n, r))


