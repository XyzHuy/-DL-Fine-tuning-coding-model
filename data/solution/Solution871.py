import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Max-heap to store the amount of fuel at each station we passed by
        max_heap = []
        current_fuel = startFuel
        refuel_stops = 0
        stations.append([target, 0])  # Add the target as a final "station" with 0 fuel
        
        for position, fuel in stations:
            # While we don't have enough fuel to reach the current station
            while max_heap and current_fuel < position:
                # Refuel with the largest available fuel from the stations we've passed
                current_fuel -= heapq.heappop(max_heap)
                refuel_stops += 1
            
            # If even after refueling from all passed stations we can't reach the current station, return -1
            if current_fuel < position:
                return -1
            
            # Add the current station's fuel to the max-heap (as negative for max-heap behavior)
            heapq.heappush(max_heap, -fuel)
        
        return refuel_stops

def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    return Solution().minRefuelStops(target, startFuel, stations)