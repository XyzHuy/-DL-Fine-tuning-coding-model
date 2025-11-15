import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        
        # If the total number of dresses is not divisible by the number of machines, it's impossible to balance
        if total_dresses % n != 0:
            return -1
        
        target_dresses = total_dresses // n
        left_excess = 0
        max_moves = 0
        
        for dresses in machines:
            # Calculate the excess dresses on the left side of the current machine
            left_excess += dresses - target_dresses
            
            # The number of moves required at the current machine is the maximum of:
            # 1. The dresses that need to be moved from the left to the right
            # 2. The dresses that need to be moved from the right to the left (tracked by left_excess)
            # 3. The current machine's excess dresses (or deficit)
            max_moves = max(max_moves, abs(left_excess), dresses - target_dresses)
        
        return max_moves

def findMinMoves(machines: List[int]) -> int:
    return Solution().findMinMoves(machines)