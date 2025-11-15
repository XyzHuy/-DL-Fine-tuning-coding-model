import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        # Find the longest common suffix between initial and target
        m, n = len(initial), len(target)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if initial[i - 1] == target[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        
        # The length of the longest common suffix
        longest_common_suffix = max(max(row) for row in dp)
        
        # Minimum operations needed
        return m + n - 2 * longest_common_suffix

def minOperations(initial: str, target: str) -> int:
    return Solution().minOperations(initial, target)