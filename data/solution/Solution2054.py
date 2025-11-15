import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by their start times
        events.sort()
        
        # Extract start times for binary search
        start_times = [event[0] for event in events]
        
        # Initialize a suffix max array to store the maximum value of events from the current index to the end
        n = len(events)
        suffix_max = [0] * (n + 1)
        suffix_max[n - 1] = events[n - 1][2]
        
        # Fill the suffix max array
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])
        
        max_value = 0
        
        # Iterate through each event to find the maximum sum of two non-overlapping events
        for i in range(n):
            _, end, value = events[i]
            # Find the first event that starts after the current event ends
            next_event_index = bisect_right(start_times, end)
            # Calculate the maximum value by considering the current event and the best non-overlapping event after it
            max_value = max(max_value, value + suffix_max[next_event_index])
        
        return max_value

def maxTwoEvents(events: List[List[int]]) -> int:
    return Solution().maxTwoEvents(events)