import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_value = float('-inf')
        # Deque to store pairs of (yi - xi, xi)
        deque_x = deque()
        
        for xj, yj in points:
            # Remove points from the deque that do not satisfy the condition |xj - xi| <= k
            while deque_x and xj - deque_x[0][1] > k:
                deque_x.popleft()
            
            # If the deque is not empty, calculate the equation value
            if deque_x:
                max_value = max(max_value, yj + xj + deque_x[0][0])
            
            # Maintain the deque in decreasing order of (yi - xi)
            while deque_x and yj - xj >= deque_x[-1][0]:
                deque_x.pop()
            
            # Add the current point to the deque
            deque_x.append((yj - xj, xj))
        
        return max_value

def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
    return Solution().findMaxValueOfEquation(points, k)