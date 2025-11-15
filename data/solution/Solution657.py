import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Initialize position at the origin
        x, y = 0, 0
        
        # Dictionary to map moves to coordinate changes
        move_map = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        
        # Update position based on each move
        for move in moves:
            dx, dy = move_map[move]
            x += dx
            y += dy
        
        # Check if the robot is back at the origin
        return x == 0 and y == 0

def judgeCircle(moves: str) -> bool:
    return Solution().judgeCircle(moves)