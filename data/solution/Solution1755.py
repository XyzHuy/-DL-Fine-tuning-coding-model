import random
import functools
import collections
import string
import math
import datetime


from itertools import combinations
from typing import List

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mid = n // 2
        
        # Generate all possible sums for the first half and the second half
        left_sums = {sum(comb) for i in range(mid + 1) for comb in combinations(nums[:mid], i)}
        right_sums = sorted({sum(comb) for i in range(n - mid + 1) for comb in combinations(nums[mid:], i)})
        
        min_diff = float('inf')
        
        # For each sum in the left half, find the closest sum in the right half
        for left_sum in left_sums:
            target = goal - left_sum
            pos = self.binary_search(right_sums, target)
            
            # Check the closest sums around the target
            if pos < len(right_sums):
                min_diff = min(min_diff, abs(left_sum + right_sums[pos] - goal))
            if pos > 0:
                min_diff = min(min_diff, abs(left_sum + right_sums[pos - 1] - goal))
        
        return min_diff
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

def minAbsDifference(nums: List[int], goal: int) -> int:
    return Solution().minAbsDifference(nums, goal)