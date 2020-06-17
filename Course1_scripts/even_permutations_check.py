#!/usr/bin/env python3

#RUnning time ~ O(n)

def is_even(p):
    target = [i for i in range(len(p))]
    steps = 0
    #Each neighbour transposition takes 2K+1 steps
    #What we require are total number of steps to reach the target
    temp = p
    for i in range(len(p)-1):
        #require difference in  indexes of permuation[i] and i@target 
        if temp[i] == target[i]:
            continue
        else:
            a = target[i] 
            ind = temp.index(a)             
            #transpose them in temp array
            temp[ind], temp[i] = temp[i], temp[ind]
            #calculate moves 
            k = abs(ind-(i+1))            
            steps += (2*k)+1 
    
    # return 0 for even steps and 1 for odd ones
    if temp != target:
        return False
    return steps%2 == 0
