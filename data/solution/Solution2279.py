import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Calculate the remaining capacity for each bag
        remaining_capacity = [capacity[i] - rocks[i] for i in range(len(capacity))]
        
        # Sort the remaining capacities in ascending order
        remaining_capacity.sort()
        
        # Initialize the count of full bags
        full_bags = 0
        
        # Iterate through the sorted remaining capacities
        for capacity in remaining_capacity:
            if additionalRocks >= capacity:
                additionalRocks -= capacity
                full_bags += 1
            else:
                break
        
        return full_bags

def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    return Solution().maximumBags(capacity, rocks, additionalRocks)