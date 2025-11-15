import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the numbers and their indices
        num_to_index = {}
        
        # Iterate over the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index

def twoSum(nums: List[int], target: int) -> List[int]:
    return Solution().twoSum(nums, target)