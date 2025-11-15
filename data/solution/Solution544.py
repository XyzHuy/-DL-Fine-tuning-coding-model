import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findContestMatch(self, n: int) -> str:
        # Initialize the list of teams as strings
        teams = list(map(str, range(1, n + 1)))
        
        # Continue pairing until we have one final match
        while n > 1:
            # Pair the first team with the last, second with the second last, and so on
            teams = [f"({teams[i]},{teams[n - 1 - i]})" for i in range(n // 2)]
            # Halve the number of teams for the next round
            n //= 2
        
        # The final match is the only element left in the list
        return teams[0]

def findContestMatch(n: int) -> str:
    return Solution().findContestMatch(n)