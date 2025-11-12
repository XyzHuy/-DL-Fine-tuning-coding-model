def getMoneyAmount(n):
    import sys
    # bottom up dp
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for j in range(2, n + 1):
        for i in range(j - 1, 0, -1):
            globalMin = sys.maxsize
            for k in range(i + 1, j):
                localMax = k + max(dp[i][k - 1], dp[k + 1][j])
                globalMin = min(globalMin, localMax)
            if i + 1 == j:
                dp[i][j] = i
            else:
                dp[i][j] = globalMin
    return dp[1][n]
