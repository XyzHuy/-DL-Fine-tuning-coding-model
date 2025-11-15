import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        direction = 1  # 1 for up-right, -1 for down-left
        
        for _ in range(m * n):
            result.append(mat[r][c])
            if direction == 1:
                if c == n - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1
        
        return result

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    return Solution().findDiagonalOrder(mat)