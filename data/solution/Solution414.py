import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Initialize three variables to store the first, second, and third maximums
        first = second = third = float('-inf')
        
        for num in nums:
            # Skip if the number is already one of the maximums
            if num in (first, second, third):
                continue
            
            # Update the maximums accordingly
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        # If third is still negative infinity, it means there were less than 3 distinct numbers
        return first if third == float('-inf') else third

def thirdMax(nums: List[int]) -> int:
    return Solution().thirdMax(nums)