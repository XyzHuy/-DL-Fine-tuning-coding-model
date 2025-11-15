import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        position = n - 1
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
            
            position -= 1
        
        return result

def sortedSquares(nums: List[int]) -> List[int]:
    return Solution().sortedSquares(nums)