import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        i = 0
        
        # Iterate through the array with the adjusted index
        while i < len(nums) - 1:
            # If the current index (after deletions) is even and nums[i] == nums[i + 1]
            if (i - deletions) % 2 == 0 and nums[i] == nums[i + 1]:
                deletions += 1
            else:
                i += 1
        
        # If the length of the resulting array is odd, we need one more deletion
        if (len(nums) - deletions) % 2 != 0:
            deletions += 1
        
        return deletions

def minDeletion(nums: List[int]) -> int:
    return Solution().minDeletion(nums)