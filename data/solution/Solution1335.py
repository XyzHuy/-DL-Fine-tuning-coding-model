import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        # dp[i][j] means the minimum difficulty to schedule the first i jobs in j days
        dp = [[math.inf] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, min(i, d) + 1):
                maxDifficulty = 0
                for k in range(i, j - 1, -1):
                    maxDifficulty = max(maxDifficulty, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + maxDifficulty)
        
        return dp[n][d] if dp[n][d] != math.inf else -1

# Example usage:
# sol = Solution()
# print(sol.minDifficulty([6,5,4,3,2,1], 2))  # Output: 7
# print(sol.minDifficulty([9,9,9], 4))        # Output: -1
# print(sol.minDifficulty([1,1,1], 3))        # Output: 3

def minDifficulty(jobDifficulty: List[int], d: int) -> int:
    return Solution().minDifficulty(jobDifficulty, d)