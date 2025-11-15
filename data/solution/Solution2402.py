import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by their start times
        meetings.sort()
        
        # Initialize a min-heap to keep track of available rooms and their next available times
        available_rooms = list(range(n))
        ongoing_meetings = []
        
        # Counter to keep track of the number of meetings held in each room
        room_count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have finished meetings before the current meeting starts
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)
            
            if available_rooms:
                # Allocate the room with the lowest number
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                # Delay the meeting until the earliest room becomes free
                next_available_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(ongoing_meetings, (next_available_time + (end - start), room))
            
            # Increment the count of meetings held in the allocated room
            room_count[room] += 1
        
        # Find the room that held the most meetings
        max_meetings = max(room_count)
        return room_count.index(max_meetings)

def mostBooked(n: int, meetings: List[List[int]]) -> int:
    return Solution().mostBooked(n, meetings)