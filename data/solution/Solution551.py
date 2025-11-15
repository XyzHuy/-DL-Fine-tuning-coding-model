import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if the student has fewer than 2 absences
        if s.count('A') >= 2:
            return False
        
        # Check if the student was never late for 3 or more consecutive days
        if "LLL" in s:
            return False
        
        return True

def checkRecord(s: str) -> bool:
    return Solution().checkRecord(s)