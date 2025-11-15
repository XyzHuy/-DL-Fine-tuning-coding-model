import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles == 0:
                # If no more doubles are allowed, just increment to 1
                return moves + target - 1
            if target % 2 == 0:
                # If target is even, we can use a double operation
                target //= 2
                maxDoubles -= 1
            else:
                # If target is odd, decrement it by 1 to make it even
                target -= 1
            moves += 1
        return moves

def minMoves(target: int, maxDoubles: int) -> int:
    return Solution().minMoves(target, maxDoubles)