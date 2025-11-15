import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        n = len(team)
        caught = 0
        i, j = 0, 0
        
        while i < n and j < n:
            if team[i] == 0:  # Look for someone who is not "it"
                i += 1
            elif team[j] == 1:  # Look for someone who is "it"
                j += 1
            else:
                if i < j - dist or i > j + dist:
                    # If the current "it" cannot catch the current "not it", move the pointers
                    if i < j - dist:
                        i += 1
                    else:
                        j += 1
                else:
                    # If the current "it" can catch the current "not it", count the catch
                    caught += 1
                    i += 1
                    j += 1
        
        return caught

def catchMaximumAmountofPeople(team: List[int], dist: int) -> int:
    return Solution().catchMaximumAmountofPeople(team, dist)