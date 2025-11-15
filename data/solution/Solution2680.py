import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_or = [0] * (n + 1)
        suffix_or = [0] * (n + 1)
        
        # Calculate prefix OR values
        for i in range(n):
            prefix_or[i + 1] = prefix_or[i] | nums[i]
        
        # Calculate suffix OR values
        for i in range(n - 1, -1, -1):
            suffix_or[i] = suffix_or[i + 1] | nums[i]
        
        max_or = 0
        for i in range(n):
            # Calculate the new OR value if we multiply nums[i] by 2^k
            new_value = nums[i] << k
            current_or = prefix_or[i] | new_value | suffix_or[i + 1]
            max_or = max(max_or, current_or)
        
        return max_or

def maximumOr(nums: List[int], k: int) -> int:
    return Solution().maximumOr(nums, k)