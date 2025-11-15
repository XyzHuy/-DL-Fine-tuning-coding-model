import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # Sort both strings
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        
        # Check if s1_sorted can break s2_sorted
        can_s1_break_s2 = all(x >= y for x, y in zip(s1_sorted, s2_sorted))
        
        # Check if s2_sorted can break s1_sorted
        can_s2_break_s1 = all(x >= y for x, y in zip(s2_sorted, s1_sorted))
        
        # Return true if either condition is satisfied
        return can_s1_break_s2 or can_s2_break_s1

def checkIfCanBreak(s1: str, s2: str) -> bool:
    return Solution().checkIfCanBreak(s1, s2)