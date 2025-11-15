import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Initialize the previous index of 1 to a value that will not cause issues
        prev_index = -1
        
        # Iterate over the list to find the positions of 1's
        for i in range(len(nums)):
            if nums[i] == 1:
                # If this is not the first 1 found, check the distance from the previous 1
                if prev_index != -1:
                    if i - prev_index - 1 < k:
                        return False
                # Update the previous index to the current position
                prev_index = i
        
        # If all 1's are at least k places apart, return True
        return True

def kLengthApart(nums: List[int], k: int) -> bool:
    return Solution().kLengthApart(nums, k)