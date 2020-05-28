#!/usr/bin/env python3
# 0 signifies empty space
# 1 signifies /
# -1 signifies \

def empty_list_generator(n):
    """ generates list of size n for calculation"""
    square = [[0 for j in range(n)] for i in range(n)]
    return square

def is_valid(square, row, column, fillable):
    '''
    Checks if the current item in list [0, 1, -1] can be added to the square list at row, column.
    It returns True if the fillable can be assigned to square[row][column] while being valid;
    else returns False
    '''
    #It is always valid if the fillable is zero
    if fillable == 0:
        return True
    if fillable == 1:
        if column+1 < len(square[row]):
            if square[row][column+1] == -1:
                return False
            if row - 1 >= 0 and square[row-1][column+1] == 1:
                return False
        
        if column-1 >= 0:
            if square[row][column-1] == -1:
                return False
            if row+1 < len(square) and square[row+1][column-1] == 1:
                return False
        
        if row - 1 >= 0 and square[row-1][column] == -1:
            return False
        
        if row + 1 < len(square) and square[row+1][column] == -1:
            return False

    #reverse case when fillable is -1
    if fillable == -1:
        #BEing LAZY AND COPIYING THE ABOVE CODE. Well remember to replace those 1s with -1
        if column+1 < len(square[row]):
            if square[row][column+1] == 1:
                return False
            if row - 1 >= 0 and square[row-1][column+1] == -1:
                return False

        if column-1 >= 0:
            if square[row][column-1] == 1:
                return False
            if row+1 < len(square) and square[row+1][column-1] == -1:
                return False

        if row - 1 >= 0 and square[row-1][column] == 1:
            return False

        if row + 1 < len(square) and square[row+1][column] == 1:
            return False
    return True

def printer(square):
    #0: " "
    #1: "/"
    #-1: "\"
    for i in range(len(square)):
        for j in range(len(square)):
            #check all three cases in current position square[i][j]
            if square[i][j] == 0:
                print("_", end=" ")
            if square[i][j] == 1:
                print("/", end=" ")
            if square[i][j] == -1:
                print("\\", end=" ")
        #changeline
        print()

def main(square, row, column, diagonals):
    """
    The main function checks if it is valid to add the current fillable out of [0, 1, -1] to the list square at row, column.
    If it is valid to do so: then it again calls the main function with improvised parameters so as to meet the base case and
    Return back the updated square list
    """
    #base case when there are no more diagonals to be added
    if diagonals == 0:
        print(square)
        printer(square)
        exit()        
        
    if row == len(square):
        return 
    for fillable in [1, -1, 0]:  #alter the positions of 1, -1 in this list so as to get a different solution    
        if is_valid(square, row, column, fillable):
            square[row][column] = fillable
            
            #if the current position is successfully filled by a diagonal then
            if fillable != 0:
                if column < len(square)-1:
                    main(square, row, column+1, diagonals-1)
                else:
                    main(square, row+1, 0, diagonals-1)
            #contrary case
            else:
                if column < len(square)-1:
                    main(square, row, column+1, diagonals)
                else:
                    main(square, row+1, 0, diagonals)

#To view certain square list copy and paste the square list into the printer function
#printer( [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 0, -1, -1, 0], [1, 1, 0, -1, -1], [0, 1, 1, 0, -1]])

if __name__ == "__main__":
    n = int(input("Enter the number of rows or columns in the square:"))
    diagonals = int(input("Enter the amount of diagonals you want me to fit inside the square space:"))
    square = empty_list_generator(n)
    main(square, 0, 0, diagonals)
