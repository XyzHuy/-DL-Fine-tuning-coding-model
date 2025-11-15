import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        
        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            numBottles = 1
            total_drunk += numBottles
            empty_bottles += numBottles
            numExchange += 1
        
        return total_drunk

def maxBottlesDrunk(numBottles: int, numExchange: int) -> int:
    return Solution().maxBottlesDrunk(numBottles, numExchange)