import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Sort tasks by their end time
        tasks.sort(key=lambda x: x[1])
        
        # Initialize a set to keep track of the seconds the computer is on
        on_time = set()
        
        for start, end, duration in tasks:
            # Count how many seconds this task is already covered
            covered = sum(1 for t in range(start, end + 1) if t in on_time)
            
            # Calculate the remaining duration needed
            remaining_duration = duration - covered
            
            # If there's a remaining duration, turn on the computer for the needed seconds
            if remaining_duration > 0:
                # Turn on the computer for the remaining duration starting from the end time
                for t in range(end, start - 1, -1):
                    if remaining_duration == 0:
                        break
                    if t not in on_time:
                        on_time.add(t)
                        remaining_duration -= 1
        
        # The size of the set is the minimum time the computer needs to be on
        return len(on_time)

def findMinimumTime(tasks: List[List[int]]) -> int:
    return Solution().findMinimumTime(tasks)