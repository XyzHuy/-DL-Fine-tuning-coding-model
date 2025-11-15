import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        nums_length = len(nums)
        
        for i in range(nums_length):
            for j in range(i + 1, nums_length):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
                    
        return count

def countKDifference(nums: List[int], k: int) -> int:
    return Solution().countKDifference(nums, k)