import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # Initialize the previous house's costs with the first house's costs
        prev_red, prev_blue, prev_green = costs[0]
        
        # Iterate over the costs starting from the second house
        for red, blue, green in costs[1:]:
            # Calculate the minimum cost for the current house with each color
            # Ensure no two adjacent houses have the same color
            curr_red = red + min(prev_blue, prev_green)
            curr_blue = blue + min(prev_red, prev_green)
            curr_green = green + min(prev_red, prev_blue)
            
            # Update the previous costs to the current costs for the next iteration
            prev_red, prev_blue, prev_green = curr_red, curr_blue, curr_green
        
        # The result is the minimum cost among the last house's three color costs
        return min(prev_red, prev_blue, prev_green)

def minCost(costs: List[List[int]]) -> int:
    return Solution().minCost(costs)