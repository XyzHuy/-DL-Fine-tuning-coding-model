import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current_height = 0
        additional_rungs = 0
        
        for rung in rungs:
            # Calculate the number of rungs needed to reach the current rung
            if rung - current_height > dist:
                additional_rungs += (rung - current_height - 1) // dist
            current_height = rung
        
        return additional_rungs

def addRungs(rungs: List[int], dist: int) -> int:
    return Solution().addRungs(rungs, dist)