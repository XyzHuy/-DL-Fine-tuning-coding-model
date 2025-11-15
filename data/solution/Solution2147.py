import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        # If the number of seats is not even or less than 2, return 0
        if len(seats) % 2 != 0 or len(seats) < 2:
            return 0
        
        # Calculate the number of ways to place dividers
        ways = 1
        for i in range(2, len(seats), 2):
            ways = (ways * (seats[i] - seats[i - 1])) % MOD
        
        return ways

def numberOfWays(corridor: str) -> int:
    return Solution().numberOfWays(corridor)