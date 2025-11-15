import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    # If the sum of nums[i], nums[left], and nums[right] is less than the target,
                    # then all sums of nums[i], nums[left], and nums[left+1] to nums[right] are also less than the target.
                    count += right - left
                    left += 1
                else:
                    right -= 1
        
        return count

def threeSumSmaller(nums: List[int], target: int) -> int:
    return Solution().threeSumSmaller(nums, target)