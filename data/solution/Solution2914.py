import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        n = len(s)
        
        # Iterate over the string in steps of 2
        for i in range(0, n, 2):
            # If the pair of characters are not the same, a change is needed
            if s[i] != s[i + 1]:
                changes += 1
                
        return changes

def minChanges(s: str) -> int:
    return Solution().minChanges(s)