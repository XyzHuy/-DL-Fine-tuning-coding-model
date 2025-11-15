import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Create a list of tuples (value, index) and sort it by value
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        
        # Initialize a list to store the result
        result = [0] * len(nums)
        
        # Iterate through the sorted list and group indices that can be swapped
        i = 0
        while i < len(indexed_nums):
            # Start a new group
            group_values = []
            group_indices = []
            
            # Add elements to the group as long as the condition |nums[i] - nums[j]| <= limit is satisfied
            while i < len(indexed_nums) - 1 and indexed_nums[i + 1][0] - indexed_nums[i][0] <= limit:
                group_values.append(indexed_nums[i][0])
                group_indices.append(indexed_nums[i][1])
                i += 1
            
            # Add the last element of the current group
            group_values.append(indexed_nums[i][0])
            group_indices.append(indexed_nums[i][1])
            
            # Sort the indices and place the smallest values in the correct positions
            group_indices.sort()
            for j, index in enumerate(group_indices):
                result[index] = group_values[j]
            
            # Move to the next group
            i += 1
        
        return result

def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    return Solution().lexicographicallySmallestArray(nums, limit)