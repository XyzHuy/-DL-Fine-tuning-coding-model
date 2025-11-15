import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Sort the friends by their arrival times
        arrival_times = sorted((arrival, i) for i, (arrival, leaving) in enumerate(times))
        leaving_times = []
        available_chairs = []
        max_chair_used = -1
        
        for arrival, i in arrival_times:
            # Free up all chairs that have been vacated by the time the current friend arrives
            while leaving_times and leaving_times[0][0] <= arrival:
                _, chair = heapq.heappop(leaving_times)
                heapq.heappush(available_chairs, chair)
            
            # Assign the smallest available chair
            if available_chairs:
                chair = heapq.heappop(available_chairs)
            else:
                max_chair_used += 1
                chair = max_chair_used
            
            # If the current friend is the target friend, return the chair they are sitting on
            if i == targetFriend:
                return chair
            
            # Add the current friend's leaving time to the heap
            heapq.heappush(leaving_times, (times[i][1], chair))
        
        return -1  # This line should never be reached given the problem constraints

def smallestChair(times: List[List[int]], targetFriend: int) -> int:
    return Solution().smallestChair(times, targetFriend)