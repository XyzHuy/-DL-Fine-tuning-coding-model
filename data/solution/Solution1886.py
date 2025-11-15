import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Function to rotate the matrix 90 degrees clockwise
        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            return [list(reversed(col)) for col in zip(*matrix)]
        
        # Check if the matrices are already equal
        if mat == target:
            return True
        
        # Try rotating the matrix up to 3 times (90, 180, 270 degrees)
        for _ in range(3):
            mat = rotate(mat)
            if mat == target:
                return True
        
        # If no rotation matches the target, return False
        return False

def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    return Solution().findRotation(mat, target)