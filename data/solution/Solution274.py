def arrangeCoins(n):
    level = 0
    while n > level:
        level += 1
        n -= level
    return level
