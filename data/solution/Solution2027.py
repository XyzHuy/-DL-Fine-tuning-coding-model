import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                # If we encounter an 'X', we need to make a move
                moves += 1
                # Skip the next two characters as they will be converted to 'O'
                i += 3
            else:
                # If it's 'O', just move to the next character
                i += 1
        return moves

def minimumMoves(s: str) -> int:
    return Solution().minimumMoves(s)