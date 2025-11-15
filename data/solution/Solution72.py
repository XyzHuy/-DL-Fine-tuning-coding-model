import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a 2D array to store the minimum edit distances
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the dp array
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from word1 to match empty word2
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters from word2 to match empty word1
        
        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed if characters match
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Delete from word1
                                       dp[i][j - 1],    # Insert into word1
                                       dp[i - 1][j - 1]) # Replace in word1
        
        return dp[m][n]

def minDistance(word1: str, word2: str) -> int:
    return Solution().minDistance(word1, word2)