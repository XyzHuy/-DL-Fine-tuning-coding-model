import random
import functools
import collections
import string
import math
import datetime


from typing import List
import sys

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        # Sort the array to make it easier to find the minimum partition value
        nums.sort()
        
        # Initialize the minimum partition value to a large number
        min_partition_value = sys.maxsize
        
        # Iterate through the sorted array and find the minimum difference between consecutive elements
        for i in range(len(nums) - 1):
            partition_value = abs(nums[i] - nums[i + 1])
            min_partition_value = min(min_partition_value, partition_value)
        
        return min_partition_value

def findValueOfPartition(nums: List[int]) -> int:
    return Solution().findValueOfPartition(nums)