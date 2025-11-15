import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths of s and goal are different
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself
        concatenated = s + s
        
        # Check if goal is a substring of the concatenated string
        return goal in concatenated

def rotateString(s: str, goal: str) -> bool:
    return Solution().rotateString(s, goal)