import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def cross_product(o, a, b):
            # Calculate the cross product of vectors OA and OB
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        n = len(points)
        if n < 3:
            return False  # A polygon must have at least 3 points
        
        # Determine the initial orientation
        prev_cross_product = 0
        
        for i in range(n):
            o = points[i]
            a = points[(i + 1) % n]
            b = points[(i + 2) % n]
            
            current_cross_product = cross_product(o, a, b)
            
            if current_cross_product != 0:
                if prev_cross_product * current_cross_product < 0:
                    return False
                prev_cross_product = current_cross_product
        
        return True

def isConvex(points: List[List[int]]) -> bool:
    return Solution().isConvex(points)