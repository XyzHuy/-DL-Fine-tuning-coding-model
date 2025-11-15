import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Sort the array to find the two largest and two smallest numbers
        nums.sort()
        
        # The two largest numbers will be the last two elements
        max1, max2 = nums[-1], nums[-2]
        
        # The two smallest numbers will be the first two elements
        min1, min2 = nums[0], nums[1]
        
        # Calculate the product difference
        product_difference = (max1 * max2) - (min1 * min2)
        
        return product_difference

def maxProductDifference(nums: List[int]) -> int:
    return Solution().maxProductDifference(nums)