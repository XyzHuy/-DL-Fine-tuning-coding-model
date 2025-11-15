import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the costs in descending order
        cost.sort(reverse=True)
        
        total_cost = 0
        n = len(cost)
        
        # Iterate over the sorted costs
        for i in range(n):
            # Add the cost of the candy to the total cost
            total_cost += cost[i]
            # If the next candy is the third one in a sequence of three, skip it as it's free
            if (i + 1) % 3 == 0:
                total_cost -= cost[i]
        
        return total_cost

def minimumCost(cost: List[int]) -> int:
    return Solution().minimumCost(cost)