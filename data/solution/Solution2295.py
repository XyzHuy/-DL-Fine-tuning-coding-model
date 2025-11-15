import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # Create a dictionary to map each number to its index in nums
        num_to_index = {num: i for i, num in enumerate(nums)}
        
        # Apply each operation
        for old_value, new_value in operations:
            # Find the index of the old value
            index = num_to_index[old_value]
            # Replace the old value with the new value in nums
            nums[index] = new_value
            # Update the dictionary to reflect the new value's index
            num_to_index[new_value] = index
            # Remove the old value from the dictionary
            del num_to_index[old_value]
        
        return nums

def arrayChange(nums: List[int], operations: List[List[int]]) -> List[int]:
    return Solution().arrayChange(nums, operations)