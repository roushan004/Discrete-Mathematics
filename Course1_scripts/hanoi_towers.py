#!/usr/bin/env python3 

def move(n):
    if n == 1:
        moves = 1
    else:
        moves = move(n-1) + 1 + move(n-1)
    return moves
#print(move(2))
#print(move(3))
#print(move(4))

if __name__ == '__main__':
    n = int(input("Enter n (number of discs):"))
    print(move(n))

