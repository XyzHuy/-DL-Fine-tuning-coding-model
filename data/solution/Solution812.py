import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangle_area(p1, p2, p3):
            # Using the Shoelace formula (or Gauss's area formula) for the area of a triangle given its vertices
            return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2.0)
        
        max_area = 0.0
        n = len(points)
        
        # Check all combinations of three points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    max_area = max(max_area, triangle_area(points[i], points[j], points[k]))
        
        return max_area

def largestTriangleArea(points: List[List[int]]) -> float:
    return Solution().largestTriangleArea(points)