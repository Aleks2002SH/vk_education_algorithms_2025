def count_sequences(N):
    if N==0:
        return 1
    if N==1:
        return 2
    if N ==2:
        return 4
    
    dp = [1,2,4]

    for i in range(3,N+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    
    return dp[N]