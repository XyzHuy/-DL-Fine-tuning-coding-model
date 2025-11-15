import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        
        # Memoization table
        from functools import lru_cache
        
        @lru_cache(None)
        def dp(start, prev):
            if start == n:
                return 1
            if num[start] == '0':
                return 0
            
            count = 0
            for end in range(start + 1, n + 1):
                current = num[start:end]
                if len(current) > len(prev) or (len(current) == len(prev) and current >= prev):
                    count = (count + dp(end, current)) % MOD
            return count 
        
        return dp(0, "")

# Example usage:
# sol = Solution()
# print(sol.numberOfCombinations("327"))  # Output: 2
# print(sol.numberOfCombinations("094"))  # Output: 0
# print(sol.numberOfCombinations("0"))    # Output: 0

def numberOfCombinations(num: str) -> int:
    return Solution().numberOfCombinations(num)