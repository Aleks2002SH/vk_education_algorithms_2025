
def pascal_triangle(N):
    dp = []

    for i in range(1,N+1):
        tmp = []
        for j in range(i):
            tmp.append(1)
        dp.append(tmp)
    
    for row in range(1,N):
        for col in range(1,row):
            dp[row][col] = dp[row-1][col-1]+dp[row-1][col]

    return dp