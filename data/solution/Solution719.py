import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort the array to facilitate the two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Helper function to count the number of pairs with distance <= mid
        def count_pairs(mid: int) -> int:
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        # Binary search for the smallest distance
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

def smallestDistancePair(nums: List[int], k: int) -> int:
    return Solution().smallestDistancePair(nums, k)