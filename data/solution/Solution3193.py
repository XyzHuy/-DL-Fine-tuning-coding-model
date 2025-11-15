import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Initialize DP table
        dp = [[0] * 401 for _ in range(n)]
        dp[0][0] = 1  # Base case: one way to arrange one number with zero inversions
        
        # Requirements dictionary for quick lookup
        req_dict = {endi: cnti for endi, cnti in requirements}
        
        for i in range(1, n):
            prefix_sum = [0] * 402  # To keep prefix sums for efficient range queries
            for j in range(401):
                prefix_sum[j + 1] = (prefix_sum[j] + dp[i - 1][j]) % MOD
            
            for j in range(401):
                # Calculate dp[i][j] using prefix sums
                if j >= i:
                    dp[i][j] = (prefix_sum[j + 1] - prefix_sum[j - i] + MOD) % MOD
                else:
                    dp[i][j] = prefix_sum[j + 1] % MOD
            
            # Apply requirements if applicable
            if i in req_dict:
                # Only keep the required number of inversions
                for j in range(401):
                    if j != req_dict[i]:
                        dp[i][j] = 0
        
        # The answer is the number of permutations of all n numbers with any number of inversions
        return sum(dp[n - 1]) % MOD

def numberOfPermutations(n: int, requirements: List[List[int]]) -> int:
    return Solution().numberOfPermutations(n, requirements)