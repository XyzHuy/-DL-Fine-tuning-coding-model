import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_capacity = capacity
        n = len(plants)
        
        for i in range(n):
            if current_capacity >= plants[i]:
                steps += 1  # Move to the next plant
                current_capacity -= plants[i]  # Water the plant
            else:
                # Refill the can
                steps += 2 * i + 1  # Steps to go back to the river and return
                current_capacity = capacity - plants[i]  # Water the plant after refill
        
        return steps

def wateringPlants(plants: List[int], capacity: int) -> int:
    return Solution().wateringPlants(plants, capacity)