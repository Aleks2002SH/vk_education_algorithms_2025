def canMakeValidWithDeletions(s,k):
    balance = 0
    extra_closed_balance = 0

    for i in range(len(s)):
        if s[i] == '(':
            balance+=1
        else:
            if balance>0:
                balance-=1
            else:
                extra_closed_balance+=1
    
    total_needed = balance+extra_closed_balance

    return total_needed <= k