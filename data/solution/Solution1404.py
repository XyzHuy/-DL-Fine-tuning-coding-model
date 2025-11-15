import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numSteps(self, s: str) -> int:
        # Convert the binary string to an integer
        num = int(s, 2)
        steps = 0
        
        # Reduce the number to 1 following the given rules
        while num > 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            steps += 1
        
        return steps

def numSteps(s: str) -> int:
    return Solution().numSteps(s)