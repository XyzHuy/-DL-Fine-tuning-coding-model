import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def adjacent_mines(r, c):
            count = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'M':
                        count += 1
            return count

        def dfs(r, c):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return
            if board[r][c] != 'E':
                return
            
            mine_count = adjacent_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        dfs(r + dr, c + dc)

        # Check if the click is on a mine
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # Perform DFS from the click position
        dfs(click[0], click[1])
        return board

def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
    return Solution().updateBoard(board, click)