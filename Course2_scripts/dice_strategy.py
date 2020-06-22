#!/usr/bin/env python3
import itertools as it
def count_wins(dice1, dice2):
    assert len(dice1)==6 and len(dice2) == 6
    global dice1_wins
    global dice2_wins
    global d1, d2
    d1, d2 = dice1, dice2
    dice1_wins, dice2_wins = 0,0
    for i in dice1:
        for j in dice2:
            if i>j:
                dice1_wins += 1
            if i<j:
                dice2_wins += 1

def find_the_best_dice(dices):
    assert all(len(dice)==6 for dice in dices)
    global indexes
    indexes = []
    for i in it.combinations(dices, 2):
        #call check_wins
        count_wins(i[0], i[1])
        if dice1_wins > dice2_wins:
            indexes.append(dices.index(d1))
        elif dice2_wins > dice1_wins:
            indexes.append(dices.index(d2))
        else:
            indexes.append(None)
        
    #check state of indexes array 
    # if the list has the same index for len(dices)-1 times then its a best dice exists
    exists = False
    for i in indexes:
        if indexes.count(i)>=len(dices)-1 and i!=None:
            exists = True
            ind = i
    if exists:
        return ind
    return -1

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = {}
    a = find_the_best_dice(dices)
    if a != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = a
    else:
        strategy["choose_first"] = False
        l = list(it.combinations(range(len(dices)), 2))
        for i in range(len(l)):
            #Find a better dice than ith dice
            for j in [0,1]:
                if indexes[i] == l[i][j] and j==0:
                    strategy[l[i][j+1]] = l[i][j]
                if indexes[i] == l[i][j] and j==1:
                    strategy[l[i][j-1]] = l[i][j]
                
    return strategy
print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))
print(compute_strategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]))
print(compute_strategy([[1,2,3,4,5,6],[1,2,3,4,5,6]]))
