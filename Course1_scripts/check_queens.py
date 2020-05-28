#!/usr/bin/env python3
#recursive or bottom-up approach decreases the number of iterations hence providing increased efficiency 

#define a function to check for continuing the permutations search ... use the distance formula to get the diagonal points 

def whether_to_extend(perm):
    i = len(perm) - 1
    for j in range(i):
        if i-j == abs(perm[i] - perm[j]):
            return False
    return True

# define a function to generate the permutations recursively while checking the conditions associated with backtracing

def extend(perm, n):
     
    #write the base case
    if len(perm) == n:
        print(perm)
        #comment the following line to get all possible permutaions
        exit()

    for i in range(n):
        if i not in perm:
            perm.append(i)
            if whether_to_extend(perm):
                extend(perm, n)
            
            perm.pop()
            

if __name__ == "__main__":
    n = int(input("Enter the number of rows on the chess board:"))
    extend([], n)


