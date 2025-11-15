import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Using two pointers to partition the array
        left, right = 0, len(nums) - 1
        
        while left < right:
            # If the left pointer is even, move it to the right
            if nums[left] % 2 == 0:
                left += 1
            # If the right pointer is odd, move it to the left
            elif nums[right] % 2 == 1:
                right -= 1
            # If left is odd and right is even, swap them
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        return nums

def sortArrayByParity(nums: List[int]) -> List[int]:
    return Solution().sortArrayByParity(nums)