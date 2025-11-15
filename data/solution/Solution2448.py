import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # Create a list of tuples (num, cost) and sort it by num
        num_cost_pairs = sorted(zip(nums, cost))
        
        # Calculate the total cost if all elements are made equal to the first element
        total_cost = 0
        target = num_cost_pairs[0][0]
        for num, c in num_cost_pairs:
            total_cost += abs(num - target) * c
        
        # Initialize the current cost to the total cost calculated above
        current_cost = total_cost
        
        # Calculate the prefix sum of costs
        prefix_cost = [0] * len(nums)
        prefix_cost[0] = num_cost_pairs[0][1]
        for i in range(1, len(nums)):
            prefix_cost[i] = prefix_cost[i - 1] + num_cost_pairs[i][1]
        
        # Iterate through each possible target value
        for i in range(1, len(nums)):
            num, c = num_cost_pairs[i]
            prev_num = num_cost_pairs[i - 1][0]
            
            # Update the current cost by adjusting for the change in target
            current_cost += (prefix_cost[i - 1] - (prefix_cost[-1] - prefix_cost[i - 1])) * (num - prev_num)
            
            # Update the total cost if the current cost is lower
            total_cost = min(total_cost, current_cost)
        
        return total_cost

def minCost(nums: List[int], cost: List[int]) -> int:
    return Solution().minCost(nums, cost)