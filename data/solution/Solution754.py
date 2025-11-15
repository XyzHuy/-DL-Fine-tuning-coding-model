import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def reachNumber(self, target: int) -> int:
        # Since the problem is symmetric, we can assume target is positive
        target = abs(target)
        
        # Initialize the number of moves
        numMoves = 0
        currentSum = 0
        
        # Keep adding moves until the currentSum is at least target
        # and the difference between currentSum and target is even
        while currentSum < target or (currentSum - target) % 2 != 0:
            numMoves += 1
            currentSum += numMoves
        
        return numMoves

def reachNumber(target: int) -> int:
    return Solution().reachNumber(target)