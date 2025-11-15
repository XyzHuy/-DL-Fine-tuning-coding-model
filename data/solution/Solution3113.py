import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        # Iterate over each element in the array
        for i in range(n):
            max_num = nums[i]
            # Check all subarrays starting from index i
            for j in range(i, n):
                # Update the maximum number in the current subarray
                if nums[j] > max_num:
                    max_num = nums[j]
                # If the first and last elements of the subarray are equal to the max_num
                if nums[i] == nums[j] == max_num:
                    count += 1
        
        return count

def numberOfSubarrays(nums: List[int]) -> int:
    return Solution().numberOfSubarrays(nums)