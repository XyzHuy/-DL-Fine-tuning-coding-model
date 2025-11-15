import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        partitions = 0
        
        for right in range(len(nums)):
            if nums[right] - nums[left] > k:
                partitions += 1
                left = right
        
        # Add the last partition
        partitions += 1
        
        return partitions

def partitionArray(nums: List[int], k: int) -> int:
    return Solution().partitionArray(nums, k)