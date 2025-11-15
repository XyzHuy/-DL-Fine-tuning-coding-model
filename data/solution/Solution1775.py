import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        
        # Ensure sum1 is the smaller sum and sum2 is the larger sum
        if sum1 > sum2:
            sum1, sum2 = sum2, sum1
            nums1, nums2 = nums2, nums1
        
        # Calculate the difference we need to make
        diff = sum2 - sum1
        
        # Create a list of possible changes we can make
        # We can either increase numbers in nums1 or decrease numbers in nums2
        changes = []
        for num in nums1:
            changes.append(6 - num)  # Maximum increase possible for each number in nums1
        for num in nums2:
            changes.append(num - 1)  # Maximum decrease possible for each number in nums2
        
        # Sort changes in descending order to use the largest possible changes first
        changes.sort(reverse=True)
        
        # Apply the largest possible changes until the difference is closed or exhausted
        operations = 0
        for change in changes:
            diff -= change
            operations += 1
            if diff <= 0:
                return operations
        
        # If we exhaust all changes and still can't make the sums equal, return -1
        return -1

def minOperations(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minOperations(nums1, nums2)