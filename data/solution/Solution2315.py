import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countAsterisks(self, s: str) -> int:
        # Split the string by '|' to get segments
        segments = s.split('|')
        count = 0
        
        # Iterate over the segments, considering only those at even indices
        for i in range(0, len(segments), 2):
            count += segments[i].count('*')
        
        return count

def countAsterisks(s: str) -> int:
    return Solution().countAsterisks(s)