import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        prime_set = set(primes)
        
        # Function to get the bitmask for prime factors
        def get_prime_mask(num):
            mask = 0
            for i, prime in enumerate(primes):
                if num % prime == 0:
                    # If num is divisible by prime^2, it's not a good subset
                    if num % (prime * prime) == 0:
                        return 0
                    mask |= (1 << i)
            return mask
        
        # Count the frequency of each number in nums
        num_count = Counter(nums)
        
        # Dynamic programming array to store the number of good subsets for each bitmask
        dp = [0] * (1 << len(primes))
        dp[0] = 1  # The empty subset
        
        # Iterate over each number from 2 to 30
        for num in range(2, 31):
            if num not in num_count:
                continue
            mask = get_prime_mask(num)
            if mask == 0:
                continue
            # Update the dp array for each subset
            for i in range((1 << len(primes)) - 1, -1, -1):
                if (i & mask) == 0:
                    dp[i | mask] = (dp[i | mask] + dp[i] * num_count[num]) % mod
        
        # Sum up all the good subsets excluding the empty subset
        ans = sum(dp[1:]) % mod
        
        # Handle the special case of the number 1
        for _ in range(num_count[1]):
            ans = (ans * 2) % mod
        
        return ans

def numberOfGoodSubsets(nums: List[int]) -> int:
    return Solution().numberOfGoodSubsets(nums)