import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        
        passenger_set = set(passengers)
        i = 0  # Pointer for passengers
        last_boarding_time = 0
        
        for bus in buses:
            current_capacity = capacity
            while current_capacity > 0 and i < len(passengers) and passengers[i] <= bus:
                last_boarding_time = passengers[i]
                i += 1
                current_capacity -= 1
            
            if current_capacity > 0:
                last_boarding_time = bus
        
        # Find the latest time to arrive
        while last_boarding_time in passenger_set:
            last_boarding_time -= 1
        
        return last_boarding_time

def latestTimeCatchTheBus(buses: List[int], passengers: List[int], capacity: int) -> int:
    return Solution().latestTimeCatchTheBus(buses, passengers, capacity)