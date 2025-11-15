import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_of_prime_factors(n: int) -> int:
            sum_factors = 0
            # Check for number of 2s that divide n
            while n % 2 == 0:
                sum_factors += 2
                n //= 2
            # n must be odd at this point, so a skip of 2 (i.e., i = i + 2) can be used
            for i in range(3, int(n**0.5) + 1, 2):
                # While i divides n, add i and divide n
                while n % i == 0:
                    sum_factors += i
                    n //= i
            # This condition is to check if n is a prime number greater than 2
            if n > 2:
                sum_factors += n
            return sum_factors
        
        # Continue replacing n with the sum of its prime factors until it stabilizes
        while True:
            next_n = sum_of_prime_factors(n)
            if next_n == n:
                break
            n = next_n
        
        return n

# Example usage:
# sol = Solution()
# print(sol.smallestValue(15))  # Output: 5
# print(sol.smallestValue(3))   # Output: 3

def smallestValue(n: int) -> int:
    return Solution().smallestValue(n)