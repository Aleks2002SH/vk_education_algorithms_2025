class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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