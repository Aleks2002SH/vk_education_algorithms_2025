
def isSubsequence_q(s, t):
    
    q = []
    
    for el in s:
        q.append(el)
    
    for el in t:
        if len(q)!= 0:
            if q[0] == el:
                q.pop(0)
        else:
            return True
    
    return len(q) == 0