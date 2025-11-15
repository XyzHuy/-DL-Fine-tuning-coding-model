import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Move the left pointer to the right, skipping duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer to the left, skipping duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

def threeSum(nums: List[int]) -> List[List[int]]:
    return Solution().threeSum(nums)