import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        total_power = 0
        prefix_sum = 0
        
        for num in nums:
            # For each number, it can be the maximum in several groups
            # The power of these groups is num^2 * (each possible minimum)
            # The possible minimums are all the numbers before it in the sorted list
            # We use prefix_sum to keep track of the sum of all possible minimums
            total_power = (total_power + num * num % MOD * (num + prefix_sum)) % MOD
            # Update prefix_sum to include the current number
            # Each number can be a minimum for 2^i new groups where i is its index
            prefix_sum = (2 * prefix_sum + num) % MOD
        
        return total_power

def sumOfPower(nums: List[int]) -> int:
    return Solution().sumOfPower(nums)