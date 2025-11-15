import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # Memoization dictionary to store results of subproblems
        memo = {}
        
        def count_ways(z, o, last_digit, last_run):
            # Base case: if we have used all zeros and ones
            if z == 0 and o == 0:
                return 1
            # If we have used more zeros or ones than needed
            if z < 0 or o < 0:
                return 0
            
            # Create a unique key for the current state
            key = (z, o, last_digit, last_run)
            if key in memo:
                return memo[key]
            
            total_ways = 0
            
            # If the last digit was 0, we can add another 0 if the run is less than limit
            if last_digit == 0:
                if last_run < limit:
                    total_ways += count_ways(z - 1, o, 0, last_run + 1)
                # We can always add a 1
                total_ways += count_ways(z, o - 1, 1, 1)
            else:  # last_digit == 1
                if last_run < limit:
                    total_ways += count_ways(z, o - 1, 1, last_run + 1)
                # We can always add a 0
                total_ways += count_ways(z - 1, o, 0, 1)
            
            # Store the result in the memo dictionary
            memo[key] = total_ways % MOD
            return memo[key]
        
        # Start the recursion with the first digit being either 0 or 1
        # We start with a run length of 1 for the first digit
        total_stable_arrays = (count_ways(zero - 1, one, 0, 1) + count_ways(zero, one - 1, 1, 1)) % MOD
        return total_stable_arrays

def numberOfStableArrays(zero: int, one: int, limit: int) -> int:
    return Solution().numberOfStableArrays(zero, one, limit)