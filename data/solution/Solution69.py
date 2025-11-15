import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right

def mySqrt(x: int) -> int:
    return Solution().mySqrt(x)