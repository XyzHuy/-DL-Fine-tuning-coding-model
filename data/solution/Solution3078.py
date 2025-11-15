import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        def is_match(board_submatrix, pattern):
            char_to_digit = {}
            digit_to_char = {}
            
            for i in range(len(pattern)):
                for j in range(len(pattern[0])):
                    pat_char = pattern[i][j]
                    board_digit = board_submatrix[i][j]
                    
                    if pat_char.isdigit():
                        if int(pat_char) != board_digit:
                            return False
                    else:
                        if pat_char in char_to_digit:
                            if char_to_digit[pat_char] != board_digit:
                                return False
                        elif board_digit in digit_to_char:
                            if digit_to_char[board_digit] != pat_char:
                                return False
                        else:
                            char_to_digit[pat_char] = board_digit
                            digit_to_char[board_digit] = pat_char
            
            return True
        
        rows, cols = len(board), len(board[0])
        pat_rows, pat_cols = len(pattern), len(pattern[0])
        
        for i in range(rows - pat_rows + 1):
            for j in range(cols - pat_cols + 1):
                board_submatrix = [board[x][j:j+pat_cols] for x in range(i, i+pat_rows)]
                if is_match(board_submatrix, pattern):
                    return [i, j]
        
        return [-1, -1]

def findPattern(board: List[List[int]], pattern: List[str]) -> List[int]:
    return Solution().findPattern(board, pattern)