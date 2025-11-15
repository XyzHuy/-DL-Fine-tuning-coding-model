import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        
        # If nums1 can be made larger or equal by replacing zeros
        if sum1 + zeros1 > sum2 + zeros2:
            if zeros2 == 0:
                return -1
            if sum1 + zeros1 < sum2 + 1:
                return -1
        # If nums2 can be made larger or equal by replacing zeros
        elif sum1 + zeros1 < sum2 + zeros2:
            if zeros1 == 0:
                return -1
            if sum2 + zeros2 < sum1 + 1:
                return -1
        # If both sums are equal without considering zeros
        else:
            if zeros1 == 0 and zeros2 == 0:
                return sum1
            if zeros1 == 0:
                return sum2 + zeros2
            if zeros2 == 0:
                return sum1 + zeros1
        
        # Calculate the minimum possible equal sum
        return max(sum1 + zeros1, sum2 + zeros2)

def minSum(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minSum(nums1, nums2)