#!/usr/bin/env python3

def change(amount):
    #base cases:
    #all of 10, 12, 14 when added by 5 further can pay any amount possibly payable by coins of 7 and 5
    assert amount >= 10, "The amount is NOT payable by coins of 7 and 5."
    if amount == 10:
        return [5,5]
    if amount == 12:
        return [5,7]
    if amount == 14:
        return  [7,7]
    if amount % 7 == 0:
        coins = change(amount-7)
        coins.append(7)
    else:
        coins = change(amount-5)
        coins.append(5)
    return coins
    
#print(change(998))
if __name__ == "__main__":
    n = int(input("Enter the amount for which you want me to genrate list of coins:"))
    print(change(n))
