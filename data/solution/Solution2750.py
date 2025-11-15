import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        first_one_index = -1
        last_one_index = -1
        count = 1
        
        # Find the first and last occurrence of 1
        for i, num in enumerate(nums):
            if num == 1:
                if first_one_index == -1:
                    first_one_index = i
                last_one_index = i
        
        # If there are no 1s in the array, there are no good subarrays
        if first_one_index == -1:
            return 0
        
        # Iterate through the array between the first and last 1
        for i in range(first_one_index, last_one_index + 1):
            if nums[i] == 1:
                # Calculate the number of zeros between consecutive 1s
                if i > first_one_index and nums[i - 1] == 0:
                    zeros_between = 0
                    j = i - 1
                    while j >= first_one_index and nums[j] == 0:
                        zeros_between += 1
                        j -= 1
                    count = (count * (zeros_between + 1)) % MOD
        
        return count

def numberOfGoodSubarraySplits(nums: List[int]) -> int:
    return Solution().numberOfGoodSubarraySplits(nums)