import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        n = len(nums)
        left, right = 0, n - 1
        count = 0
        
        # Precompute powers of 2 up to n
        power_of_2 = [1] * n
        for i in range(1, n):
            power_of_2[i] = (power_of_2[i - 1] * 2) % mod
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + power_of_2[right - left]) % mod
                left += 1
            else:
                right -= 1
        
        return count

def numSubseq(nums: List[int], target: int) -> int:
    return Solution().numSubseq(nums, target)