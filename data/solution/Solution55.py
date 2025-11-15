import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the farthest index we can reach
        farthest = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is greater than the farthest we can reach, return False
            if i > farthest:
                return False
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            # If the farthest index is or exceeds the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        # If we finish the loop without reaching the last index, return False
        return False

def canJump(nums: List[int]) -> bool:
    return Solution().canJump(nums)