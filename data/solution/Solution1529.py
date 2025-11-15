import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        n = len(target)
        i = 0
        
        # Skip leading zeros
        while i < n and target[i] == '0':
            i += 1
        
        # Count the number of flip transitions
        while i < n:
            if i == 0 or target[i] != target[i - 1]:
                flips += 1
            i += 1
        
        return flips

def minFlips(target: str) -> int:
    return Solution().minFlips(target)