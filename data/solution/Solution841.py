import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Initialize a set to keep track of visited rooms
        visited = set()
        
        # Start with room 0
        stack = [0]
        
        # Perform a depth-first search (DFS) to visit all reachable rooms
        while stack:
            current_room = stack.pop()
            visited.add(current_room)
            
            # Add all keys found in the current room to the stack if they haven't been visited
            for key in rooms[current_room]:
                if key not in visited:
                    stack.append(key)
        
        # Check if we have visited all rooms
        return len(visited) == len(rooms)

def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    return Solution().canVisitAllRooms(rooms)