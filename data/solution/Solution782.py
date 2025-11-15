import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Check the parity of the board
        for r in range(n):
            for c in range(n):
                if (board[0][0] ^ board[r][0] ^ board[0][c] ^ board[r][c]) == 1:
                    return -1
        
        # Count the number of 0s and 1s in the first row and column
        rowSum = colSum = rowSwap = colSwap = 0
        for i in range(n):
            rowSum += board[0][i]
            colSum += board[i][0]
            if board[i][0] == i % 2:
                rowSwap += 1
            if board[0][i] == i % 2:
                colSwap += 1
        
        # If the number of 0s is not equal to the number of 1s, it's impossible
        if n // 2 > rowSum or rowSum > (n + 1) // 2:
            return -1
        if n // 2 > colSum or colSum > (n + 1) // 2:
            return -1
        
        # If n is even, rowSwap and colSwap must be even
        if n % 2 == 0:
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)
        else:
            if rowSwap % 2 == 1:
                rowSwap = n - rowSwap
            if colSwap % 2 == 1:
                colSwap = n - colSwap
        
        return (rowSwap + colSwap) // 2

def movesToChessboard(board: List[List[int]]) -> int:
    return Solution().movesToChessboard(board)