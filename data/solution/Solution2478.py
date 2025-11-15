import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # Helper function to check if a digit is prime
        def is_prime_digit(digit):
            return digit in {'2', '3', '5', '7'}
        
        # If the string does not start with a prime digit or end with a non-prime digit, return 0
        if not is_prime_digit(s[0]) or is_prime_digit(s[-1]):
            return 0
        
        # Dynamic programming table
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        # Precompute valid partition points
        valid_points = [i for i in range(0, n - minLength + 1) if (i == 0 or not is_prime_digit(s[i - 1])) and is_prime_digit(s[i])]
        
        for i in range(minLength, n + 1):
            for parts in range(1, k + 1):
                for j in valid_points:
                    if i - j >= minLength:
                        dp[i][parts] = (dp[i][parts] + dp[j][parts - 1]) % MOD
        
        return dp[n][k]

def beautifulPartitions(s: str, k: int, minLength: int) -> int:
    return Solution().beautifulPartitions(s, k, minLength)