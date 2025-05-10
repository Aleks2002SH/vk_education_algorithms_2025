


def b_sequence(N):
    if N == 1:
        return 2
    if N == 2:
        return 3
    dp = [1,2]
    for i in range(2,N+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[N]



    