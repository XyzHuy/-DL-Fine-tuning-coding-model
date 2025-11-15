import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate the area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        
        # Calculate the area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)
        
        # Calculate the overlap in the x-dimension
        overlap_x = max(0, min(ax2, bx2) - max(ax1, bx1))
        
        # Calculate the overlap in the y-dimension
        overlap_y = max(0, min(ay2, by2) - max(ay1, by1))
        
        # Calculate the area of the overlap
        overlap_area = overlap_x * overlap_y
        
        # Total area is the sum of the areas minus the overlap
        total_area = area1 + area2 - overlap_area
        
        return total_area

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    return Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)