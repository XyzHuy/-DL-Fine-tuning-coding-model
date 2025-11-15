import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find the largest number and its index
        max_num = max(nums)
        max_index = nums.index(max_num)
        
        # Check if the largest number is at least twice as much as every other number
        for num in nums:
            if num != max_num and max_num < 2 * num:
                return -1
        
        return max_index

def dominantIndex(nums: List[int]) -> int:
    return Solution().dominantIndex(nums)