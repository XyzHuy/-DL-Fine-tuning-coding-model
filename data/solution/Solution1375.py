import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flipped = 0
        blue_moments = 0
        
        for i, flip in enumerate(flips, start=1):
            max_flipped = max(max_flipped, flip)
            if max_flipped == i:
                blue_moments += 1
        
        return blue_moments

def numTimesAllBlue(flips: List[int]) -> int:
    return Solution().numTimesAllBlue(flips)