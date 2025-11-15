import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        # If the array is too short to satisfy the indexDifference, return [-1, -1]
        if n < indexDifference:
            return [-1, -1]
        
        # Initialize variables to track the minimum and maximum values and their indices
        min_index = max_index = 0
        
        for j in range(indexDifference, n):
            i = j - indexDifference
            
            # Update the min_index and max_index for the subarray nums[0:i+1]
            if nums[i] < nums[min_index]:
                min_index = i
            if nums[i] > nums[max_index]:
                max_index = i
            
            # Check if the current j and min_index satisfy the conditions
            if nums[j] - nums[min_index] >= valueDifference:
                return [min_index, j]
            
            # Check if the current j and max_index satisfy the conditions
            if nums[max_index] - nums[j] >= valueDifference:
                return [max_index, j]
        
        return [-1, -1]

def findIndices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    return Solution().findIndices(nums, indexDifference, valueDifference)