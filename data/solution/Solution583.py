import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a 2D DP array to store the lengths of longest common subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence
        lcs_length = dp[m][n]
        
        # The minimum number of deletions required
        return (m - lcs_length) + (n - lcs_length)

def minDistance(word1: str, word2: str) -> int:
    return Solution().minDistance(word1, word2)