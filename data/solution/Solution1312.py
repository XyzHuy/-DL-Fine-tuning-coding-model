import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minInsertions(self, s: str) -> int:
        # Helper function to find the longest palindromic subsequence
        def longest_palindromic_subsequence(s: str) -> int:
            n = len(s)
            dp = [[0] * n for _ in range(n)]
            
            # Every single character is a palindrome of length 1
            for i in range(n):
                dp[i][i] = 1
            
            # Build the dp table
            for length in range(2, n + 1):  # length of the substring
                for i in range(n - length + 1):
                    j = i + length - 1
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            
            return dp[0][n - 1]
        
        # The minimum number of insertions needed is the difference
        # between the length of the string and the length of the longest
        # palindromic subsequence.
        return len(s) - longest_palindromic_subsequence(s)

def minInsertions(s: str) -> int:
    return Solution().minInsertions(s)