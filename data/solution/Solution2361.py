import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        # Initialize the cost to reach the first stop on regular and express routes
        regular_cost = [0] * (n + 1)
        express_cost = [0] * (n + 1)
        
        # Starting point
        regular_cost[0] = 0
        express_cost[0] = expressCost
        
        # Initialize the result array
        costs = [0] * n
        
        for i in range(1, n + 1):
            # Cost to reach stop i using regular route
            regular_cost[i] = min(regular_cost[i - 1] + regular[i - 1], express_cost[i - 1] + express[i - 1])
            
            # Cost to reach stop i using express route
            express_cost[i] = min(express_cost[i - 1] + express[i - 1], regular_cost[i - 1] + regular[i - 1] + expressCost)
            
            # The minimum cost to reach stop i (1-indexed in the result)
            costs[i - 1] = min(regular_cost[i], express_cost[i])
        
        return costs

def minimumCosts(regular: List[int], express: List[int], expressCost: int) -> List[int]:
    return Solution().minimumCosts(regular, express, expressCost)