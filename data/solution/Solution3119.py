import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        # Split the road string by '.' to get segments of consecutive 'x'
        pothole_segments = road.split('.')
        
        # Calculate the cost and number of potholes for each segment
        pothole_info = [(len(segment), len(segment) + 1) for segment in pothole_segments if segment]
        
        # Sort segments by cost (len(segment) + 1) in ascending order
        pothole_info.sort(key=lambda x: x[1])
        
        total_fixed = 0
        
        # Iterate over sorted segments and fix as many as possible within the budget
        for potholes, cost in pothole_info:
            if budget >= cost:
                budget -= cost
                total_fixed += potholes
            else:
                # If we can't afford the whole segment, fix as many as we can
                while budget > 1 and potholes > 0:
                    budget -= 1
                    total_fixed += 1
                    potholes -= 1
                break
        
        return total_fixed

def maxPotholes(road: str, budget: int) -> int:
    return Solution().maxPotholes(road, budget)