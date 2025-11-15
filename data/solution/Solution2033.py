import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a single list
        nums = [num for row in grid for num in row]
        
        # Check if it's possible to make all elements equal
        # All elements must have the same remainder when divided by x
        remainder = nums[0] % x
        if not all(num % x == remainder for num in nums):
            return -1
        
        # Sort the numbers to find the median
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Calculate the number of operations needed to make all elements equal to the median
        operations = sum(abs(num - median) for num in nums) // x
        
        return operations

def minOperations(grid: List[List[int]], x: int) -> int:
    return Solution().minOperations(grid, x)