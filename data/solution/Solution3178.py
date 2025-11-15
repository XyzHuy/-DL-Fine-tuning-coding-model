import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # Calculate the number of full cycles of passing the ball to the end and back
        full_cycles = k // (2 * n - 2)
        # Calculate the remaining steps after full cycles
        remaining_steps = k % (2 * n - 2)
        
        # If remaining steps are less than n, ball is still moving to the right
        if remaining_steps < n:
            return remaining_steps
        else:
            # Otherwise, ball is moving to the left
            return 2 * n - 2 - remaining_steps

def numberOfChild(n: int, k: int) -> int:
    return Solution().numberOfChild(n, k)