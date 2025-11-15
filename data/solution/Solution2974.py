import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Sort the nums array to easily access the minimum elements
        nums.sort()
        arr = []
        
        # Iterate through the sorted nums array in steps of 2
        for i in range(0, len(nums), 2):
            # Bob appends the element that Alice removes
            arr.append(nums[i + 1])
            # Alice appends the element that she removes
            arr.append(nums[i])
        
        return arr

def numberGame(nums: List[int]) -> List[int]:
    return Solution().numberGame(nums)