import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        max_robots = 0
        left = 0
        current_sum = 0
        dq = deque()  # Deque to store indices of chargeTimes in decreasing order of their values
        
        for right in range(n):
            # Add running cost of the current robot
            current_sum += runningCosts[right]
            
            # Maintain the deque to keep track of the maximum charge time
            while dq and chargeTimes[dq[-1]] <= chargeTimes[right]:
                dq.pop()
            dq.append(right)
            
            # Calculate the total cost for the current window
            k = right - left + 1
            total_cost = chargeTimes[dq[0]] + k * current_sum
            
            # If the total cost exceeds the budget, shrink the window from the left
            while total_cost > budget:
                current_sum -= runningCosts[left]
                if dq and dq[0] == left:
                    dq.popleft()
                left += 1
                k = right - left + 1
                total_cost = chargeTimes[dq[0]] + k * current_sum if k > 0 else 0
            
            # Update the maximum number of robots that can be run within the budget
            max_robots = max(max_robots, k)
        
        return max_robots

def maximumRobots(chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
    return Solution().maximumRobots(chargeTimes, runningCosts, budget)