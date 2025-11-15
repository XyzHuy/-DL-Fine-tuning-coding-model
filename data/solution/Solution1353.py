import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by their start day
        events.sort()
        min_heap = []  # This will store the end days of events
        day = 0  # Current day
        event_index = 0  # Index to track the current event
        max_events_attended = 0  # Count of events attended

        # Iterate through the days
        while event_index < len(events) or min_heap:
            # If the heap is empty, fast forward to the next event's start day
            if not min_heap:
                day = events[event_index][0]
            
            # Push all events that start on the current day into the heap
            while event_index < len(events) and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1
            
            # Attend the event that ends the earliest
            heapq.heappop(min_heap)
            max_events_attended += 1
            day += 1
            
            # Remove all events from the heap that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

        return max_events_attended

def maxEvents(events: List[List[int]]) -> int:
    return Solution().maxEvents(events)