import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def markCandiesToCrush(board):
            to_crush = set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j + 2 < len(board[0]) and board[i][j] != 0 and board[i][j] == board[i][j + 1] == board[i][j + 2]:
                        to_crush.update({(i, j), (i, j + 1), (i, j + 2)})
                    if i + 2 < len(board) and board[i][j] != 0 and board[i][j] == board[i + 1][j] == board[i + 2][j]:
                        to_crush.update({(i, j), (i + 1, j), (i + 2, j)})
            return to_crush

        def crushCandies(board, to_crush):
            for i, j in to_crush:
                board[i][j] = 0

        def dropCandies(board):
            for j in range(len(board[0])):
                write_index = len(board) - 1
                for i in range(len(board) - 1, -1, -1):
                    if board[i][j] != 0:
                        board[write_index][j] = board[i][j]
                        write_index -= 1
                for i in range(write_index, -1, -1):
                    board[i][j] = 0

        while True:
            to_crush = markCandiesToCrush(board)
            if not to_crush:
                break
            crushCandies(board, to_crush)
            dropCandies(board)
        
        return board

def candyCrush(board: List[List[int]]) -> List[List[int]]:
    return Solution().candyCrush(board)