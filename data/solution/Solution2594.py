import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Helper function to check if we can repair all cars within a given time
        def canRepairWithinTime(time):
            total_cars_repaired = 0
            for rank in ranks:
                # Calculate the number of cars the current mechanic can repair in the given time
                total_cars_repaired += int(math.sqrt(time // rank))
            return total_cars_repaired >= cars
        
        # Binary search setup
        left, right = 0, min(ranks) * cars * cars  # min(ranks) * cars^2 is the upper bound
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            if canRepairWithinTime(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def repairCars(ranks: List[int], cars: int) -> int:
    return Solution().repairCars(ranks, cars)