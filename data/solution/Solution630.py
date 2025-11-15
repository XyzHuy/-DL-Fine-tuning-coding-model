import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort courses by their end day
        courses.sort(key=lambda x: x[1])
        
        max_heap = []  # This will store the durations of the courses taken so far
        total_time = 0  # This will keep track of the total time spent on courses
        
        for duration, end_day in courses:
            # Add the current course to the total time and the heap
            total_time += duration
            heapq.heappush(max_heap, -duration)  # Use max-heap by pushing negative duration
            
            # If the total time exceeds the end day, remove the longest course taken so far
            if total_time > end_day:
                longest_duration = heapq.heappop(max_heap)
                total_time += longest_duration  # This will be negative, effectively adding the duration
        
        # The size of the heap is the number of courses taken
        return len(max_heap)

def scheduleCourse(courses: List[List[int]]) -> int:
    return Solution().scheduleCourse(courses)