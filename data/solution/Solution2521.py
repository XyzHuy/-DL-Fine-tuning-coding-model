import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import sqrt

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(n):
            factors = set()
            # Check for number of 2s in n
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            # Check for odd factors from 3 to sqrt(n)
            for i in range(3, int(sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            # If n is a prime number greater than 2
            if n > 2:
                factors.add(n)
            return factors
        
        distinct_factors = set()
        for num in nums:
            distinct_factors.update(prime_factors(num))
        
        return len(distinct_factors)

# Example usage:
# sol = Solution()
# print(sol.distinctPrimeFactors([2,4,3,7,10,6]))  # Output: 4
# print(sol.distinctPrimeFactors([2,4,8,16]))     # Output: 1

def distinctPrimeFactors(nums: List[int]) -> int:
    return Solution().distinctPrimeFactors(nums)