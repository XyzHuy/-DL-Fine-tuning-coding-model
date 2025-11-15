import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = -1
        
        for num in nums:
            current_num = num
            length = 1
            while current_num * current_num in num_set:
                current_num *= current_num
                length += 1
            
            if length > 1:
                max_length = max(max_length, length)
        
        return max_length

def longestSquareStreak(nums: List[int]) -> int:
    return Solution().longestSquareStreak(nums)