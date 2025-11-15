import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start with the square root of the area as the initial width
        w = int(math.sqrt(area))
        
        # Find the largest width that is a factor of the area
        while area % w != 0:
            w -= 1
        
        # Calculate the corresponding length
        l = area // w
        
        return [l, w]

def constructRectangle(area: int) -> List[int]:
    return Solution().constructRectangle(area)