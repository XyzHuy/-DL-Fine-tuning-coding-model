import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Find the positions where the characters in the two strings differ
        diff = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        # If there are no differences, the strings are already equal
        if not diff:
            return True
        
        # If there are exactly two differences, check if swapping them makes the strings equal
        if len(diff) == 2:
            return diff[0] == diff[1][::-1]
        
        # If there are more than two differences, it's not possible to make the strings equal with one swap
        return False

def areAlmostEqual(s1: str, s2: str) -> bool:
    return Solution().areAlmostEqual(s1, s2)