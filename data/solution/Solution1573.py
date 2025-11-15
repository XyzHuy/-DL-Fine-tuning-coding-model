import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        total_ones = s.count('1')
        
        # If the total number of ones is not divisible by 3, we cannot split the string as required
        if total_ones % 3 != 0:
            return 0
        
        # If there are no ones, we can split the string in any way we want
        if total_ones == 0:
            # We need to choose 2 positions out of n-1 possible positions to split the string
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % MOD
        
        # Each part must have exactly total_ones // 3 ones
        target_ones = total_ones // 3
        count_ones = 0
        first_cut_options = 0
        second_cut_options = 0
        
        for i, char in enumerate(s):
            if char == '1':
                count_ones += 1
            
            # Find the end of the first part
            if count_ones == target_ones:
                first_cut_options += 1
            # Find the end of the second part
            elif count_ones == 2 * target_ones:
                second_cut_options += 1
        
        # The number of ways to split is the product of the number of ways to place the first and second cuts
        return (first_cut_options * second_cut_options) % MOD

def numWays(s: str) -> int:
    return Solution().numWays(s)