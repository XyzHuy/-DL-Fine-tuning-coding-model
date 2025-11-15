import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def can_place(word, row):
            n = len(word)
            m = len(row)
            for i in range(m - n + 1):
                if (i == 0 or row[i - 1] == '#') and (i + n == m or row[i + n] == '#'):
                    can_place = True
                    for j in range(n):
                        if row[i + j] not in (' ', word[j]):
                            can_place = False
                            break
                    if can_place:
                        return True
            return False
        
        def can_place_transposed(board, word):
            transposed_board = list(zip(*board))
            return any(can_place(word, row) for row in transposed_board)
        
        for row in board:
            if can_place(word, row) or can_place(word[::-1], row):
                return True
        
        if can_place_transposed(board, word) or can_place_transposed(board, word[::-1]):
            return True
        
        return False

def placeWordInCrossword(board: List[List[str]], word: str) -> bool:
    return Solution().placeWordInCrossword(board, word)