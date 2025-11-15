import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than n
        
        # Helper function to reverse a portion of the array
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Reverse the whole array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the remaining n-k elements
        reverse(k, n - 1)

def rotate(nums: List[int], k: int) -> None:
    return Solution().rotate(nums, k)