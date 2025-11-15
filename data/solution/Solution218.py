import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create a list of all the critical points (start and end of buildings)
        critical_points = set()
        for left, right, height in buildings:
            critical_points.add(left)
            critical_points.add(right)
        
        # Convert the set to a sorted list
        critical_points = sorted(critical_points)
        
        # Create a list of events, where each event is (left, -height, right) for start points
        # and (right, 0, 0) for end points. The negative height ensures that start points
        # are processed before end points when they share the same x-coordinate.
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
        
        # Sort events by x-coordinate. If two events have the same x-coordinate,
        # start points (negative height) come before end points (height 0).
        events.sort()
        
        # Initialize a max-heap with a sentinel value of (0, float('inf')) to represent
        # the ground level.
        max_heap = [(0, float('inf'))]
        
        # List to store the result skyline points
        result = []
        
        # Index to track the current position in the events list
        event_idx = 0
        n = len(events)
        
        # Iterate over each critical point
        for point in critical_points:
            # Process all events that happen at the current critical point
            while event_idx < n and events[event_idx][0] == point:
                _, height, right = events[event_idx]
                # Push the height (negative) and right boundary of the building into the heap
                heapq.heappush(max_heap, (height, right))
                event_idx += 1
            
            # Remove buildings from the heap that have ended before the current critical point
            while max_heap[0][1] <= point:
                heapq.heappop(max_heap)
            
            # The current maximum height in the heap is the height of the skyline at this point
            current_height = -max_heap[0][0]
            
            # If the current height is different from the last height in the result,
            # add it to the result skyline
            if not result or result[-1][1] != current_height:
                result.append([point, current_height])
        
        return result

# Example usage:
# sol = Solution()
# print(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))

def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    return Solution().getSkyline(buildings)