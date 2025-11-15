import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def possible(mid):
            # Calculate the sum of the left part of the array
            if mid > index:
                left_sum = (mid - 1 + mid - index) * index // 2
            else:
                left_sum = (mid - 1 + 1) * (mid - 1) // 2 + (index - mid + 1)
            
            # Calculate the sum of the right part of the array
            if mid > n - index - 1:
                right_sum = (mid - 1 + mid - n + index + 1) * (n - index - 1) // 2
            else:
                right_sum = (mid - 1 + 1) * (mid - 1) // 2 + (n - index - mid)
            
            # Total sum with the current mid at index
            total_sum = left_sum + mid + right_sum
            return total_sum <= maxSum
        
        low, high = 1, maxSum
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if possible(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result

def maxValue(n: int, index: int, maxSum: int) -> int:
    return Solution().maxValue(n, index, maxSum)