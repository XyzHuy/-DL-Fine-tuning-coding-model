import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive duplicates
        filtered_nums = []
        for num in nums:
            if not filtered_nums or filtered_nums[-1] != num:
                filtered_nums.append(num)
        
        # If after filtering the length is less than 3, no hills or valleys can exist
        if len(filtered_nums) < 3:
            return 0
        
        count = 0
        for i in range(1, len(filtered_nums) - 1):
            left = filtered_nums[i - 1]
            current = filtered_nums[i]
            right = filtered_nums[i + 1]
            
            if current > left and current > right:
                count += 1  # Hill
            elif current < left and current < right:
                count += 1  # Valley
        
        return count

def countHillValley(nums: List[int]) -> int:
    return Solution().countHillValley(nums)