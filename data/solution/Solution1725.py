import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # Calculate the possible square side lengths for each rectangle
        squares = [min(l, w) for l, w in rectangles]
        
        # Find the maximum square side length
        maxLen = max(squares)
        
        # Count how many rectangles can form a square with side length maxLen
        return squares.count(maxLen)

def countGoodRectangles(rectangles: List[List[int]]) -> int:
    return Solution().countGoodRectangles(rectangles)