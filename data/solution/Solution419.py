import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        
        count = 0
        rows, cols = len(board), len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    # Check if it's the start of a battleship
                    if (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                        count += 1
        
        return count

def countBattleships(board: List[List[str]]) -> int:
    return Solution().countBattleships(board)