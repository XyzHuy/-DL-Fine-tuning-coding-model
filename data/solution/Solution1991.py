import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Subtract the current element from the total sum to get the right sum
            total_sum -= num
            
            # Check if left sum equals right sum
            if left_sum == total_sum:
                return i
            
            # Add the current element to the left sum
            left_sum += num
        
        return -1

def findMiddleIndex(nums: List[int]) -> int:
    return Solution().findMiddleIndex(nums)