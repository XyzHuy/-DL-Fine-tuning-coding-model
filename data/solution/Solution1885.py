import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # Calculate the difference array
        diff = [n1 - n2 for n1, n2 in zip(nums1, nums2)]
        
        # Sort the difference array
        diff.sort()
        
        left, right = 0, len(diff) - 1
        count = 0
        
        # Use two pointers to count the valid pairs
        while left < right:
            if diff[left] + diff[right] > 0:
                # If the sum of diff[left] and diff[right] is greater than 0,
                # then all pairs (left, left+1), (left, left+2), ..., (left, right) are valid
                count += right - left
                right -= 1
            else:
                left += 1
        
        return count

def countPairs(nums1: List[int], nums2: List[int]) -> int:
    return Solution().countPairs(nums1, nums2)