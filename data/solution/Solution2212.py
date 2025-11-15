import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_points = 0
        best_bob = [0] * 12
        
        # There are 2^12 possible ways for Bob to shoot arrows (each section can be won or not)
        for i in range(1 << 12):
            bob_points = 0
            arrows_used = 0
            bob = [0] * 12
            
            for k in range(12):
                if i & (1 << k):  # Check if k-th bit is set
                    bob[k] = aliceArrows[k] + 1
                    arrows_used += bob[k]
                    bob_points += k
            
            if arrows_used <= numArrows and bob_points > max_points:
                max_points = bob_points
                best_bob = bob[:]
        
        # If we have arrows left, we can add them to the 0th section
        remaining_arrows = numArrows - sum(best_bob)
        best_bob[0] += remaining_arrows
        
        return best_bob

def maximumBobPoints(numArrows: int, aliceArrows: List[int]) -> List[int]:
    return Solution().maximumBobPoints(numArrows, aliceArrows)