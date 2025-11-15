import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def count_valid_subarrays_with_max_length(max_length):
            count = 0
            current_min = float('inf')
            current_max = float('-inf')
            left = 0
            
            for right in range(len(nums)):
                current_min = min(current_min, nums[right])
                current_max = max(current_max, nums[right])
                
                while (current_min < minK or current_max > maxK) and left <= right:
                    if nums[left] == current_min:
                        current_min = min(nums[left+1:right+1], default=float('inf'))
                    if nums[left] == current_max:
                        current_max = max(nums[left+1:right+1], default=float('-inf'))
                    left += 1
                
                if current_min == minK and current_max == maxK:
                    count += left + 1
                
            return count
        
        def count_valid_subarrays():
            return count_valid_subarrays_with_max_length(len(nums))
        
        return count_valid_subarrays()

# Optimized Solution
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left_bound = -1
        min_pos = -1
        max_pos = -1
        count = 0
        
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left_bound = i
            
            if nums[i] == minK:
                min_pos = i
            if nums[i] == maxK:
                max_pos = i
            
            count += max(0, min(min_pos, max_pos) - left_bound)
        
        return count

def countSubarrays(nums: List[int], minK: int, maxK: int) -> int:
    return Solution().countSubarrays(nums, minK, maxK)