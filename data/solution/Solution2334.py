import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums = [0] + nums + [0]  # Add sentinel values to handle edge cases
        stack = []
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                j = stack.pop()
                k = i - stack[-1] - 1  # Length of the subarray
                if nums[j] > threshold / k:
                    return k
            stack.append(i)
        
        return -1

# Example usage:
# sol = Solution()
# print(sol.validSubarraySize([1, 3, 4, 3, 1], 6))  # Output: 3
# print(sol.validSubarraySize([6, 5, 6, 5, 8], 7))  # Output: 1

def validSubarraySize(nums: List[int], threshold: int) -> int:
    return Solution().validSubarraySize(nums, threshold)