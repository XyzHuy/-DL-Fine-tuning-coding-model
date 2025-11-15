import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkString(self, s: str) -> bool:
        # Check if the string contains the pattern 'ba'
        # If it does, it means there is at least one 'a' that appears after a 'b'
        return 'ba' not in s

def checkString(s: str) -> bool:
    return Solution().checkString(s)