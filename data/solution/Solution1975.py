import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0
        
        for row in matrix:
            for num in row:
                total_sum += abs(num)
                min_abs_value = min(min_abs_value, abs(num))
                if num < 0:
                    negative_count += 1
        
        # If the count of negative numbers is even, we can make all numbers positive
        # If the count of negative numbers is odd, we can make all but one number positive
        # The one negative number will be the one with the smallest absolute value
        if negative_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_value

def maxMatrixSum(matrix: List[List[int]]) -> int:
    return Solution().maxMatrixSum(matrix)