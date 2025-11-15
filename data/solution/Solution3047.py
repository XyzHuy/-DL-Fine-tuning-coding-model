import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        def intersection_area(bl1, tr1, bl2, tr2):
            # Calculate the intersection rectangle's bottom-left and top-right coordinates
            intersection_bl = [max(bl1[0], bl2[0]), max(bl1[1], bl2[1])]
            intersection_tr = [min(tr1[0], tr2[0]), min(tr1[1], tr2[1])]
            
            # Check if the intersection is valid
            if intersection_bl[0] < intersection_tr[0] and intersection_bl[1] < intersection_tr[1]:
                # Calculate the side length of the largest square that can fit in the intersection
                side_length = min(intersection_tr[0] - intersection_bl[0], intersection_tr[1] - intersection_bl[1])
                return side_length ** 2
            else:
                return 0
        
        max_area = 0
        n = len(bottomLeft)
        
        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                max_area = max(max_area, intersection_area(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j]))
        
        return max_area

def largestSquareArea(bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
    return Solution().largestSquareArea(bottomLeft, topRight)