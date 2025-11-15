import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            # Check if the segment is a valid IP segment
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)
        
        def backtrack(start=0, path=[]):
            # If we have 4 segments and we reached the end of the string, we found a valid IP
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            # Try to create segments of length 1, 2, and 3
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if is_valid(segment):
                        backtrack(start + length, path + [segment])
        
        result = []
        backtrack()
        return result

def restoreIpAddresses(s: str) -> List[str]:
    return Solution().restoreIpAddresses(s)