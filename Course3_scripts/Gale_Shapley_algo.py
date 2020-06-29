#!/usr/bin/env python3

def stableMatching(n, menPreferences, womenPreferences):
    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n
    # Each man made 0 proposals, which means that
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]]
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]

        # Write your code here
        if currentHusband == None:
          #do the rest as she accepts him
          manSpouse[he] = she
          womanSpouse[she] = he
          unmarriedMen.remove(he)
          nextManChoice[he] += 1

        elif herPreferences.index(he) < herPreferences.index(currentHusband):
          #she accepts him
          manSpouse[he] = she
          manSpouse[currentHusband] = None
          womanSpouse[she] = he
          unmarriedMen.remove(he)
          unmarriedMen.append(currentHusband)
          nextManChoice[he] += 1

        else:
          #gets rejected
          nextManChoice[he] += 1

    return manSpouse

# You might want to test your implementation on the following two tests:
#print(stableMatching(1, [ [0] ], [ [0] ]))
#stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ])

a = stableMatching(3, [ [0,1,2], [0,2,1], [2,1,0] ], [ [1,2,0], [0,2,1], [1,0,2] ])
a

