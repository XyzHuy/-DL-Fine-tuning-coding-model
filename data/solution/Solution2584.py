import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import math

def prime_factors(n):
    factors = defaultdict(int)
    # Check for number of 2s
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    # Check for odd factors from 3 onwards
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        factors[n] += 1
    return factors

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return -1
        
        # Prime factorization for all numbers
        pf = [prime_factors(num) for num in nums]
        
        # Prefix and suffix prime factor counters
        prefix_pf = defaultdict(int)
        suffix_pf = defaultdict(int)
        
        # Initialize suffix_prime_factors with all factors
        for factors in pf:
            for prime, count in factors.items():
                suffix_pf[prime] += count
        
        for i in range(n - 1):
            # Add current number's factors to prefix
            for prime, count in pf[i].items():
                prefix_pf[prime] += count
            # Subtract current number's factors from suffix
            for prime, count in pf[i].items():
                suffix_pf[prime] -= count
                if suffix_pf[prime] == 0:
                    del suffix_pf[prime]
            
            # Check if prefix and suffix are coprime
            if not (prefix_pf.keys() & suffix_pf.keys()):
                return i
        
        return -1

# Example usage:
# sol = Solution()
# print(sol.findValidSplit([4,7,8,15,3,5]))  # Output: 2
# print(sol.findValidSplit([4,7,15,8,3,5]))  # Output: -1

def findValidSplit(nums: List[int]) -> int:
    return Solution().findValidSplit(nums)