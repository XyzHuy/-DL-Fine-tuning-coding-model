import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(s)
        
        # dp[i][j] will store the length of the longest palindromic subsequence in s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the table
        for length in range(2, n + 1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        # We need to ensure that the palindrome uses at least one character from word1 and one from word2
        max_length = 0
        for i in range(len(word1)):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    max_length = max(max_length, dp[i][j + len(word1)])
        
        return max_length

def longestPalindrome(word1: str, word2: str) -> int:
    return Solution().longestPalindrome(word1, word2)