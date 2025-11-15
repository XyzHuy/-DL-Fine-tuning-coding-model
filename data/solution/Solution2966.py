import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Sort the array to make it easier to find groups with minimal differences
        nums.sort()
        result = []
        
        # Iterate through the sorted array in steps of 3
        for i in range(0, len(nums), 3):
            # Check if the difference between the max and min in the current group is <= k
            if nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                # If any group fails the condition, return an empty array
                return []
        
        return result

def divideArray(nums: List[int], k: int) -> List[List[int]]:
    return Solution().divideArray(nums, k)