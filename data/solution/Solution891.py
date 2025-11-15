import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        total_sum = 0
        power = [1] * n
        
        # Precompute powers of 2 modulo MOD
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD
        
        # Calculate the sum of widths
        for i in range(n):
            total_sum = (total_sum + nums[i] * (power[i] - power[n - i - 1])) % MOD
        
        return total_sum

def sumSubseqWidths(nums: List[int]) -> int:
    return Solution().sumSubseqWidths(nums)