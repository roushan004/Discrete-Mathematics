#!/usr/bin/env python3

def conv(trans):
    for element in trans:
        if abs(element[0] - element[1]) == 1:
            continue
        else:
            el = [ (i, i+1) for i in range(element[0], element[1])]
            for i in range(len(el)-1):
                #append len(ele)-1 elements
                el.append(el[i])
            trans[trans.index(element)] = el
    return trans
print(conv([(0, 3), (0, 1), (4, 5)]))
if __name__ == '__main__':
    print("Not meant to be directly executed")
