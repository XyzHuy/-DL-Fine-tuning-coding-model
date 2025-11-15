import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Build a graph where each node is a bus stop and each edge represents a bus transfer
        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)
        
        # BFS initialization
        queue = deque([(source, 0)])  # (current_stop, num_buses_taken)
        visited_stops = set([source])
        visited_buses = set()
        
        while queue:
            current_stop, num_buses_taken = queue.popleft()
            
            # Check all buses that can be taken from the current stop
            for bus_id in stop_to_buses[current_stop]:
                if bus_id in visited_buses:
                    continue
                
                # Visit all stops that can be reached by the current bus
                for next_stop in routes[bus_id]:
                    if next_stop in visited_stops:
                        continue
                    
                    if next_stop == target:
                        return num_buses_taken + 1
                    
                    visited_stops.add(next_stop)
                    queue.append((next_stop, num_buses_taken + 1))
                
                # Mark the bus as visited to avoid re-processing
                visited_buses.add(bus_id)
        
        return -1

def numBusesToDestination(routes: List[List[int]], source: int, target: int) -> int:
    return Solution().numBusesToDestination(routes, source, target)