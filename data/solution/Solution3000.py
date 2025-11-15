import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        
        for length, width in dimensions:
            diagonal = math.sqrt(length * length + width * width)
            area = length * width
            
            if diagonal > max_diagonal or (diagonal == max_diagonal and area > max_area):
                max_diagonal = diagonal
                max_area = area
        
        return max_area

def areaOfMaxDiagonal(dimensions: List[List[int]]) -> int:
    return Solution().areaOfMaxDiagonal(dimensions)