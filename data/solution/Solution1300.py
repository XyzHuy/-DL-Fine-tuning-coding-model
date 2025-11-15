import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def array_sum_with_value(val):
            return sum(min(a, val) for a in arr)
        
        left, right = 0, max(arr)
        best_value = left
        min_diff = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            current_sum = array_sum_with_value(mid)
            current_diff = abs(current_sum - target)
            
            if current_diff < min_diff or (current_diff == min_diff and mid < best_value):
                min_diff = current_diff
                best_value = mid
            
            if current_sum < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return best_value

def findBestValue(arr: List[int], target: int) -> int:
    return Solution().findBestValue(arr, target)