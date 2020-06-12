#!/usr/bin/env python3

def seq(word, target):
    path = []
    temp = list(word)
    for letter in word:
        tup = []
        if "".join(temp) == target:
            break
        tup.append(temp.index(letter))
        temp[target.index(letter)], temp[temp.index(letter)] = temp[temp.index(letter)], temp[target.index(letter)]
        tup.append(temp.index(letter))
        if tup[0] != tup[1]:
            path.append(tuple(tup))
    return path

if __name__ == '__main__':
    w = str(input("word:"))
    t = str(input("target:"))
    trans = seq(w, t)
    print(f"The transpositions required are: {trans}")


