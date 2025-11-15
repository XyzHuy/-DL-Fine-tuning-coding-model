import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == mid:
                # Check if this is the smallest index
                if mid == 0 or arr[mid - 1] != mid - 1:
                    return mid
                else:
                    right = mid - 1
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

# Example usage:
# sol = Solution()
# print(sol.fixedPoint([-10, -5, 0, 3, 7]))  # Output: 3
# print(sol.fixedPoint([0, 2, 5, 8, 17]))  # Output: 0
# print(sol.fixedPoint([-10, -5, 3, 4, 7, 9]))  # Output: -1

def fixedPoint(arr: List[int]) -> int:
    return Solution().fixedPoint(arr)