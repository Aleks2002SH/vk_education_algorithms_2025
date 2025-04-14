from build_tree import *

def maxMinMultiplication(data):
    if len(data)<3:
        return -1
    min_ind,max_ind = 0,0
    while 2 * min_ind + 1 < len(data) and data[2*min_ind+1]!=None:  
        min_ind = 2 * min_ind + 1

    while 2 * max_ind + 2 < len(data) and data[2*max_ind+2]!=None:  
        max_ind = 2 * max_ind + 2

    res = data[min_ind]*data[max_ind]
    return res