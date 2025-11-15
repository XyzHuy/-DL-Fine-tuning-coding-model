import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Check if the rook can capture the queen in one move
        if a == e or b == f:
            # Check if the bishop is blocking the rook
            if a == e and c == e and ((d - b) * (d - f) < 0):
                return 2
            if b == f and d == f and ((c - a) * (c - e) < 0):
                return 2
            return 1
        
        # Check if the bishop can capture the queen in one move
        if abs(c - e) == abs(d - f):
            # Check if the rook is blocking the bishop
            if abs(c - a) == abs(d - b) and ((b - d) * (b - f) < 0):
                return 2
            return 1
        
        # If neither piece can capture the queen in one move, it will take at least 2 moves
        return 2

def minMovesToCaptureTheQueen(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    return Solution().minMovesToCaptureTheQueen(a, b, c, d, e, f)