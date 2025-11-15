import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to use the two-pointer technique
        closest_sum = float('inf')  # Initialize the closest sum to a large number
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Check if the current sum is closer to the target than the closest sum found so far
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move the pointers based on the comparison with the target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the current sum is exactly equal to the target, return it immediately
                    return current_sum
        
        return closest_sum

def threeSumClosest(nums: List[int], target: int) -> int:
    return Solution().threeSumClosest(nums, target)