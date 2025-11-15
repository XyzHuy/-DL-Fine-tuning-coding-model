import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Let x be the number of jumbo burgers and y be the number of small burgers
        # We have the following equations:
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices
        
        # We can solve these equations to find x and y
        # From the second equation, y = cheeseSlices - x
        # Substitute y in the first equation: 4x + 2(cheeseSlices - x) = tomatoSlices
        # Simplify: 4x + 2cheeseSlices - 2x = tomatoSlices
        # Simplify: 2x + 2cheeseSlices = tomatoSlices
        # Simplify: 2x = tomatoSlices - 2cheeseSlices
        # Simplify: x = (tomatoSlices - 2cheeseSlices) / 2
        
        # Check if x is a non-negative integer
        if (tomatoSlices - 2 * cheeseSlices) % 2 != 0 or (tomatoSlices - 2 * cheeseSlices) < 0:
            return []
        
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        
        # Now find y
        y = cheeseSlices - x
        
        # Check if y is non-negative
        if y < 0:
            return []
        
        return [x, y]

def numOfBurgers(tomatoSlices: int, cheeseSlices: int) -> List[int]:
    return Solution().numOfBurgers(tomatoSlices, cheeseSlices)