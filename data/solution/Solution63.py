def uniquePathsWithObstacles( obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    if m == 0:
        return 0
    dmap = [[0] * (n + 1) for _ in range(m + 1)]
    dmap[m - 1][n] = 1
    for i in range(m - 1, -1, -1):
        for j in  range(n - 1, -1, -1):
            if obstacleGrid[i][j] == 1:
                dmap[i][j] = 0
            else:
                dmap[i][j] = dmap[i][j + 1] + dmap[i + 1][j]
    return dmap[0][0]
