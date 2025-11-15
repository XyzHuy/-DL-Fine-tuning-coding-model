import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Find the two largest numbers in the list
        first_max = second_max = float('-inf')
        
        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        # Calculate the maximum product of (nums[i]-1)*(nums[j]-1)
        return (first_max - 1) * (second_max - 1)

def maxProduct(nums: List[int]) -> int:
    return Solution().maxProduct(nums)