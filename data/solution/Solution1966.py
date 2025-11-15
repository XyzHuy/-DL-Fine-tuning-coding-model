import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Initialize left_max and right_min arrays
        left_max = [float('-inf')] * n
        right_min = [float('inf')] * n
        
        # Fill the left_max array
        for i in range(n):
            if i == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i-1], nums[i])
        
        # Fill the right_min array
        for i in range(n-1, -1, -1):
            if i == n-1:
                right_min[i] = nums[i]
            else:
                right_min[i] = min(right_min[i+1], nums[i])
        
        # Count the number of guaranteed elements
        count = 0
        for i in range(n):
            if (i == 0 or nums[i] >= left_max[i-1]) and (i == n-1 or nums[i] <= right_min[i+1]):
                count += 1
        
        return count

# Example usage:
# sol = Solution()
# print(sol.binarySearchableNumbers([7]))  # Output: 1
# print(sol.binarySearchableNumbers([-1, 5, 2]))  # Output: 1

def binarySearchableNumbers(nums: List[int]) -> int:
    return Solution().binarySearchableNumbers(nums)