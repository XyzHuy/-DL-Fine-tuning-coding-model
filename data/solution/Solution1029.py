import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort the costs array based on the difference between the cost of flying to city A and city B
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        # Assign the first n people to city A and the remaining to city B
        for i in range(n):
            total_cost += costs[i][0]  # Cost to fly to city A
            total_cost += costs[i + n][1]  # Cost to fly to city B
        
        return total_cost

def twoCitySchedCost(costs: List[List[int]]) -> int:
    return Solution().twoCitySchedCost(costs)