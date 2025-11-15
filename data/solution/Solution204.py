import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a list to track prime status of numbers from 0 to n-1
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        # Use the Sieve of Eratosthenes algorithm
        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start*start, n, start):
                    is_prime[multiple] = False
        
        # Count the number of primes
        return sum(is_prime)

def countPrimes(n: int) -> int:
    return Solution().countPrimes(n)