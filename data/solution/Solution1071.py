import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Helper function to check if s divides t
        def divides(s, t):
            return t == (s * (len(t) // len(s)))
        
        # Ensure str1 is the longer string
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        # Iterate from the longest possible substring to the shortest
        for i in range(len(str2), 0, -1):
            candidate = str2[:i]
            if divides(candidate, str1) and divides(candidate, str2):
                return candidate
        
        return ""

def gcdOfStrings(str1: str, str2: str) -> str:
    return Solution().gcdOfStrings(str1, str2)