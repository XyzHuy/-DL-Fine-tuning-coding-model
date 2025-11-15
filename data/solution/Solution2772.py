import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        operations = [0] * n
        
        for i in range(n):
            if i > 0:
                operations[i] += operations[i - 1]
            
            current_value = nums[i] + operations[i]
            
            if current_value < 0:
                return False
            
            if current_value > 0:
                if i + k > n:
                    return False
                operations[i] -= current_value
                if i + k < n:
                    operations[i + k] += current_value
        
        return all(x == 0 for x in (nums[i] + operations[i] for i in range(n)))

# Example usage:
# sol = Solution()
# print(sol.checkArray([2,2,3,1,1,0], 3))  # Output: True
# print(sol.checkArray([1,3,1,1], 2))      # Output: False

def checkArray(nums: List[int], k: int) -> bool:
    return Solution().checkArray(nums, k)