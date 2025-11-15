import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Sort rooms by size in descending order
        rooms.sort(key=lambda x: -x[1])
        
        # Add index to queries to keep track of the original order
        queries = [(preferred, minSize, idx) for idx, (preferred, minSize) in enumerate(queries)]
        
        # Sort queries by minSize in descending order
        queries.sort(key=lambda x: -x[1])
        
        available_rooms = []
        answer = [-1] * len(queries)
        room_index = 0
        
        for preferred, minSize, idx in queries:
            # Add rooms that meet the current query's minSize requirement
            while room_index < len(rooms) and rooms[room_index][1] >= minSize:
                bisect.insort(available_rooms, rooms[room_index][0])
                room_index += 1
            
            # If there are no available rooms that meet the requirement, answer is -1
            if not available_rooms:
                continue
            
            # Find the position to insert the preferred room id in the sorted list
            pos = bisect.bisect_left(available_rooms, preferred)
            
            # Check the closest room id to the preferred id
            if pos == 0:
                answer[idx] = available_rooms[0]
            elif pos == len(available_rooms):
                answer[idx] = available_rooms[-1]
            else:
                # Compare the closest room ids on both sides of the position
                left_diff = abs(preferred - available_rooms[pos - 1])
                right_diff = abs(preferred - available_rooms[pos])
                if left_diff <= right_diff:
                    answer[idx] = available_rooms[pos - 1]
                else:
                    answer[idx] = available_rooms[pos]
        
        return answer

def closestRoom(rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
    return Solution().closestRoom(rooms, queries)