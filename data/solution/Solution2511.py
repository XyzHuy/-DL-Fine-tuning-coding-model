import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captured = 0
        last_fort_position = -1
        
        for i in range(len(forts)):
            if forts[i] != 0:
                if last_fort_position != -1 and forts[last_fort_position] == -forts[i]:
                    max_captured = max(max_captured, i - last_fort_position - 1)
                last_fort_position = i
        
        return max_captured

def captureForts(forts: List[int]) -> int:
    return Solution().captureForts(forts)