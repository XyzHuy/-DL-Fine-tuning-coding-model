import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Helper function to count the number of missing elements up to index i
        def count_missing(i):
            return nums[i] - nums[0] - i
        
        # Total number of missing elements in the entire array
        total_missing = count_missing(len(nums) - 1)
        
        # If k is greater than the total number of missing elements in the array,
        # the kth missing number is beyond the last element of the array
        if k > total_missing:
            return nums[-1] + k - total_missing
        
        # Binary search to find the first position where the number of missing elements is >= k
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            missing_up_to_mid = count_missing(mid)
            if missing_up_to_mid < k:
                left = mid + 1
            else:
                right = mid
        
        # After the binary search, left is the smallest index where the number of missing elements is >= k
        # The kth missing number is then nums[left - 1] + (k - missing_up_to_left_minus_1)
        return nums[left - 1] + (k - count_missing(left - 1))

def missingElement(nums: List[int], k: int) -> int:
    return Solution().missingElement(nums, k)