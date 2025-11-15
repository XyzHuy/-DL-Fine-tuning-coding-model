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
    def validTicTacToe(self, board: List[str]) -> bool:
        # Count the number of 'X' and 'O' on the board
        count_x = sum(row.count('X') for row in board)
        count_o = sum(row.count('O') for row in board)
        
        # Check if the number of 'X' is not equal to 'O' or 'O' + 1
        if not (count_x == count_o or count_x == count_o + 1):
            return False
        
        # Function to check if a player has won
        def wins(player):
            # Check rows and columns
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or \
                   all(board[j][i] == player for j in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)) or \
               all(board[i][2 - i] == player for i in range(3)):
                return True
            return False
        
        # Check if both players have won
        if wins('X') and wins('O'):
            return False
        
        # Check if 'X' wins but the count of 'X' is not one more than 'O'
        if wins('X') and count_x != count_o + 1:
            return False
        
        # Check if 'O' wins but the count of 'X' is not equal to 'O'
        if wins('O') and count_x != count_o:
            return False
        
        # If all checks pass, the board is valid
        return True

def validTicTacToe(board: List[str]) -> bool:
    return Solution().validTicTacToe(board)