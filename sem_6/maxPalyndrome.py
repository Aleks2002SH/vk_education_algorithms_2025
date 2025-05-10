def maxPalyndrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    ind = 0
    max_len = 1
    
    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ind = i
            max_len = 2

    for l in range(2,n+1):
        for i in range(n - l + 1):
            j = i+l-1
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if l > max_len:
                    ind = i  
                    max_len = l

    return s[ind:ind+max_len]  
        
