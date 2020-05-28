#!/usr/bin/env python3
from n_choose_k import choose
"""
The choose function returns ways to choose k sized subset from a n sized set
Getting the coefficients from choose() function we can divide each of them by 2^(layers-1) 
and append the values to the fractions array.
The fractions array then contains the fraction of all beads going in the bins for the range of bins given
So THE CONCENTRATION of beads in bins is just the sum of all elements times 100
"""

def main(n, start, stop):
    fractions = []
    #iterate through all favourable values of k
    for k in range(start, stop+1):
        #calculate the fraction
        fract = choose(n, k)/2**n
        fractions.append(fract)

        #uncomment the following line to get a more verbose output
        #print(f"TRACKING- k:{k} _______ fraction={fract}")
    #calculate and print the concentration
    print("Concentration: ",sum(fractions)*100)

if __name__ == "__main__":
    n = int(input("Enter layers on board:"))-1
    print("Enter the start and stop point of values of k:-")
    start = int(input("(K) start point:"))
    stop = int(input("(K) end point:"))
    main(n, start, stop)
