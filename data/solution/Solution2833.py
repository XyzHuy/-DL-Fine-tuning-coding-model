import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_count = moves.count('L')
        right_count = moves.count('R')
        wildcard_count = moves.count('_')
        
        # If there are more 'L's, use all '_' to move left
        if left_count >= right_count:
            return left_count - right_count + wildcard_count
        else:
            # If there are more 'R's, use all '_' to move right
            return right_count - left_count + wildcard_count

def furthestDistanceFromOrigin(moves: str) -> int:
    return Solution().furthestDistanceFromOrigin(moves)