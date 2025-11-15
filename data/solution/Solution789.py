import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # Calculate the Manhattan distance from (0, 0) to the target
        player_distance = abs(target[0]) + abs(target[1])
        
        # Check the distance from each ghost to the target
        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_distance <= player_distance:
                return False
        
        return True

def escapeGhosts(ghosts: List[List[int]], target: List[int]) -> bool:
    return Solution().escapeGhosts(ghosts, target)