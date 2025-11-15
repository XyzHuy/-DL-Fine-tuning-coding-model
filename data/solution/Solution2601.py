import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve_of_eratosthenes(max_num):
            is_prime = [True] * (max_num + 1)
            p = 2
            while (p * p <= max_num):
                if (is_prime[p] == True):
                    for i in range(p * p, max_num + 1, p):
                        is_prime[i] = False
                p += 1
            prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
            return prime_numbers
        
        max_num = max(nums)
        primes = sieve_of_eratosthenes(max_num)
        
        # Check if we can make the array strictly increasing
        prev = 0
        for i in range(len(nums)):
            # Find the largest prime that can be subtracted from nums[i] to keep it greater than prev
            target = nums[i] - prev - 1
            if target < 0:
                return False
            # Find the largest prime less than or equal to target
            j = 0
            while j < len(primes) and primes[j] <= target:
                j += 1
            if j > 0:
                nums[i] -= primes[j - 1]
            prev = nums[i]
        
        return all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))

def primeSubOperation(nums: List[int]) -> bool:
    return Solution().primeSubOperation(nums)