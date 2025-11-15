import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # Filter numbers that are even and divisible by 3
        filtered_nums = [num for num in nums if num % 2 == 0 and num % 3 == 0]
        
        # If no numbers satisfy the condition, return 0
        if not filtered_nums:
            return 0
        
        # Calculate the average and round down
        average = sum(filtered_nums) // len(filtered_nums)
        
        return average

def averageValue(nums: List[int]) -> int:
    return Solution().averageValue(nums)