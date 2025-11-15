import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        if n < 5:
            return 0
        
        # DP tables
        left = [[0] * 10 for _ in range(n)]
        right = [[0] * 10 for _ in range(n)]
        left_pairs = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        right_pairs = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        
        # Fill left table
        for i in range(n):
            for d in range(10):
                left[i][d] = (left[i-1][d] if i > 0 else 0) + (1 if int(s[i]) == d else 0)
        
        # Fill right table
        for i in range(n-1, -1, -1):
            for d in range(10):
                right[i][d] = (right[i+1][d] if i < n-1 else 0) + (1 if int(s[i]) == d else 0)
        
        # Fill left_pairs table
        for i in range(n):
            for d1 in range(10):
                for d2 in range(10):
                    left_pairs[i][d1][d2] = (left_pairs[i-1][d1][d2] if i > 0 else 0)
                    if i > 0:
                        left_pairs[i][d1][d2] += left[i-1][d1] if d2 == int(s[i]) else 0
        
        # Fill right_pairs table
        for i in range(n-1, -1, -1):
            for d1 in range(10):
                for d2 in range(10):
                    right_pairs[i][d1][d2] = (right_pairs[i+1][d1][d2] if i < n-1 else 0)
                    if i < n-1:
                        right_pairs[i][d1][d2] += right[i+1][d2] if d1 == int(s[i]) else 0
        
        # Count palindromic subsequences of length 5
        result = 0
        for i in range(2, n-2):
            for d1 in range(10):
                for d2 in range(10):
                    result += left_pairs[i-1][d1][d2] * right_pairs[i+1][d2][d1]
                    result %= MOD
        
        return result

def countPalindromes(s: str) -> int:
    return Solution().countPalindromes(s)