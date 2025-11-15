import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # Directions: east, south, west, north
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0  # Start moving east
        steps = 0
        count = 1  # We start at the initial position
        result = [[rStart, cStart]]
        
        while count < rows * cols:
            # Change direction every two turns (e.g., after going east, go south, then two turns later, go west)
            if direction_index % 2 == 0:
                steps += 1
            
            for _ in range(steps):
                rStart += directions[direction_index][0]
                cStart += directions[direction_index][1]
                
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    result.append([rStart, cStart])
                    count += 1
                    
                    if count == rows * cols:
                        break
            
            direction_index = (direction_index + 1) % 4
        
        return result

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    return Solution().spiralMatrixIII(rows, cols, rStart, cStart)