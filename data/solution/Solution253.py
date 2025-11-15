import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Create a list of all events: start and end times
        events = []
        for start, end in intervals:
            events.append((start, 1))  # Meeting starts
            events.append((end, -1))   # Meeting ends
        
        # Sort events by time. If two events have the same time, end comes before start
        events.sort()
        
        # Initialize variables to keep track of the current number of rooms and the maximum number of rooms needed
        current_rooms = 0
        max_rooms = 0
        
        # Process each event in the sorted list
        for time, delta in events:
            current_rooms += delta  # Update the number of current rooms
            max_rooms = max(max_rooms, current_rooms)  # Update the maximum number of rooms needed
        
        return max_rooms

def minMeetingRooms(intervals: List[List[int]]) -> int:
    return Solution().minMeetingRooms(intervals)