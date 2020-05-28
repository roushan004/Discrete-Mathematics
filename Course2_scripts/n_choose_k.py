#!/usr/bin/env python3
def choose(N, K):
    #pt[n, k] is just equal to n chose k
    pt = {}
    #populate the dictionary

    for n in range(N+1):
        pt[n, 0] = 1
        pt[n, n] = 1

        for k in range(1, n):
            pt[n, k] = pt[n-1, k-1] + pt[n-1, k]

    return pt[N, K]

#test: print(choose(10, 5))

if __name__ == "__main__":
    n = int(input("Enter n:"))
    k = int(input("Enter k:"))
    print(choose(n, k))
