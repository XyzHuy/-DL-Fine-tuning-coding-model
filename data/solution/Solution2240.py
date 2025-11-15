import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if total < 0:
            return 0
        
        # Ensure cost1 is the larger cost to minimize the number of iterations
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1
        
        ways = 0
        # Iterate over the number of pens we can buy
        for pens in range(total // cost1 + 1):
            remaining_money = total - pens * cost1
            # Calculate the number of pencils we can buy with the remaining money
            pencils = remaining_money // cost2
            # Each combination of pens and pencils is a distinct way to spend the money
            ways += pencils + 1
        
        return ways

def waysToBuyPensPencils(total: int, cost1: int, cost2: int) -> int:
    return Solution().waysToBuyPensPencils(total, cost1, cost2)