import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left_max = [0] * n
        right_min = [0] * n
        
        # Fill left_max array
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])
        
        # Fill right_min array
        right_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])
        
        # Calculate the sum of beauties
        beauty_sum = 0
        for i in range(1, n - 1):
            if left_max[i - 1] < nums[i] < right_min[i + 1]:
                beauty_sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty_sum += 1
        
        return beauty_sum

def sumOfBeauties(nums: List[int]) -> int:
    return Solution().sumOfBeauties(nums)