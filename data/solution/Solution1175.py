import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime_count = n - prime_count
        
        def factorial(x):
            result = 1
            for i in range(2, x + 1):
                result = (result * i) % (10**9 + 7)
            return result
        
        return (factorial(prime_count) * factorial(non_prime_count)) % (10**9 + 7)

def numPrimeArrangements(n: int) -> int:
    return Solution().numPrimeArrangements(n)