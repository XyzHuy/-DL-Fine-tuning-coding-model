import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def largestVariance(self, s: str) -> int:
        from itertools import permutations
        
        max_variance = 0
        unique_chars = set(s)
        
        for x, y in permutations(unique_chars, 2):
            count_x = count_y = 0
            has_x = has_y = False
            for char in s:
                if char == x:
                    count_x += 1
                    has_x = True
                elif char == y:
                    count_y += 1
                    has_y = True
                
                if count_y > count_x:
                    count_x = count_y = 0
                elif count_x > 0 and count_y > 0:
                    max_variance = max(max_variance, count_x - count_y)
            
            if has_x and has_y and count_x > count_y:
                max_variance = max(max_variance, count_x - count_y - 1)
        
        return max_variance

def largestVariance(s: str) -> int:
    return Solution().largestVariance(s)