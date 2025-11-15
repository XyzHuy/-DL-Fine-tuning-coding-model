import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        total_subarrays = 0
        
        # Function to check if a list is strictly increasing
        def is_strictly_increasing(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
        
        # Check all possible subarrays
        for start in range(n):
            for end in range(start + 1, n + 1):
                # Remove the subarray nums[start:end]
                remaining = nums[:start] + nums[end:]
                if is_strictly_increasing(remaining):
                    total_subarrays += 1
        
        return total_subarrays

# Example usage:
# sol = Solution()
# print(sol.incremovableSubarrayCount([1, 2, 3, 4]))  # Output: 10
# print(sol.incremovableSubarrayCount([6, 5, 7, 8]))  # Output: 7
# print(sol.incremovableSubarrayCount([8, 7, 6, 6]))  # Output: 3

def incremovableSubarrayCount(nums: List[int]) -> int:
    return Solution().incremovableSubarrayCount(nums)