import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        import math
        
        def sieve_of_eratosthenes(limit):
            is_prime = [True] * (limit + 1)
            p = 2
            while (p * p <= limit):
                if (is_prime[p] == True):
                    for i in range(p * p, limit + 1, p):
                        is_prime[i] = False
                p += 1
            prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
            return prime_numbers
        
        # Find all primes up to sqrt(r)
        limit = int(math.sqrt(r))
        primes = sieve_of_eratosthenes(limit)
        
        # Count special numbers in the range [l, r]
        special_count = 0
        for prime in primes:
            square = prime * prime
            if l <= square <= r:
                special_count += 1
        
        # Total numbers in the range [l, r]
        total_count = r - l + 1
        
        # Non-special numbers
        non_special_count = total_count - special_count
        return non_special_count

def nonSpecialCount(l: int, r: int) -> int:
    return Solution().nonSpecialCount(l, r)