import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][k] means the number of valid sequences of length i
        # where j is 1 if there is one 'A' in the sequence, 0 if there is none
        # and k is the number of trailing 'L's in the sequence (0, 1, or 2)
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # Base case: empty sequence
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Adding 'P'
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD
                    # Adding 'A' (only if there is no 'A' in the sequence yet)
                    if j == 0:
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD
                    # Adding 'L' (only if there are less than 2 trailing 'L's)
                    if k > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD
        
        # Sum up all valid sequences of length n
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        
        return result

def checkRecord(n: int) -> int:
    return Solution().checkRecord(n)