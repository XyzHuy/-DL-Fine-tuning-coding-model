import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        # Sort the array to find the median
        nums.sort()
        n = len(nums)
        
        # Find the median index
        median_index = n // 2
        
        # Calculate the number of operations needed to make the median equal to k
        operations = 0
        if nums[median_index] < k:
            while median_index < n and nums[median_index] < k:
                operations += k - nums[median_index]
                median_index += 1
        elif nums[median_index] > k:
            while median_index >= 0 and nums[median_index] > k:
                operations += nums[median_index] - k
                median_index -= 1
        
        return operations

# Example usage:
# sol = Solution()
# print(sol.minOperationsToMakeMedianK([2,5,6,8,5], 4))  # Output: 2
# print(sol.minOperationsToMakeMedianK([2,5,6,8,5], 7))  # Output: 3
# print(sol.minOperationsToMakeMedianK([1,2,3,4,5,6], 4))  # Output: 0

def minOperationsToMakeMedianK(nums: List[int], k: int) -> int:
    return Solution().minOperationsToMakeMedianK(nums, k)