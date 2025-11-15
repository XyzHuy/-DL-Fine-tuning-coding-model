import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # Convert the list of queens to a set for O(1) lookups
        queens_set = {(x, y) for x, y in queens}
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        attacking_queens = []

        # Check each direction from the king's position
        for dx, dy in directions:
            x, y = king
            # Move in the direction until we go off the board or find a queen
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if (x, y) in queens_set:
                    attacking_queens.append([x, y])
                    break

        return attacking_queens

def queensAttacktheKing(queens: List[List[int]], king: List[int]) -> List[List[int]]:
    return Solution().queensAttacktheKing(queens, king)