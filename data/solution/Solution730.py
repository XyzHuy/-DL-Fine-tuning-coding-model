import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # next[i][c] is the next occurrence of character c after index i
        # prev[i][c] is the previous occurrence of character c before index i
        next = [[-1] * 4 for _ in range(n)]
        prev = [[-1] * 4 for _ in range(n)]
        
        # Fill prev array
        last = [-1] * 4
        for i in range(n):
            last[ord(s[i]) - ord('a')] = i
            for j in range(4):
                prev[i][j] = last[j]
        
        # Fill next array
        last = [-1] * 4
        for i in range(n - 1, -1, -1):
            last[ord(s[i]) - ord('a')] = i
            for j in range(4):
                next[i][j] = last[j]
        
        # dp[i][j] is the number of distinct palindromic subsequences in s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for c in range(4):
                    char = chr(ord('a') + c)
                    left = next[i][c]
                    right = prev[j][c]
                    if left > j or right < i:
                        # No character c in s[i:j+1]
                        continue
                    elif left == right:
                        # Exactly one character c in s[i:j+1]
                        dp[i][j] += 1
                    else:
                        # More than one character c in s[i:j+1]
                        dp[i][j] += dp[left + 1][right - 1] + 2
        
        return dp[0][n - 1] % MOD

def countPalindromicSubsequences(s: str) -> int:
    return Solution().countPalindromicSubsequences(s)