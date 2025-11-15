import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert each time point to minutes since midnight
        minutes = []
        for time in timePoints:
            hours, mins = map(int, time.split(':'))
            total_minutes = hours * 60 + mins
            minutes.append(total_minutes)
        
        # Sort the list of minutes
        minutes.sort()
        
        # Initialize the minimum difference with the difference between the first and last time
        min_diff = (24 * 60) - (minutes[-1] - minutes[0])
        
        # Find the minimum difference between consecutive time points
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)
        
        return min_diff

def findMinDifference(timePoints: List[str]) -> int:
    return Solution().findMinDifference(timePoints)