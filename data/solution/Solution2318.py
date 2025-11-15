import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Define valid transitions based on the GCD condition
        valid_next = {
            1: [2, 3, 4, 5, 6],
            2: [1, 3, 5],
            3: [1, 2, 4, 5],
            4: [1, 3, 5],
            5: [1, 2, 3, 4, 6],
            6: [1, 5]
        }
        
        # Initialize DP table
        # dp[i][j][k] means the number of valid sequences of length i ending with j, k
        if n == 1:
            return 6
        
        dp = [[[0] * 7 for _ in range(7)] for _ in range(n + 1)]
        
        # Base case: sequences of length 2
        for i in range(1, 7):
            for j in valid_next[i]:
                dp[2][i][j] = 1
        
        # Fill the DP table
        for length in range(3, n + 1):
            for prev in range(1, 7):
                for curr in valid_next[prev]:
                    for next_roll in valid_next[curr]:
                        if next_roll != prev:
                            dp[length][curr][next_roll] = (dp[length][curr][next_roll] + dp[length - 1][prev][curr]) % MOD
        
        # Sum up all valid sequences of length n
        result = 0
        for i in range(1, 7):
            for j in range(1, 7):
                result = (result + dp[n][i][j]) % MOD
        
        return result

def distinctSequences(n: int) -> int:
    return Solution().distinctSequences(n)