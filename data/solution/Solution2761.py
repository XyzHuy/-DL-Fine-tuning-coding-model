import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 4:
            return []
        
        # Step 1: Generate all prime numbers up to n using the Sieve of Eratosthenes
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        
        # Step 2: Find all prime pairs (x, y) such that x + y = n
        prime_pairs = []
        for x in range(2, n // 2 + 1):
            if is_prime[x] and is_prime[n - x]:
                prime_pairs.append([x, n - x])
        
        return prime_pairs

def findPrimePairs(n: int) -> List[List[int]]:
    return Solution().findPrimePairs(n)