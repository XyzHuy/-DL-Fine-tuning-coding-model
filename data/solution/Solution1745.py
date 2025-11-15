import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        n = len(s)
        
        # Precompute palindrome status for all substrings
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        
        # Try to find the first palindrome partition
        for i in range(1, n - 1):
            if is_pal[0][i - 1]:
                for j in range(i + 1, n):
                    if is_pal[i][j - 1] and is_pal[j][n - 1]:
                        return True
        
        return False

def checkPartitioning(s: str) -> bool:
    return Solution().checkPartitioning(s)