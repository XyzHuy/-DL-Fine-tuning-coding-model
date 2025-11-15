import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        highest_altitude = 0
        
        for g in gain:
            current_altitude += g
            highest_altitude = max(highest_altitude, current_altitude)
        
        return highest_altitude

def largestAltitude(gain: List[int]) -> int:
    return Solution().largestAltitude(gain)