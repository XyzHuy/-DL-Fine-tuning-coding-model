import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate the distance between start and end positions
        distance = abs(endPos - startPos)
        
        # If the distance is greater than k or (k - distance) is odd, it's impossible to reach
        if distance > k or (k - distance) % 2 != 0:
            return 0
        
        # Calculate the number of right steps needed
        right_steps = (k + distance) // 2
        
        # Calculate the number of ways to choose right_steps out of k steps
        # This is a combination problem: C(k, right_steps) = k! / (right_steps! * (k - right_steps)!)
        from math import comb
        return comb(k, right_steps) % MOD

def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    return Solution().numberOfWays(startPos, endPos, k)