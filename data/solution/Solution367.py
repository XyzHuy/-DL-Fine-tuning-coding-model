import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        left, right = 1, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            if mid_squared == num:
                return True
            elif mid_squared < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

def isPerfectSquare(num: int) -> bool:
    return Solution().isPerfectSquare(num)