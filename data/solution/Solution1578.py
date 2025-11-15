import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        i = 0
        
        while i < len(colors):
            current_color = colors[i]
            max_cost = 0
            group_cost = 0
            
            # Traverse through all consecutive balloons of the same color
            while i < len(colors) and colors[i] == current_color:
                group_cost += neededTime[i]
                max_cost = max(max_cost, neededTime[i])
                i += 1
            
            # Add the cost of removing all but the most expensive balloon in the group
            total_cost += group_cost - max_cost
        
        return total_cost

def minCost(colors: str, neededTime: List[int]) -> int:
    return Solution().minCost(colors, neededTime)