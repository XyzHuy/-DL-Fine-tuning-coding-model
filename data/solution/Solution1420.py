import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # memo[i][j][c] will store the number of ways to build an array of length i
        # with maximum value j and search cost c
        memo = {}
        
        def dp(i, j, c):
            if i == n:
                return 1 if c == k else 0
            if c > k:
                return 0
            if (i, j, c) in memo:
                return memo[(i, j, c)]
            
            # Case 1: The next element is less than or equal to the current max j
            ways = j * dp(i + 1, j, c)
            
            # Case 2: The next element is greater than the current max j, increasing the search cost
            for x in range(j + 1, m + 1):
                ways += dp(i + 1, x, c + 1)
            
            memo[(i, j, c)] = ways % MOD
            return memo[(i, j, c)]
        
        # Start the recursion with an array of length 0, max value 0, and search cost 0
        total_ways = 0
        for x in range(1, m + 1):
            total_ways += dp(1, x, 1)
        
        return total_ways % MOD

def numOfArrays(n: int, m: int, k: int) -> int:
    return Solution().numOfArrays(n, m, k)