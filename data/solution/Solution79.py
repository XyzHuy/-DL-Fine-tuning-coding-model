import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False
            
            # Mark the cell as visited
            temp, board[x][y] = board[x][y], '#'
            
            # Explore neighbors
            found = (dfs(x + 1, y, index + 1) or
                     dfs(x - 1, y, index + 1) or
                     dfs(x, y + 1, index + 1) or
                     dfs(x, y - 1, index + 1))
            
            # Unmark the cell
            board[x][y] = temp
            
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

def exist(board: List[List[str]], word: str) -> bool:
    return Solution().exist(board, word)