def mergeAlgo(left,right):

    newCabinet = []
    while(min(len(left),len(right)) > 0):
        if left[0] > right[0]:
            to_insert = right.pop(0)
            newCabinet.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            newCabinet.append(to_insert)
    if(len(left) > 0):
        for i in left:
            newCabinet.append(i)
    if(len(right) > 0):
        for i in right:
            newCabinet.append(i)
    return(newCabinet)

import math

def mergSortAlgo(cabinet):
    newCabinet = []
    if(len(cabinet) == 1):
        newCabinet = cabinet
    else:
        left = mergSortAlgo(cabinet[:math.floor(len(cabinet)/2)])
        right = mergSortAlgo(cabinet[math.floor(len(cabinet)/2):])
        newCabinet = mergeAlgo(left,right)
    return(newCabinet)

cabinet = [13,27,44,7,6,8,9]
newerCabinet= mergSortAlgo(cabinet)
print(cabinet)