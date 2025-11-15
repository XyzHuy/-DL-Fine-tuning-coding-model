import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def encode(self, s: str) -> str:
        def find_repetition(sub):
            n = len(sub)
            for i in range(1, n // 2 + 1):
                if n % i == 0 and sub[:i] * (n // i) == sub:
                    return i
            return n

        def dp(i, j):
            if i == j:
                return s[i]
            if (i, j) in memo:
                return memo[(i, j)]
            substring = s[i:j+1]
            n = len(substring)
            rep_len = find_repetition(substring)
            if rep_len < n:
                encoded = f"{n // rep_len}[{dp(i, i + rep_len - 1)}]"
            else:
                encoded = substring
            
            for k in range(i, j):
                left = dp(i, k)
                right = dp(k + 1, j)
                combined = left + right
                if len(combined) < len(encoded):
                    encoded = combined
            
            memo[(i, j)] = encoded
            return encoded
        
        memo = {}
        return dp(0, len(s) - 1)

def encode(s: str) -> str:
    return Solution().encode(s)