import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # Initialize the closest cost with the first base cost
        closest_cost = baseCosts[0]
        
        # Function to update the closest cost
        def update_closest(current_cost):
            nonlocal closest_cost
            if abs(current_cost - target) < abs(closest_cost - target) or \
               (abs(current_cost - target) == abs(closest_cost - target) and current_cost < closest_cost):
                closest_cost = current_cost
        
        # Generate all possible topping combinations
        def dfs(index, current_cost):
            update_closest(current_cost)
            if index == len(toppingCosts):
                return
            # Try 0, 1, or 2 of the current topping
            for amount in range(3):
                if current_cost + amount * toppingCosts[index] <= target + abs(closest_cost - target):
                    dfs(index + 1, current_cost + amount * toppingCosts[index])
        
        # Try each base cost with all topping combinations
        for base in baseCosts:
            dfs(0, base)
        
        return closest_cost

def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    return Solution().closestCost(baseCosts, toppingCosts, target)