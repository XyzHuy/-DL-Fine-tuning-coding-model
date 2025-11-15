import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        total_cost = 0
        
        # Calculate the cost for moving to the target row
        if startPos[0] < homePos[0]:
            total_cost += sum(rowCosts[startPos[0] + 1:homePos[0] + 1])
        elif startPos[0] > homePos[0]:
            total_cost += sum(rowCosts[homePos[0]:startPos[0]])
        
        # Calculate the cost for moving to the target column
        if startPos[1] < homePos[1]:
            total_cost += sum(colCosts[startPos[1] + 1:homePos[1] + 1])
        elif startPos[1] > homePos[1]:
            total_cost += sum(colCosts[homePos[1]:startPos[1]])
        
        return total_cost

def minCost(startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
    return Solution().minCost(startPos, homePos, rowCosts, colCosts)