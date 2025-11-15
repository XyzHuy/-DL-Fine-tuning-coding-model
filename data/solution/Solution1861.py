import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Apply gravity to each row
        for i in range(m):
            # Find the position where the next stone can fall
            last_empty = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    # If there's an obstacle, update the last_empty position
                    last_empty = j - 1
                elif boxGrid[i][j] == '#':
                    # Swap the stone with the last empty position
                    boxGrid[i][j], boxGrid[i][last_empty] = boxGrid[i][last_empty], boxGrid[i][j]
                    # Update the last_empty position
                    last_empty -= 1
        
        # Rotate the box 90 degrees clockwise
        rotated_box = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated_box[j][m - 1 - i] = boxGrid[i][j]
        
        return rotated_box

def rotateTheBox(boxGrid: List[List[str]]) -> List[List[str]]:
    return Solution().rotateTheBox(boxGrid)