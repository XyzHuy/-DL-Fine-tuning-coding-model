import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        # Create a 2D array to store lengths of longest common subsequence.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the dp array from bottom up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence is in the bottom-right cell
        return dp[m][n]

def longestCommonSubsequence(text1: str, text2: str) -> int:
    return Solution().longestCommonSubsequence(text1, text2)