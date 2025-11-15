import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph from the tickets
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        
        # Sort the destinations in lexical order
        for u in graph:
            graph[u].sort()
        
        # Result itinerary
        itinerary = []
        
        # Depth-first search function
        def dfs(city):
            # Visit all the neighbors of the current city
            while graph[city]:
                neighbor = graph[city].pop(0)
                dfs(neighbor)
            # Append the city to the itinerary
            itinerary.append(city)
        
        # Start the DFS from "JFK"
        dfs("JFK")
        
        # The itinerary is constructed in reverse order
        return itinerary[::-1]

def findItinerary(tickets: List[List[str]]) -> List[str]:
    return Solution().findItinerary(tickets)