import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Sort the array to make it easier to handle duplicates
        nums.sort()
        
        # Initialize the number of moves to 0
        moves = 0
        
        # Iterate through the sorted array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not greater than the previous one
            if nums[i] <= nums[i - 1]:
                # Calculate the number of moves needed to make nums[i] unique
                increment = nums[i - 1] - nums[i] + 1
                # Add the increment to the total number of moves
                moves += increment
                # Increment nums[i] to make it unique
                nums[i] += increment
        
        return moves

def minIncrementForUnique(nums: List[int]) -> int:
    return Solution().minIncrementForUnique(nums)