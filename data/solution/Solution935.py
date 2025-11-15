import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Define the possible moves for each number on the dial pad
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        # Initialize the dp array where dp[i] is the number of ways to end at number i with 1-length number
        dp = [1] * 10
        
        # Iterate for n-1 steps (since we start with 1-length number)
        for _ in range(1, n):
            new_dp = [0] * 10
            for i in range(10):
                for move in moves[i]:
                    new_dp[i] = (new_dp[i] + dp[move]) % MOD
            dp = new_dp
        
        # Sum up all the ways to end at any number with n-length number
        return sum(dp) % MOD

def knightDialer(n: int) -> int:
    return Solution().knightDialer(n)