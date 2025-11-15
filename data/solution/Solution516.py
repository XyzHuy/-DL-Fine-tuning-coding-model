import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Create a 2D array to store the length of the longest palindromic subsequence
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Build the dp array from substrings of length 2 to n
        for length in range(2, n + 1):  # length is the length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # The result is the length of the longest palindromic subsequence for the whole string
        return dp[0][n - 1]

def longestPalindromeSubseq(s: str) -> int:
    return Solution().longestPalindromeSubseq(s)