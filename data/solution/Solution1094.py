import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Create a dictionary to store the changes in the number of passengers at each location
        stops = defaultdict(int)
        
        # For each trip, add the number of passengers at the start location and subtract at the end location
        for numPassengers, from_i, to_i in trips:
            stops[from_i] += numPassengers
            stops[to_i] -= numPassengers
        
        # Initialize the current number of passengers in the car
        current_passengers = 0
        
        # Iterate over the locations in sorted order
        for location in sorted(stops):
            # Update the current number of passengers
            current_passengers += stops[location]
            
            # If the current number of passengers exceeds the capacity, return False
            if current_passengers > capacity:
                return False
        
        # If we never exceeded the capacity, return True
        return True

def carPooling(trips: List[List[int]], capacity: int) -> bool:
    return Solution().carPooling(trips, capacity)