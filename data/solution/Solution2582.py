import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Calculate the number of complete cycles and the remaining time
        cycle_length = 2 * (n - 1)
        complete_cycles = time // cycle_length
        remaining_time = time % cycle_length
        
        # Determine the position based on the remaining time
        if remaining_time < n:
            # Pillow is moving forward
            return remaining_time + 1
        else:
            # Pillow is moving backward
            return n - (remaining_time - (n - 1))

def passThePillow(n: int, time: int) -> int:
    return Solution().passThePillow(n, time)